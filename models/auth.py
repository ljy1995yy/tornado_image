from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey ,Table
from sqlalchemy.orm import relationship

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 项目路径添加到搜索路径中
from models.connect import Base,session


# 基类
class Bassmodels:
    create_time = Column(DateTime,default=datetime.now)  # 创建时间
    update_time = Column(DateTime,default=datetime.now)  # 修改时间
    is_delete = Column(Boolean, default=False)  # 逻辑删除

class User(Base,Bassmodels):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(30),nullable=False,unique=True)
    password = Column(String(200),nullable=False)
    activation = Column(Boolean,default=False)  # 激活
    email = Column(String(100))
    phone = Column(String(30))

    # 校验（模型中查询）
    @classmethod
    def check_username(cls,username):  # cls代表类本身
        return session.query(cls).filter_by(username=username).first()

    # 入库
    @classmethod
    def add_user(cls,username,password,**kwargs):
        user = User(username=username,password=password,**kwargs)
        session.add(user)
        session.commit()



    def __repr__(self):
        return "<User:{}>".format(self.username)






class Post(Base,Bassmodels):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(300))
    user_id = Column(Integer, ForeignKey("users.id"))  # 表名.属性
    user = relationship("User",backref="posts",uselist=False,cascade="all")

    def __repr__(self):
        return "Post:{}".format(self.user_id)

# 双向关系backref
# 图片实例.user ====>对应的User实例
# 用户实例.posts=====>对应的Post实例

    @classmethod
    def app_post(cls,img_url,username):
        user = User.check_username(username)
        post = Post(image_url=img_url,user_id=user.id)
        session.add(post)
        session.commit()
