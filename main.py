from fastapi import FastAPI

app = FastAPI(
    title="MicroServicio de reconocimiento facial",
    description="API para el MicroServicio de reconocimiento facial",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de reconocimiento facial",
        "version": "1.0.0",
        "author": "Jorge Gustavo Banegas Melgar",
        "email": "jorge.g.banegas@gmail.com",
        "github": "https://github.com/JorgeGBanegas",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
