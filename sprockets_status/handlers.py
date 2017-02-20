import json
import pkg_resources

from tornado import web


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
            pkg_info = pkg_resources.get_distribution(kwargs['package'])
            self.name = pkg_info.project_name
            self.version = pkg_info.version
        else:
            self.name = self.name or kwargs.get('name')
            self.version = self.version or kwargs.get('version')

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
