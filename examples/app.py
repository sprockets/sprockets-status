from tornado import ioloop, web

import sprockets_status.handlers


name = 'my-application'
version = '1.2.3'


def make_app(**settings):
    return web.Application([
        web.url('/status', sprockets_status.handlers.StatusHandler,
                {'name': name, 'version': version}),
    ], **settings)


if __name__ == '__main__':
    app = make_app()
    iol = ioloop.IOLoop.current()
    try:
        app.listen(8888)
        iol.start()
    except KeyboardInterrupt:
        iol.stop()
