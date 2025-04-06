from pydantic import *


class RequestKunde(BaseModel):
    PLZ: str
    Nachname: str
    Vorname: str
    E_Mail: str
    Telefon: str
    Geburtstag: str
    Strasse: str
    Hausnummer: str

    class Config:
        orm_mode = True
