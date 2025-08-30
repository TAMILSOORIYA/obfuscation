from fastapi import FastAPI
from routers import users

app = FastAPI(title="My FastAPI CSR Example")

# include routers
app.include_router(users.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000)