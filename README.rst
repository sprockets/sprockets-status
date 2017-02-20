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
The simplest example is a JSON payload that contains directly configured
information.  The application name and version is passed through the
``URLSpec`` keyword arguments to the status handler.

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

Running this application and retrieving the ``/status`` resource returns
the following:

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Length: 62
   Etag: "e7bca140bba5af0fdb7b9e4fab6487186d7739d2"
   Content-Type: application/json
   Server: TornadoServer/4.4.2
   Date: Mon, 20 Feb 2017 12:54:47 GMT

   {"status": "ok", "version": "1.1.1", "name": "my-app-name"}

Python Packaged Application
===========================
If your application is a python package, then you can let the status
handler do the work of looking up your application's name and version
number from the python package metadata.

.. code-block:: python

   from tornado import ioloop, web
   import sprockets_status.handlers

   def make_app(**settings):
       return web.Application([
           web.url('/status', sprockets_status.handlers.StatusHandler,
                   {'package': 'my-app'}),
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

The status handler will use ``pkg_resources`` to look up the named
distribution and retrieve the package name and version for you.  If you
give it a package that doesn't exist, then it will return a server error
so don't do that.

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
