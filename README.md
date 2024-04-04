#todo-app
create folder desktop 
open power shell
poetry new todo-server --name app
cd todo server
open in vs code `code .`

```
install some packages
poetry add fastapi uvicorn
virtul enviroment `app-mmIRADZA-py3.12 in C:\Users\Msc3.0\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\Local\pypoetry\Cache\virtualenvs`
check toml file all necessery dependies install
`ctrl + shift + p tpye interpreter and past`
```

in app folder create `main.py`

```
main.py

from fastapi import FastAPI

# declear veriable type object
todo_server: FastAPI = FastAPI()

# create get route and create function in python
@todo_server.get("/")
def hello():
    return {"hello":"world"}

```
check route 
poetry run packge name `uvicorn` folder name `app.` file name `main` variable name `:todo_server --realod`

`poetry run uvicorn app.main:todo_server --reload` 


intigrate neon database

create .env file in root folder and past key 

```
create file in app folder setting.py

from starlette.config import Config
from starlette.datastructures import Secret

try:
  config = Config(".env")

except FileNotFoundError:
   config = Config()

DATABASE_URL = config("DATABASE_URL", cast = Secret)    

```
create file in root 
.gitignore
write .env 
for not pushing in githib




