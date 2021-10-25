from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
from datetime import datetime

from envs import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
db = SQLAlchemy()


class Employees(db.Model):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    rfc = Column(String(13), nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    birthday = Column(DateTime)
    job_position = Column(String(100))
    pronouns = Column(String(4))

