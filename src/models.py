import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name =  Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(Integer)
    birth_date = Column(Integer)
    password = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key= True)
    user_id =  Column(Integer, ForeignKey('user.id'))
    user = relationship("User")


class Following(Base):
    __tablename__ = 'following'

    id = Column(Integer, primary_key= True)
    user_id =  Column(Integer, ForeignKey('user.id'))
    user = relationship("User")




class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comments_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship("Comments")


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post") 



    def to_dict(self):
        return {}








## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
