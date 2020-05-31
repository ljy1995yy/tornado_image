import tornado.web
from models.auth import *


class RegisterHandler(tornado.web.RequestHandler):
    """
    注册
    """
    def get(self):
        return self.render("register.html")

    def post(self):
        # 获取前端参数
        username = self.get_argument("username","").strip()
        password = self.get_argument("password","").strip()
        repeat_password = self.get_argument("repeat_password","").strip()
        # 校验参数
         # 是否为空
        if not all([username,password,repeat_password]):
            return self.write("参数错误")
         # 是否符合规定
        if not (len(username) >= 6 and len(password) >= 6 and password == repeat_password):
            return self.write("格式错误")
         # 数据库用户名唯一
        if User.check_username(username):
            return self.write("用户名已存在")

        # 加密

        # 入库
        User.add_user(username,password)  #存入数据
        # 返回数据
        return self.redirect("/login")

class LoginHandler(tornado.web.RequestHandler):
    """
    登录
    """
    def get(self):
        return self.render("login.html")

    def post(self):
        pass