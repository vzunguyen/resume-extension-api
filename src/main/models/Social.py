from pydantic import BaseModel

class Social(BaseModel):
    linkedin: str | None = None
    github: str | None = None
    twitter: str | None = None
    facebook: str | None = None
    instagram: str | None = None
    website: str | None = None