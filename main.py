from fastapi import FastAPI
from models import UserProfile
from recommender import recommend_jobs
from data import jobs
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Job Recommendation API is running"}

@app.post("/recommend")
def recommend(user: UserProfile):
    results = recommend_jobs(user.skills)
    return {"recommendations": results}
@app.get("/jobs")
def get_jobs():
    return {"available_jobs": jobs}
@app.post("/add-job")
def add_job(job: dict):
    jobs.append(job)
    return {"message": "Job added successfully"}