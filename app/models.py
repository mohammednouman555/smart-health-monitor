from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    age = Column(Integer)

    temperature = Column(Float)
    heart_rate = Column(Integer, nullable=True)
    blood_pressure = Column(String)

    water_ph = Column(Float)
    water_tds = Column(Float)
    water_turbidity = Column(Float)
    contamination = Column(Boolean)