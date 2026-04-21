from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import models, schemas, crud, alerts
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Health Monitor")

# Static + Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ FIXED UI ROUTE (IMPORTANT CHANGE HERE)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# API Routes
@app.post("/records", response_model=schemas.HealthRecordResponse)
def create_record(record: schemas.HealthRecordCreate, db: Session = Depends(get_db)):
    return crud.create_record(db, record)

@app.get("/records")
def get_all_records(db: Session = Depends(get_db)):
    return crud.get_records(db)

@app.post("/alerts")
def get_alerts(record: schemas.HealthRecordCreate):
    return {"alerts": alerts.generate_alerts(record)}