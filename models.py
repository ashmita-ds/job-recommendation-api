from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    skills: List[str]