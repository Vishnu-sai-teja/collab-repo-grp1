from pydantic import BaseModel
from typing import Optional, List

class MentorRecommendationRequest(BaseModel):
    skillset: Optional[str] = None       # e.g. "Python"
    organisation: Optional[str] = None   # e.g. "MNC"
    exp_type: Optional[str] = None       # e.g. "service"
    min_experience: Optional[int] = None # e.g. 5 years
    sex: Optional[str] = None            # "m" or "f"
    age: Optional[int] = None            # e.g. 25 years
    experience: Optional[int] = None     # e.g. 5 years


class Mentor(BaseModel):
    id: int
    name: str
    age: int
    experience: int
    skillset: str
    organisation: str
    exp_type: str
    sex: str

class MentorsResponse(BaseModel):
    mentors: List[Mentor]