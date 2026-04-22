from data import jobs

def recommend_jobs(user_skills):
    """
    Recommend jobs based on skill overlap.
    Returns top 5 ranked jobs.
    """

    user_skills = [skill.lower() for skill in user_skills]
    recommendations = []

    for job in jobs:
        job_skills = [skill.lower() for skill in job["skills"]]

        if not job_skills:
            continue

        matched = set(user_skills).intersection(set(job_skills))
        score = len(matched) / len(job_skills)

        recommendations.append({
            "job_title": job["title"],
            "match_score": round(score, 2),
            "matched_skills": list(matched)
        })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)

    return recommendations[:5]