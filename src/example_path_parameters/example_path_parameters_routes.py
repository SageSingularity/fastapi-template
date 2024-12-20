from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Path, Query

example_path_parameters_router = APIRouter(
    prefix="/example-path-parameters",
    tags=["example-path-parameters"],
)

@example_path_parameters_router.get("/")
async def path_parameters_root():
    return {"message": "Hello World"}

@example_path_parameters_router.get("/{item_id}",
                                     summary="The item_id is a path parameter in this example.")
async def path_parameters_item_id(item_id):
    return {"item_id": item_id}

@example_path_parameters_router.get("/typed/{item_id}",
                                     summary="Provides a type for the path parameter.")
async def path_parameters_typed(item_id: int):
    return {"item_id": item_id}

# Enum Selector:
# Define possible selections for AI models by name
class AvailableAIModels(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@example_path_parameters_router.get("/enum/{model_name}")
async def path_parameters_enum_selector(model_name: AvailableAIModels):
    if model_name is AvailableAIModels.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@example_path_parameters_router.get("/additional-validation-via-annotated/{item_id}")
async def path_parameters_additional_validation_via_query_and_annotated(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results