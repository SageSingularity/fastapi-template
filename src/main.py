from fastapi import FastAPI
from .auth.auth_routes import auth_router
from .business_logic.example_business_logic_routes import business_logic_router

app = FastAPI(
    title="FastAPI Template",
    description="A template for FastAPI projects",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(business_logic_router)

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to FastAPI Template"}
