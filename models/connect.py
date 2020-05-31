# 新建connect.py
from sqlalchemy import create_engine


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'instagram_t'
USERNAME = 'root'
PASSWORD = 'qwe123'

db_url='mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)

# 创建引擎
engine = create_engine(db_url)

# 创建基类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engine)

# 创建会话
from sqlalchemy.orm import sessionmaker

# 增删改查需要会话提交，实例化一个会话
Session = sessionmaker(engine)
session = Session()

# 验证
if __name__=='__main__':
    print(dir(Base))
    print(dir(session))