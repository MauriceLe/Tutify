from fastapi import *
from schemas.account import *
from util import db


router = APIRouter()
__tablename__ = "Account"
__key__ = "ID_Account"
__columns__ = ["ID_Mitarbeiter", "ID_Kunde", "Passwort", "EMail"]


@router.post("/login")
def login(request: Login):
    return db.custom_statement("SELECT * FROM Account WHERE EMail LIKE '" + request.EMail + "' AND Passwort LIKE '" + request.Passwort + "'")


@router.post("/register")
def register(request: Register):
    if not db.select_id(__tablename__, "EMail", request.EMail):
        db.insert(__tablename__, "ID_Mitarbeiter, ID_Kunde, Passwort, EMail", "NULL, " + str(request.ID_Kunde) + ", '" + str(request.Passwort) + "', '" + str(request.EMail) + "'")
    else:
        raise HTTPException(status_code=422)