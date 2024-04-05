from fastapi import FastAPI
from sqlmodel import SQLModel, Field

from app import setting


# declear veriable type object

todo_server: FastAPI = FastAPI()




# create get route and create function in python

@todo_server.get("/")
def hello():
    return {"hello":"world"}


@todo_server.get("/db")
def db_var():
    return {"DB": setting.DATABASE_URL}


# connection to database
# step1 table schema

class todo(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    




# table data save and get
# use sqlalcamy which is orm for sql postgresql for data validation
# let start

