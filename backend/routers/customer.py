from fastapi import *
from schemas.customer import *
from util import db


router = APIRouter()
__tablename__ = "Kunde"
__key__ = "ID_KUNDE"
__columns__ = ["Nachname", "Vorname", "E_Mail", "Telefon", "Geburtstag", "PLZ", "Strasse", "Hausnummer"]


@router.get("/")
def get_all():
    return db.select_all(__tablename__)


@router.get("/{id}")
def get_specific(id: int):
    return db.select_id(__tablename__, __key__, id)


@router.post("/")
def add_user(request: RequestKunde):
    db.insert(__tablename__, "PLZ, Nachname, Vorname, E_Mail, Telefon, Geburtstag, Strasse, Hausnummer", \
              "'" + str(request.PLZ) + "','" + str(request.Nachname) + "','" + str(request.Vorname) + "','" + \
              str(request.E_Mail) + "','" + str(request.Telefon) + "','" + str(request.Geburtstag) + "','" + str(request.Strasse) + "','" + \
              str(request.Hausnummer) + "'")
    return db.custom_statement("SELECT * FROM Kunde WHERE E_Mail LIKE '" + request.E_Mail + "'")


@router.delete("/delete/{id}")
def delete(id: int):
    db.delete(__tablename__,id,__key__)


@router.get("/Ort/{id}")
def get_ort(id: str):
    return db.select_id("Ort", "PLZ", id)
