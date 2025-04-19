import strawberry
from sqlalchemy.orm import Session
from models import ItemModel
from gqltypes import Item, ItemInput, ActionStatus


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
