from fastapi import FastAPI
import uuid

app = FastAPI()

tasks = {}


@app.get("/")
def home():
    return {'hello':"world"}

@app.get("/tasks")
def all_tasks():
    return tasks

@app.get("/tasks/{uid}")
def display_one_task(uid: str):
    if uid not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[uid]

@app.post("/tasks/{name}/{age}")
def create_task(name: str,age: int):
    uidu = str(uuid.uuid4())
    nameu = name
    ageu = age
    
    tasks[uidu] = {
        "name": nameu,
        "age": ageu
    }

    return {
        "message" : "user created successfully",
        "name of user" : nameu,
        "age of user" : ageu
    }
