import json
import pkg_resources

from tornado import concurrent, gen, web


class StatusHandler(web.RequestHandler):
    """
    Simple handler that returns application status information.

    The easiest way to use this handler is to pass your package's
    name as the ``package`` kwarg to :class:`tornado.web.URLSpec`::

        app = web.Application([
            web.url('/status', StatusHandler, {'package': 'my-package'}),
        ])

    If your application is not bundled as a python package, then you can
    specify the name and version explicitly::

        app = web.Application([
            web.url('/status', StatusHandler,
                    {'name': 'my-package', 'version': '0.0.1'}),
        ])

    """

    def __init__(self, *args, **kwargs):
        self.name = 'UNKNOWN'
        self.version = '0.0.0'
        self.status = 'ok'
        self._package_name = None
        super(StatusHandler, self).__init__(*args, **kwargs)

    def initialize(self, **kwargs):
        """
        Sets the static information.

        :keyword str package: name of the package to retrieve
            metadata from
        :keyword str name: name of the application
        :keyword str version: application version number

        If the ``package`` keyword is specified, then the distribution
        is retrieved using :py:mod:`pkg_resources` and used as a source
        of status information.  Otherwise, the ``name`` and ``version``
        keywords are used.

        """
        if 'package' in kwargs:
            self._package_name = kwargs['package']
        else:
            self.name = kwargs.get('name') or self.name
            self.version = kwargs.get('version') or self.version

    @gen.coroutine
    def prepare(self):
        maybe_future = super(StatusHandler, self).prepare()
        if concurrent.is_future(maybe_future):
            yield maybe_future

        if not self._finished:
            if self._package_name is not None:
                try:
                    pkg_info = pkg_resources.get_distribution(
                        self._package_name)
                    self.name = pkg_info.project_name
                    self.version = pkg_info.version
                except pkg_resources.ResolutionError:
                    self.set_status(500)
                    self.finish()

    def get(self):
        """
        Returns a JSON object containing the application status.

        **Sample Response**

        .. code-block:: json

           {
              "name": "application-name",
              "version": "1.2.3",
              "status": "ok"
           }

        """
        self.set_status(200)
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'name': self.name,
                               'version': self.version,
                               'status': self.status}).encode('utf-8'))
        self.finish()
