from fastapi import *
from schemas.course import *
from typing import Optional
from typing import List
from util import db


router = APIRouter()
__tablename__ = "Kurs"
__key__ = "ID_Kurs"
__columns__ = ["ID_Fachbereich", "Name", "Datum", "Preis", "Klasse", "Verfugbarkeit"]


@router.get("/")
def get_all():
    return db.select_all(__tablename__)


@router.get("/{id}")
def get_specific(id: int):
    return db.select_id(__tablename__, __key__, id)


@router.post("/")
def add_kurs(request: RequestKurs):
    db.insert(__tablename__, "ID_Fachbereich, Name, Datum, Preis, Klasse, Verfugbarkeit", \
              "" + str(request.ID_FACHBEREICH) + ",'" + str(request.NAME) + "','" + str(request.DATUM) + "'," + \
              str(request.PREIS) + "," + str(request.KLASSE) + ",'" + str(request.VERFUGBARKEIT) + "'")


@router.post("/subscribe/{id}")
def subscribe_kurs(id: int, userid: int):
    db.insert("KUNDE_KURS", "ID_KUNDE, ID_KURS", str(userid) + "," + str(id))


@router.get("/subscribed/{userid}")
def get_user_kurs(userid: int):
    return db.custom_statement("select * from Kurs where ID_KURS in (select id_kurs from kunde_kurs where id_kunde = " + str(userid) + ")")


@router.post("/billing")
def create_bill(courseids: List[int], billing_date: str, userid: str = Header(None)):
    db.insert("Rechnung", "ID_Kunde, Erstellungsdatum", str(userid) + ",'" + str(billing_date) + "'")
    bill_id = db.custom_statement("SELECT ID_Rechnung FROM Rechnung WHERE ID_Kunde = " + str(userid) + " AND Erstellungsdatum = '" + str(billing_date) + "' ORDER BY ID_Rechnung DESC")[0][0]
    for id in courseids:
        db.insert("Kurs_Rechnung","ID_KURS, ID_Rechnung", "'" + str(id) + "', '" + str(bill_id) + "'")


@router.get("/billing/")
def get_bills(userid: int = Header(None)):
    return db.custom_statement("SELECT * FROM Rechnung WHERE ID_KUNDE = " + str(userid))


@router.get("/billing/{id}")
def get_specific_bill(id: int):
    return db.select_id("Rechnung", "ID_Rechnung", str(id))