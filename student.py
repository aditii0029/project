from fastapi import FastAPI
from fastapi import json
from datetime import date 

app = FastAPI()


@app.get('/home/')
def home():
    return {"Message": "Welcome to Student API"}


@app.post('/students/')
def students():
    return {"Message": "The Updated Endpoint"}


@app.create('/data{id}')
def create():
    return {"Message": "Creating new records"}


def calculate():
        average = 85+90/2
        print(average)
        return {"Message": "This is the Average Marks of Both the Students"}
    
    
@app.delete('/students{id}')
def delete():
    return {"Message": "Deletion of ID"}

