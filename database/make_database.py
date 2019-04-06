#!/usr/bin/python3

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()

class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question = Column(String(500), nullable=False)
    verified = Column(String(1), nullable=False)
    user = Column(String(50), nullable=False)
    

class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    topic = Column(String(200), nullable=False)

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    answer = Column(String(500), nullable=False)
    topic = Column(String(200), nullable=False)

engine = create_engine('sqlite:///bot.db')

Base.metadata.create_all(engine)
    

