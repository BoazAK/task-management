from fastapi import FastAPI

from config.config import env_mode

# Créer l'application FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {
        "status": "OK",
        "message": f"API en mode {env_mode.capitalize()}"
    }
