from pydantic import *
from typing import Optional
from datetime import date


class RequestKurs(BaseModel):
    ID_FACHBEREICH: Optional[int]
    NAME: Optional[str]
    DATUM: Optional[str]
    PREIS: Optional[float]
    KLASSE: Optional[int]
    VERFUGBARKEIT: Optional[str]

    class Config:
        orm_mode = True