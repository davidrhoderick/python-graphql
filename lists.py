import strawberry
from sqlalchemy.orm import Session
from models import ListModel
from gqltypes import List, Item, ListInput, ActionStatus


def get_lists() -> list[List]:
    # Implement the logic to fetch lists from the database
    return []


def get_list(id: strawberry.ID) -> list[Item]:
    # Implement the logic to fetch a specific list from the database
    return []


def put_list(input: ListInput, info: strawberry.Info) -> List:

    print("context", info.context["db"])
    db = info.context["db"]
    if not input.id:
        db_list = ListModel(name=input.name)
        db.add(db_list)
        db.commit()
        db.refresh(db_list)
    else:
        db_list = db.query(ListModel).filter(ListModel.id == input.id).first()
        if db_list:
            db_list.name = input.name
            db.commit()
        else:
            raise ValueError("List not found")
    return List(id=db_list.id, name=db_list.name)


def delete_list(id: strawberry.ID) -> ActionStatus:
    # Implement the logic to delete a list from the database
    return ActionStatus.SUCCESS
