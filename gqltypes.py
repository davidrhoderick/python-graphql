import strawberry
from strawberry.tools import create_type
from typing import Optional
from enum import Enum


@strawberry.input
class ListInput:
    id: Optional[strawberry.ID] = None
    name: str


@strawberry.input
class ItemInput:
    listId: strawberry.ID
    id: Optional[strawberry.ID] = None
    name: str
    description: Optional[str] = None


@strawberry.input
class SubItemInput:
    itemId: strawberry.ID
    id: Optional[strawberry.ID] = None
    name: str
    description: Optional[str] = None


@strawberry.type
class BaseList:
    id: strawberry.ID
    name: str


@strawberry.type
class List(BaseList):
    pass


@strawberry.type
class ListWithItems(BaseList):
    items: list[Optional["Item"]]


@strawberry.type
class BaseItem:
    id: strawberry.ID
    name: str
    description: Optional[str] = None
    completed: Optional[bool] = False


@strawberry.type
class SubItem(BaseItem):
    parent: strawberry.ID


@strawberry.type
class Item(BaseItem):
    children: Optional[list["SubItem"]] = None


@strawberry.enum
class ActionStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


@strawberry.type
class Query:
    @strawberry.field
    def lists(self) -> list[List]:
        return []

    @strawberry.field
    def list(self, id: strawberry.ID) -> list[Item]:
        return []
