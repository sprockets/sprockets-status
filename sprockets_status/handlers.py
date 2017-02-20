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

    OK = 'ok'
    FAILURE = 'failed'

    _package_name = None
    _application_name = 'UNKNOWN'
    _application_version = None

    @property
    def application_name(self):
        """The application's reported name."""
        self._lookup_package_info()
        return self._application_name

    @property
    def application_version(self):
        """The application's version number."""
        self._lookup_package_info()
        return self._application_version

    @property
    def application_status(self):
        """The application's current status."""
        self._lookup_package_info()
        if self.application_name is None:
            return self.FAILURE
        return self.OK

    @classmethod
    def _lookup_package_info(cls):
        if cls._package_name is not None:
            try:
                pkg_info = pkg_resources.get_distribution(cls._package_name)
                cls._application_name = pkg_info.project_name
                cls._application_version = pkg_info.version
                cls._package_name = None
            except pkg_resources.ResolutionError:
                cls._application_name = None
                cls._application_version = None

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
        cls = self.__class__
        if 'package' in kwargs:
            cls._package_name = kwargs['package']
        else:
            cls._application_name = kwargs['name']
            cls._application_version = kwargs['version']

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
        if self.application_status == self.FAILURE:
            self.set_status(500)
        else:
            self.set_status(200)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({
            'name': self.application_name,
            'version': self.application_version,
            'status': self.application_status
        }).encode('utf-8'))
        self.finish()
