from fastapi import APIRouter, Query
from typing import Annotated

example_query_parameters_router = APIRouter(
    prefix="/example-query-parameters",
    tags=["example-query-parameters"],
)


@example_query_parameters_router.get("/")
async def example_root():
    return {"message": "Hello World"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Required Query Parameters:
# When you declare function parameters that are not part of the path parameters
# they are automatically interpreted as query parameters.
@example_query_parameters_router.get("/query-parameters/default-values",
                                     summary="Provide default values for query parameters.")
async def query_parameters_get_subset_of_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/items/
# is the same as:
# http://127.0.0.1:8000/items/?skip=0&limit=10
# But if you go to:
# http://127.0.0.1:8000/items/?skip=20
# The parameter values in your function will be:
# skip = 20
# limit = 10

# Optional Query Parameters:
# Set the default to None: q: str | None = None
# q is also not in the path, so it is interpreted as a query parameter
@example_query_parameters_router.get("/query-parameters/q-is-optional/{item_id}",
                                     summary="Parameters not included in the path become optional.",
                                     description="To make a parameter optional, do not use it in the path and set a default value of None."
                                     "\nExample: q: str | None = None",)
async def query_parameters_read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@example_query_parameters_router.get("/query-parameters/type-conversion/{item_id}",
                                     summary="If you declare bool types, they will be converted.",
                                     description="All of the following are interpreted as a bool value of True:"
                                      "\n1. http://127.0.0.1:8000/items/foo?short=1"
                                      "\n2. http://127.0.0.1:8000/items/foo?short=True"
                                      "\n3. http://127.0.0.1:8000/items/foo?short=true"
                                      "\n4. http://127.0.0.1:8000/items/foo?short=on"
                                      "\n5. http://127.0.0.1:8000/items/foo?short=yes",)
async def query_parameters_type_conversion(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@example_query_parameters_router.get("/query-parameters/required-parameter/{item_id}",
                                     summary="Enforce required query parameters.",
                                     description="Defining the query parameter without a default value will make it required.",)
async def query_parameters_required_parameter(item_id: str, required_query_parameter: str):
    item = {"item_id": item_id, "required_query_parameter": required_query_parameter}
    return item

@example_query_parameters_router.get("/query-parameters/additional-validation-via-annotated/{item_id}",
                                     summary="Enforce additional validation rules via annotated query parameters.",
                                     description="Read more here: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#use-annotated-in-the-type-for-the-q-parameter.",)
async def query_parameters_additional_validation_via_query_and_annotated(
    item_id: str, required_query_parameter: Annotated[str, Query(min_length=3, max_length=50)]):
    item = {"item_id": item_id, "required_query_parameter": required_query_parameter}
    return item