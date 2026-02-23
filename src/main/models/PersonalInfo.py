from pydantic import BaseModel

class PersonalInfo(BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str
    # TODO: Preferred name field could have all first/middle/last name options, and the API can determine which one to use based on the resume format. For now, we will just use a single preferred name field.
    preferred_name: str | None = None
    email: str
    phone: str
    address: str
    summary: str | None = None
    
    
    
