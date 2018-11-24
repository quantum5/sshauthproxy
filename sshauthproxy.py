import os
from textwrap import dedent

from tornado import web, gen
from tornado.options import options
from tornado.process import Subprocess


class HomeHandler(web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'text/plain')
        self.finish(dedent('''\
            Usage: GET /<username>

            Response body is a list of SSH public key in authorized_keys format.

            Source: https://github.com/quantum5/sshauthproxy
        '''))


class SSHKeyHandler(web.RequestHandler):
    devnull = open(os.devnull, 'r+')

    @gen.coroutine
    def get(self, username):
        proc = Subprocess([options.command, username], stdin=self.devnull,
                          stdout=Subprocess.STREAM, stderr=self.devnull)
        output = yield proc.stdout.read_until_close()
        result = yield proc.wait_for_exit(raise_error=False)
        if result != 0:
            self.set_status(404)
        self.set_header('Content-Type', 'text/plain')
        self.finish(output)


def get_application():
    return web.Application([
        (r'/', HomeHandler),
        (r'/(.+)', SSHKeyHandler),
    ])


def main():
    import tornado
    from tornado.options import options, define

    define('port', default=8888, help='run on the given port', type=int)
    define('address', help='address to bind to')
    define('command', default='sss_ssh_authorizedkeys', help='command to get SSH keys with')

    tornado.options.parse_command_line()
    tornado.httpserver.HTTPServer(get_application()).listen(options.port, address=options.address)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
