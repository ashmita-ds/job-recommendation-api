from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    skills: List[str]

class Job(BaseModel):
    id: int
    title: str
    skills: List[str]