from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy_utils import database_exists, create_database
import json

Base = declarative_base()

class Event(Base):
    __tablename__ = 'timings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    startnumber = Column(Integer)
    license_plate = Column(String)
    start_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)
    distance = Column(Integer)
    speed = Column(Integer)
    session_name = Column(String)
    

DATABASE_URL = "postgresql://pi:HNoorito66!!@localhost/OTT"

engine = create_engine(DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)
Session = sessionmaker(bind=engine)

def create_tables():

    Base.metadata.create_all(engine)

def delete_tables():
    Base.metadata.drop_all(engine)   # all tables are deleted

def add_event(name, license_plate, start_timestamp, end_timestamp, distance, speed, session_name):
    session = Session()
    event = Event(startnumber=name, license_plate=license_plate, start_timestamp=start_timestamp, end_timestamp=end_timestamp, distance=distance, speed=speed, session_name=session_name)
    session.add(event)
    session.commit()
    session.close()

def get_all_events():
    session = Session()
    try:
        events = session.query(Event).all()
        return events
    finally:
        session.close()

def event_to_dict(event):
    return {
        "id": event.id,
        "startnumber": event.startnumber,
        "license_plate": event.license_plate,
        "start_timestamp": event.start_timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "end_timestamp": event.end_timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "distance": event.distance,
        "speed": event.speed,
        "session_name": event.session_name
    }

def events_to_json(events):
    events_list = [event_to_dict(event) for event in events]
    return json.dumps(events_list)
