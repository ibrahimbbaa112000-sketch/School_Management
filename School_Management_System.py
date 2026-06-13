from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Student(BaseModel):
    id:int
    name:str
    grade:float

Students = [Student(id=1,name="Ibrahim BK",grade=85.6),Student(id=2,name="Raad KH",grade=93.9)]

@app.get("/Students/")
async def get_students():
    return Students

@app.post("/Students/")
async def update_student(new_student:Student):
    Students.append(new_student)
    return new_student

@app.put("/Students/{student_id}")
async def update_student(student_id:int,new_student:Student):
    for index,student in enumerate(Students):
        if student.id == student_id:
            Students[index] = new_student
            return new_student
    return {"Error":"Student not found"}

@app.delete("/Students/{student_id}")
async def delete_student(student_id:int):
    for index,student in enumerate(Students):
        if student.id == student_id:
            del Students[index]
            return {"message":"deleted"}
    return {"Error":"Student not found"}


