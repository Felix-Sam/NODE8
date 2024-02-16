from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# table for mulnurish user
class Malnurish_data(Base):
    __tablename__ = 'malnurish'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    mid_lower_hand_circumference = Column(Integer)
    skin_type = Column(String)
    hair_type = Column(String)
    eyes_type = Column(String)
    date_created = Column(DateTime, default=datetime.now)
    oedema = Column(String)
    angular_stomatitis = Column(String)
    cheilosis = Column(String)
    bowlegs = Column(String)
    location = Column(String)
    face_image = Column(String)
    hair_image = Column(String)
    hands_image = Column(String)
    leg_image = Column(String)

# table for nurish data
class Nurish_data(Base):
    __tablename__ = 'nurish'
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    mid_lower_hand_circumference = Column(Integer)
    skin_type = Column(String)
    hair_type = Column(String)
    eyes_type = Column(String)
    date_created = Column(DateTime, default=datetime.now)
    oedema = Column(String)
    angular_stomatitis = Column(String)
    cheilosis = Column(String)
    bowlegs = Column(String)
    location = Column(String)
    face_image = Column(String)
    hair_image = Column(String)
    hands_image = Column(String)
    leg_image = Column(String)