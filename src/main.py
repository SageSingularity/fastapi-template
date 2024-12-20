from fastapi import FastAPI
from src.auth.auth_routes import auth_router
from src.users.users_routes import users_router
from src.example_path_parameters.example_path_parameters_routes import example_path_parameters_router
from src.example_query_parameters.example_query_parameters_routes import example_query_parameters_router
from src.example_request_body.example_request_body_routes import example_request_body_router

app = FastAPI(
    title="FastAPI Template",
    description="A template for FastAPI projects",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(example_path_parameters_router)
app.include_router(example_query_parameters_router)
app.include_router(example_request_body_router)
app.include_router(users_router)

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to FastAPI Template"}