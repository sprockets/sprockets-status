================
sprockets-status
================
Simple application status handler for Tornado.

+-------------+--------------------------------------------------------+
| |GitHub|    | https://github.com/sprockets/sprockets-status          |
+-------------+--------------------------------------------------------+
| |PyPI|      | https://pypi.org/project/sprockets-status/             |
+-------------+--------------------------------------------------------+
| |Docs|      | https://pythonhosted.org/sprockets-status/             |
+-------------+--------------------------------------------------------+
| |Coveralls| | https://coveralls.io/github/sprockets/sprockets-status |
+-------------+--------------------------------------------------------+
| |Travis|    | https://travis-ci.org/sprockets/sprockets-status       |
+-------------+--------------------------------------------------------+

This library includes a very simple ``tornado.web.RequestHandler`` that
returns an applications status information.  You should install the
handler under the ``/status`` path for a very simple healthcheck that
verifies the operation of the IOLoop (at the very least).  This library
is the successor to the `sprockets.handlers.status`_ library.  We have
moved away from a deeply nested package structure based on namespace
packages because they are actually more trouble than they are worth.

Simplest Example
================
.. code-block:: python

   from tornado import ioloop, web
   import sprockets_status.handlers

   def make_app(**settings):
       return web.Application([
           web.url('/status', sprockets_status.handlers.StatusHandler,
                   {'name': 'my-app-name', 'version': '1.1.1'}),
           # add your handlers here
       ], **settings)

   if __name__ == '__main__':
       app = make_app()
       iol = ioloop.IOLoop.current()
       try:
           app.listen(8888)
           iol.start()
       except KeyboardInterrupt:
           iol.stop()

Developer Quickstart
====================
.. code-block:: bash

   python3.5 -mvenv --copies env
   env/bin/pip install -r requires/development.txt -e .
   env/bin/nosetests
   env/bin/python setup.py build_sphinx

.. _sprockets.handlers.status: https://github.com/sprockets/
   sprockets.handlers.status
.. |Coveralls| image:: https://img.shields.io/coveralls/sprockets/sprockets-status.svg
   :target: https://coveralls.io/github/sprockets/sprockets-status
.. |GitHub| image:: https://img.shields.io/github/release/sprockets/sprockets-status.svg
   :target: https://github.com/sprockets/sprockets-status
.. |PyPI| image:: https://img.shields.io/pypi/v/sprockets-status.svg
   :target: https://pypi.org/project/sprockets-status
.. |Docs| image:: https://img.shields.io/badge/docs-pythonhosted-green.svg
   :target: https://pythonhosted.com/sprockets-status/
.. |Travis| image:: https://img.shields.io/travis/sprockets/sprockets-status.svg
   :target: https://travis-ci.org/sprockets/sprockets-status
