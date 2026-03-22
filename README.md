# 🚀 AI Interview Backend – Database Integration & Data Pipeline


Overview

This module implements the **Database Integration & Data Pipeline** for the AI-based Interview System.

It connects the backend with the database and provides APIs to:

* Store candidate answers
* Store evaluation results
* Store final performance summaries
* Provide data for frontend and reporting modules

---

 Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL (primary)
* SQLite (fallback for local testing)

---

 Project Structure

```
interview-backend/
│
├── main.py          # Entry point
├── db.py            # Database configuration
├── models.py        # Database schema
├── routes.py        # API routes
├── requirements.txt # Dependencies
├── README.md        # Documentation
```

---

 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd interview-backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Environment

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configure Database

Edit `db.py` and update your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/interview_system"
```

> ⚠️ Make sure PostgreSQL is running and database `interview_system` exists.

---

### 6️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Database Schema

Defined in `models.py`

### Tables:

* `candidates`
* `questions`
* `answers`
* `results`
* `summary`

---

## 🔗 API Endpoints

### 🔹 1. Submit Answer

**POST** `/submit-answer/`

```json
{
  "candidate_id": 1,
  "question_id": 1,
  "answer": "Sample answer",
  "score": 8
}
```

---

### 🔹 2. Get Answers

**GET** `/answers/`

---

### 🔹 3. Store Result

**POST** `/store-result/`

```json
{
  "candidate_id": 1,
  "total_score": 85,
  "feedback": "Good performance"
}
```

---

### 🔹 4. Store Summary

**POST** `/store-summary/`

```json
{
  "candidate_id": 1,
  "summary": "Candidate performed well",
  "recommendation": "Selected"
}
```

---

## 🔄 Data Flow

```
Frontend / Voice Input
        ↓
FastAPI Backend
        ↓
PostgreSQL Database
        ↓
Reporting & Analytics
```

---
Integration Guide

Frontend (Assessment UI)

* Use `/submit-answer/` to store answers

---

 Result Review Module

* Use `/answers/` to fetch answers

---

###Voice Input System

* Send transcribed text to `/submit-answer/`

---

### Summary Generator

* Send data to `/store-summary/`

---

### Admin Reporting

* Fetch data from:

  * answers
  * results
  * summary

---

##  Important Notes

* Use consistent fields:

  * `candidate_id` (int)
  * `question_id` (int)
  * `answer` (string)
  * `score` (float)

* Do not modify table names

---

##  Switching to SQLite (Optional)

For local testing:

```python
DATABASE_URL = "sqlite:///./interview.db"
```

---

##  Features Implemented

* ✔ PostgreSQL database integration
* ✔ Answer storage pipeline
* ✔ Result storage system
* ✔ Summary storage system
* ✔ API endpoints for full data flow
* ✔ Ready for frontend & reporting integration

---

## Status

** Module Complete and Ready for Integration**

---

##  Author

**Yash Satyawan Pawar**
Database Integration & Data Pipeline



