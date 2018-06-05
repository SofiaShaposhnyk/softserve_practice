from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String

Base = declarative_base()


class Contracts(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, autoincrement=True, primary_key=True)
    product = Column('product', String, unique=True, nullable=False)
    start_date = Column('start_date', String, nullable=False)
    end_date = Column('end_date', String, nullable=False)
    discount = Column('discount', Float, nullable=False)
