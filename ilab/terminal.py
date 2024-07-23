import os.path
import tornado.web
import tornado.ioloop

# This demo requires tornado_xstatic and XStatic-term.js
import tornado_xstatic

import terminado

STATIC_DIR = os.path.join(os.path.dirname(terminado.__file__), "_static")

PORT = os.getenv("XTERM_PORT", 8501)


class TerminalPageHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render(
            "/app/termpage.html",
            static=self.static_url,
            xstatic=self.application.settings["xstatic_url"],
            ws_url_path="/websocket",
        )


if __name__ == "__main__":
    term_manager = terminado.SingleTermManager(shell_command=["bash"])
    handlers = [
        (r"/websocket", terminado.TermSocket, {"term_manager": term_manager}),
        (r"/", TerminalPageHandler),
        (
            r"/xstatic/(.*)",
            tornado_xstatic.XStaticFileHandler,
            {"allowed_modules": ["termjs"]},
        ),
    ]
    app = tornado.web.Application(
        handlers,
        static_path=STATIC_DIR,
        xstatic_url=tornado_xstatic.url_maker("/xstatic/"),
    )
    app.listen(PORT)
    try:
        print(f"Terminal URL: http://localhost:{PORT}")
        tornado.ioloop.IOLoop.instance().start()
    finally:
        term_manager.shutdown()
