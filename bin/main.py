from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# GET request - get or return 
@app.get("/")
def read_root():
    return {"Message" : "Hello Arpita"}

@app.get("/greet")
def greet():
    return {"Message": "Hello Vivek"}

@app.get("/greet/")
def greet_name(name: str, age: Optional[int] = None):
    return {"Message": f"Hello {name} and you are {age} years old." }



#  Pydantic class for data validation used in PUT and POST
class Student(BaseModel):
    name: str
    age: int
    roll: int

#  POST request - sending data (since we are sending data, it should be validated correctly)
@app.post("/create_student")
def create_student(student: Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "roll" : student.roll
    }

