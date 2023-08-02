# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from fastapi import FastAPI
from v1.api import app as v1_app


app = FastAPI(
    title="MicroServicio de reconocimiento facial",
    description="API para el MicroServicio de reconocimiento facial",
    version="1.0.0"
)


@app.get("/api")
async def root():
    return {
        "message": "Bienvenido a la API de reconocimiento facial",
        "version": "1.0.0",
        "author": "Jorge Gustavo Banegas Melgar",
        "email": "jorge.g.banegas@gmail.com",
        "github": "https://github.com/JorgeGBanegas",
    }

app.mount("/api/v1", v1_app)

if __name__ == "__main__":
    import uvicorn
    print("Running on port 8000")
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
