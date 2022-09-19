from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()
engine = create_engine('sqlite:///devdb.db', echo=True)
Session = sessionmaker(bind=engine)


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    reporter_id = Column(String)
    reason = Column(String)

    def __repr__(self):
        return "<Report(name='%s', description='%s')>" % (self.name, self.description)

    def __init__(self, user_id: str, reporter_id: str, reason: str) -> None:
        self.user_id = user_id
        self.reason = reason
        self.reporter_id = reporter_id


class Warn(Base):
    __tablename__ = 'warns'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    mod_id = Column(String)
    reason = Column(String)

    def __repr__(self):
        return "<Warn(name='%s', description='%s')>" % (self.name, self.description)

    def __init__(self, user_id: str, mod_id: str, reason: str) -> None:
        self.user_id = user_id
        self.mod_id = mod_id
        self.reason = reason


class Verify(Base):
    __tablename__ = 'verified'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    mod_id = Column(String)

    def __init__(self, user_id: str, mod_id: str):
        self.user_id = user_id
        self.mod_id = mod_id


Base.metadata.create_all(engine)
