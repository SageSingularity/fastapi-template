from fastapi import APIRouter
from pydantic import BaseModel

example_request_body_router = APIRouter(
    prefix="/example-request-body",
    tags=["example-request-body"],
)


@example_request_body_router.get("/")
async def example_request_body_root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name: str
    description: str | None = None # Optional field
    price: float
    tax: float | None = None # Optional field

@example_request_body_router.post("/items/", summary="Create an item as defined in the Item model.")
async def example_request_body_create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@example_request_body_router.put("/items/{item_id}",  summary="Demonstrates request body, path, and query parameters used together.")
async def example_request_body_path_and_query_parameters(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result