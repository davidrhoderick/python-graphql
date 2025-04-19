import strawberry
from lists import (
    get_lists,
    get_list,
    put_list,
    delete_list,
)
from items import (
    put_item,
    toggle_item_completion,
    put_sub_item,
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
    put_sub_item = strawberry.mutation(resolver=put_sub_item)
    toggle_item_completion = strawberry.mutation(resolver=toggle_item_completion)
    delete_item = strawberry.mutation(resolver=delete_item)


schema = strawberry.Schema(query=Query, mutation=Mutation)
