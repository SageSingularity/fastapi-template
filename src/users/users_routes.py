from fastapi import APIRouter

users_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@users_router.get("/me")
async def user_me():
    return {"message": "Hello World"}

@users_router.get("/{user_id}")
async def user_by_id(user_id: int):
    return {"message": f"Item {user_id} retrieved"}