from data import jobs

def recommend_jobs(user_skills):
    user_skills = [skill.lower() for skill in user_skills]

    recommendations = []

    for job in jobs:
        job_skills = [skill.lower() for skill in job["skills"]]

        matched = set(user_skills).intersection(set(job_skills))
        score = len(matched) / len(job_skills) if job_skills else 0

        if score > 0:
            recommendations.append({
                "job_title": job["title"],
                "match_score": round(score, 2),
                "matched_skills": list(matched)
            })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)

    return recommendations[:5]