from pydantic import BaseModel
from typing import Optional

class HealthRecordCreate(BaseModel):
    patient_name: str
    age: int

    temperature: float
    heart_rate: Optional[int] = None
    blood_pressure: str

    water_ph: float
    water_tds: float
    water_turbidity: float
    contamination: bool

class HealthRecordResponse(HealthRecordCreate):
    id: int

    class Config:
        from_attributes = True   # ✅ FIXED (Pydantic v2)