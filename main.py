from fastapi import FastAPI, HTTPException
from models import UserProfile, Job
from recommender import recommend_jobs
from data import jobs

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Job Recommendation API is running"}


@app.post("/recommend")
def recommend(user: UserProfile):
    if not user.skills:
        raise HTTPException(status_code=400, detail="Skills list cannot be empty")

    results = recommend_jobs(user.skills)
    return {"recommendations": results}


@app.get("/jobs")
def get_jobs():
    return {"available_jobs": jobs}


@app.post("/add-job")
def add_job(job: Job):
    # Check duplicate ID
    for existing_job in jobs:
        if existing_job["id"] == job.id:
            raise HTTPException(status_code=400, detail="Job ID already exists")

    jobs.append(job.dict())
    return {"message": "Job added successfully"}
@app.get("/search")
def search_jobs(skill: str):
    results = []

    for job in jobs:
        if skill.lower() in [s.lower() for s in job["skills"]]:
            results.append(job)

    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)