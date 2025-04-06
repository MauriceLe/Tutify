from pydantic import *


class Login(BaseModel):
    EMail: str
    Passwort: str

    class Config:
        orm_mode = True


class Register(BaseModel):
    EMail: str
    Passwort: str
    ID_Kunde: int

    class Config:
        orm_mode = True
