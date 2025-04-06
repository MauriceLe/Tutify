from fastapi import *
from util import db


router = APIRouter()
__tablename__ = "Filiale"
__key__ = "ID_Filiale"
__columns__ = ["PLZ", "ID_BETREUER", "Name", "Offnungszeiten", "Strasse", "Hausnummer"]


@router.get("/")
def get_all():
    return db.select_all(__tablename__)


@router.get("/{id}")
def get_specific(id: int):
    return db.select_id(__tablename__, __key__, id)


@router.get("/betreuer/{id}")
def get_betreuer(id: int):
    return db.select_id("Betreuer", "ID_Betreuer", id)


@router.get("/Ort/{id}")
def get_ort(id: str):
    return db.select_id("Ort", "PLZ", id)