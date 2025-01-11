import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, relationship


Base = declarative_base()


class AsInfo(Base):
    __tablename__ = 'as_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.datetime.now())
    jobid = Column(String(128))
    name = Column(String(128))
    provider = Column(Text)
    networks = relationship('Network', back_populates='as_info')


class Network(Base):
    __tablename__ = 'network'
    id = Column(Integer, primary_key=True, autoincrement=True)
    network = Column(String(128))
    provider = Column(Text)
    country = Column(Text)
    ip_version = Column(Integer)
    as_info_id = mapped_column(ForeignKey('as_info.id'))
    as_info = relationship('AsInfo', back_populates='networks')
