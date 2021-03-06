# 开启服务
# 使用命令行模式 manage.py
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from handlers.main import *
from handlers.users import *


# 监听端口
define("port", default="8888", help="Listening port", type=int)

# 视图
class Application(tornado.web.Application):  # 继承原本的类方法
    # 改写类方法
    def __init__(self):
        handlers = [
            (r"/",IndexHandler),
            (r"/explore",ExploreHandler),
            (r"/post/(?P<post_id>[0-9]+)",PostHandler),
            (r'/register',RegisterHandler),
            (r'/login',LoginHandler),

        ]
        settings = dict(
            debug=True,
            template_path="templates"
        )
        super().__init__(handlers,**settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()  # 开启命令行
    application = Application()  # 实例化
    application.listen(options.port)  # 开启端口
    tornado.ioloop.IOLoop.current().start()  # 开启tornado服务