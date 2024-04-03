from fastapi import FastAPI

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
