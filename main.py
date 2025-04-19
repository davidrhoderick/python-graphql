import strawberry

from enum import Enum

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from database import SessionLocal

from models import ListModel, SubItemModel, ItemModel


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@strawberry.input
class ListInput:
    id: strawberry.ID = None
    name: str


@strawberry.input
class ItemInput:
    listId: strawberry.ID
    id: strawberry.ID = None
    name: str
    description: str = None


@strawberry.type
class List:
    id: strawberry.ID
    name: str


@strawberry.type
class BaseItem:
    id: strawberry.ID
    name: str
    description: str = None
    completed: bool = False


@strawberry.type
class SubItem(BaseItem):
    pass


@strawberry.type
class Item(BaseItem):
    children: list["SubItem"] = None


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


@strawberry.type
class Mutation:
    @strawberry.mutation
    def put_list(self, input: ListInput) -> List:
        if not input.id:
            id = "123456"
        else:
            id = input.id
        return List(id=id, name=input.name)

    @strawberry.mutation
    def delete_list(self, id: strawberry.ID) -> ActionStatus:
        return ActionStatus.SUCCESS

    @strawberry.mutation
    def put_item(self, input: ItemInput) -> Item:
        if not input.id:
            id = "123456"
        else:
            id = input.id
        return Item(
            id=id,
            name=input.name,
            description=input.description,
            completed=False,
        )

    @strawberry.mutation
    def toggle_item_check(self, id: strawberry.ID) -> ActionStatus:
        return ActionStatus.SUCCESS

    @strawberry.mutation
    def delete_item(self, id: strawberry.ID) -> ActionStatus:
        return ActionStatus.SUCCESS


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
