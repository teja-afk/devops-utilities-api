import uvicorn

if __name__ == "__main__":
    # ASGI (Asynchronous Server Gateway Interface)
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
