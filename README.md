# 🧠 Smart Health Monitor

A **FastAPI-based Smart Health Monitoring System** that records patient health metrics and water quality data, stores them in a database, and generates real-time alerts based on abnormal conditions.

---

## 🚀 Features

- 📊 Record patient health data:
  - Temperature
  - Heart Rate
  - Blood Pressure

- 💧 Monitor water quality:
  - pH level
  - TDS (Total Dissolved Solids)
  - Turbidity
  - Contamination status

- 🚨 Intelligent alert system:
  - Detects abnormal health conditions
  - Identifies unsafe water quality

- 🗄️ Database integration using SQLite
- ⚡ FastAPI backend with automatic API docs
- 🌐 Simple UI using HTML, CSS, JavaScript

---

## 🏗️ Project Structure

smart_health_monitor/ │ ├── app/ │   ├── init.py │   ├── main.py │   ├── database.py │   ├── models.py │   ├── schemas.py │   ├── crud.py │   └── alerts.py │ ├── static/ │   ├── style.css │   └── script.js │ ├── templates/ │   └── index.html │ ├── requirements.txt └── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone <your-repo-link>
cd smart_health_monitor

### 2. Create virtual environment

python -m venv .venv

### 3. Activate virtual environment

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt


---

## ▶️ Run the Application

uvicorn app.main:app --reload


---

## 🌐 Access the Application

UI: http://127.0.0.1:8000/

API Docs (Swagger): http://127.0.0.1:8000/docs



---

## 🧪 API Endpoints

### Create Health Record

- POST /records

- Get All Records

- GET /records

### Generate Alerts

- POST /alerts


---

## 📌 Example Input

{
  "patient_name": "Nouman",
  "age": 21,
  "temperature": 101,
  "heart_rate": 110,
  "blood_pressure": "140/95",
  "water_ph": 9,
  "water_tds": 200,
  "water_turbidity": 2,
  "contamination": true
}


---

## 🚨 Example Alerts

- High Temperature

- Abnormal Heart Rate

- High Blood Pressure

- Unsafe Water pH

- High TDS

- High Turbidity

- Water Contamination Detected


---

## 🛠️ Tech Stack

- Backend: FastAPI

- Database: SQLite + SQLAlchemy

- Frontend: HTML, CSS, JavaScript

-Server: Uvicorn


---

## 📈 Future Enhancements

- Authentication (JWT)

- Dashboard with charts

- IoT device integration

- Cloud deployment (AWS / Render)

- Mobile app integration



---

## 👨‍💻 Author

- Mohammed Nouman

- GitHub: https://github.com/mohammednouman555

- LinkedIn: https://www.linkedin.com/in/mohammed-nouman-2a8989343


---

## 📄 License

- This project is open-source and available for learning and development purposes.

---

## ⭐ Contribution

- Contributions, issues, and feature requests are welcome!

---

## 🏁 Summary

- Smart Health Monitor combines health monitoring + water quality analysis + alert generation, making it a strong foundation for real-world healthcare and IoT-based applications.

---
