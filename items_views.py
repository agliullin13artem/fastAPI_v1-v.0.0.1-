from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/latest/")
def get_latest_item():
    return {
        "latest_item": {
            "id": 6,
            "name": "Latest Item",
            "description": "This is the latest item",
        }
    }



@router.get("/")
def get_items():
    return [
        "item1",
        "item2",
        "item3",
        "item4",
        "item5",
    ]


@router.get("/{item_id}/")
def item_id(item_id: Annotated[int, Path(ge=1, lt=100_000)]):
    return {
        "items_id": {
            "id": item_id,
            "name": f"Item {item_id} ",
            "description": "This is an item",
        }
    }


