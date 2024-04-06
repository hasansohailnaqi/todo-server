from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine

from app import setting

# step1: Database table schema

class Todo(SQLModel, table=True):
   id: int | None = Field(default=None, primary_key=True)
   title: str = "Create Todo Api"

# connection to database
connection_string: str = str(setting.DATABASE_URL)

# engine = create_engine(setting.DATABASE_URL)   


# declear veriable type object

todo_server: FastAPI = FastAPI()




# create get route and create function in python

@todo_server.get("/")
def hello():
    return {"hello":"world"}

 
@todo_server.get("/db")
def db_var():
  return {"DB": setting.DATABASE_URL, "connection": connection_string} 











    




# table data save and get
# use sqlalcamy which is orm for sql postgresql for data validation
# let start

