from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def servidor_online():
    return "Servidor Online."