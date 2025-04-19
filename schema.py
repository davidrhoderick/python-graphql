import strawberry
from resolvers import (
    get_lists,
    get_list,
    put_list,
    delete_list,
    put_item,
    toggle_item_check,
    delete_item,
)
from gqltypes import List, Item, ListInput, ItemInput, ActionStatus


@strawberry.type
class Query:
    lists = strawberry.field(resolver=get_lists)
    list = strawberry.field(resolver=get_list)


@strawberry.type
class Mutation:
    put_list = strawberry.mutation(resolver=put_list)
    delete_list = strawberry.mutation(resolver=delete_list)
    put_item = strawberry.mutation(resolver=put_item)
    toggle_item_check = strawberry.mutation(resolver=toggle_item_check)
    delete_item = strawberry.mutation(resolver=delete_item)


schema = strawberry.Schema(query=Query, mutation=Mutation)
