from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema
from context import get_context
from fastapi.middleware.cors import CORSMiddleware

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_app, prefix="/graphql")
