from fastapi import APIRouter

business_logic_router = APIRouter(
    prefix="/business-logic",
    tags=["business-logic"],
)


@business_logic_router.get("/")
async def business_logic():
    return {"message": "Hello World"}
