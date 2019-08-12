from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id = Column(String(100),primary_key=True)
    username = Column(String(255))
    password = Column(String(255))

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/pythontestdb")
DBSession = sessionmaker(bind = engine)
sessio = DBSession()
# # 增加数据
# user1 = User(id='3',username = 'zhangyujie',password = '123321')
# sessio.add(user1)
# sessio.commit()
# sessio.close()

# 查询数据
user = sessio.query(User).filter(User.username == 'zhangyujie').one()
print(user.username)
sessio.close()
