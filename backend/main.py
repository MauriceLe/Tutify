from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import customer, course, account, branch


app = FastAPI()


origins = [
    "http://localhost:8080"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    customer.router,
    prefix="/kunde",
    tags=["Kunden-Router"]
)


app.include_router(
    course.router,
    prefix="/kurs",
    tags=["Kurs-Router"]
)


app.include_router(
    account.router,
    prefix="/account",
    tags=["Account-Router"]
)


app.include_router(
    branch.router,
    prefix="/filiale",
    tags=["Filiale-Router"]
)
