import json

from tornado import web


class StatusHandler(web.RequestHandler):
    """
    Simple handler that returns application status information.
    """

    def __init__(self, *args, **kwargs):
        self.name = 'UNKNOWN'
        self.version = '0.0.0'
        self.status = 'ok'
        super(StatusHandler, self).__init__(*args, **kwargs)

    def initialize(self, name, version):
        """
        Sets the static information.

        :param str name: name of the application
        :param str version: application version number

        """
        self.name = name
        self.version = version

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
