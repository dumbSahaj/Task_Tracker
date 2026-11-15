from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.get("/")
def home():
    return {'hello':"world"}

@app.get("/tasks")
def all_tasks():
    return tasks

@app.get("/tasks/{uid}")
def display_one_task():
    return {"it shall display a particular task"}

@app.post("/tasks/{name}/{age}")
def create_task(name: str,age: int):
    nameu = name
    ageu = age
    
    tasks.append([nameu,ageu])

    return {
        "message" : "user created successfully",
        "name of user" : nameu,
        "age of user" : ageu
    }
