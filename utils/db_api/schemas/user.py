from sqlalchemy import sql, Column, Integer, BigInteger, String

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    referral = Column(Integer)
    query: sql.Select
