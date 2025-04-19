import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


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
class Item:
    id: strawberry.ID
    name: str
    description: str = None
    completed: bool = False
    children: list["Item"] = None


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


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
