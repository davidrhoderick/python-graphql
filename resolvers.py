import strawberry
from sqlalchemy.orm import Session
from models import ListModel, ItemModel
from gqltypes import List, Item, ListInput, ItemInput, ActionStatus


def get_lists() -> list[List]:
    # Implement the logic to fetch lists from the database
    return []


def get_list(id: strawberry.ID) -> list[Item]:
    # Implement the logic to fetch a specific list from the database
    return []


def put_list(input: ListInput) -> List:
    # Implement the logic to add or update a list in the database
    return List(id="123456", name=input.name)


def delete_list(id: strawberry.ID) -> ActionStatus:
    # Implement the logic to delete a list from the database
    return ActionStatus.SUCCESS


def put_item(input: ItemInput) -> Item:
    # Implement the logic to add or update an item in the database
    return Item(
        id="123456", name=input.name, description=input.description, completed=False
    )


def toggle_item_check(id: strawberry.ID) -> ActionStatus:
    # Implement the logic to toggle an item's completion status
    return ActionStatus.SUCCESS


def delete_item(id: strawberry.ID) -> ActionStatus:
    # Implement the logic to delete an item from the database
    return ActionStatus.SUCCESS
