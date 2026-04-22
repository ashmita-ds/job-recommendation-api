# 🚀 Job Recommendation API

A simple FastAPI-based job recommendation system that suggests relevant job roles based on a user's skill set.

This project demonstrates backend development, API design, and basic recommendation logic using Python.

## Live Demo
https://job-recommendation-api-nm2x.onrender.com/docs

---

## 📌 Features

- Recommend jobs based on user skills  
- Match scoring using skill overlap  
- FastAPI backend with REST endpoints  
- Clean and modular code structure  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- Pydantic  
- Uvicorn  

---

## 📂 Project Structure

```
job-recommendation-api/

├── main.py            # FastAPI app entry point
├── models.py          # Request/response models
├── recommender.py     # Recommendation logic
├── data.py            # Sample job dataset
├── requirements.txt   # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ashmita-ds/job-recommendation-api.git
cd job-recommendation-api
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the API

```bash
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

### 🔹 Home
```bash
GET /
```

Returns API status.

---

### 🔹 Get All Jobs
```bash
GET /jobs
```

---

### 🔹 Recommend Jobs
```bash
POST /recommend
```

#### Request Body:
```json
{
  "skills": ["python", "sql"]
}
```

#### Response:
```json
{
  "recommendations": [
    {
      "job_title": "Backend Engineer",
      "match_score": 0.5,
      "matched_skills": ["python", "sql"]
    }
  ]
}
```

---

## 🧠 How It Works

The system compares user skills with job requirements and calculates a match score:

- Uses set intersection to find common skills  
- Score = matched skills / total job skills  
- Results are sorted by relevance  

---

## 🚧 Future Improvements

- Add ML-based recommendation system  
- Integrate real job datasets (LinkedIn, Indeed APIs)  
- Add authentication  
- Deploy using Docker or cloud  


## ⭐ If you found this useful, consider giving it a star!
