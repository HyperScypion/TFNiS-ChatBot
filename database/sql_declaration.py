#!/usr/bin/python3

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Char

Base = declarative_base()

class Question(Base):
    __tablename__ = 'question'

    question = Column(String(500), nullable=False)
    verified = Column(Char, nullable=False)
    user = Column(String(50), nullable=False)
    topic = Column(String(20), nullable=False)

class Topic(Base):
    

class Answer(Base):
    

