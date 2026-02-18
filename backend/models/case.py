from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Assuming you have a database.py where Base is defined

class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # Assuming there is a User model

    user = relationship('User', back_populates='cases')  # Assuming a relationship with User model
