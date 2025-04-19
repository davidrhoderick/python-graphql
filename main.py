import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


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


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
