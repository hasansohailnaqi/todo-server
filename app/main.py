from fastapi import FastAPI


# declear veriable type object

todo_server: FastAPI = FastAPI()

# create get route and create function in python

@todo_server.get("/")
def hello():
    return {"hello":"world"}
