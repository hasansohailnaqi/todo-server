from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session
from contextlib import asynccontextmanager

from app import setting

# step1: Database table schema

class Todo(SQLModel, table=True):
   id: int | None = Field(default=None, primary_key=True)
   title: str = "Create Todo Api"

# connection to database
conn_str: str = str(setting.DATABASE_URL). replace(
   "postgresql", "postgresql+psycopg" 
)

engine = create_engine(conn_str)   

def create_db_tables():
    print ("create_tb_tables")
    SQLModel.metadata.create_all(engine)
    print("done")

@asynccontextmanager

async def lifespan(todo_server:FastAPI):
   print("Server Startup")
   create_db_tables
   yield



# declear veriable type object

todo_server: FastAPI = FastAPI(lifespan = lifespan)




# create get route and create function in python

@todo_server.get("/")
def hello():
    create_db_tables()
    return {"hello":"world"}

 
@todo_server.get("/db")
def db_var():
  return {"DB": setting.DATABASE_URL, "connection": conn_str} 




@todo_server.post("/todo")
def create_todo(todo_data:Todo):
   with Session(engine) as session:
       session.add(todo_data)
       session.commit()
       session.refresh(todo_data)
       return todo_data







    




# table data save and get
# use sqlalcamy which is orm for sql postgresql for data validation
# let start

