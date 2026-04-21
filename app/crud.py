from sqlalchemy.orm import Session
from . import models, schemas

def create_record(db: Session, record: schemas.HealthRecordCreate):
    db_record = models.HealthRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session):
    return db.query(models.HealthRecord).all()