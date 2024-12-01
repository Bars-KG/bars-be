from pydantic import BaseModel

class BaseDataClass(BaseModel):
    class Config:
        arbitrary_types_allowed = True