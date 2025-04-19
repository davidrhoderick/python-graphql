import strawberry
from sqlalchemy.orm import Session, joinedload
from models import ListModel
from gqltypes import List, Item, ListInput, ActionStatus


def get_lists(info: strawberry.Info) -> list[List]:
    db: Session = info.context["db"]
    db_lists = db.query(ListModel).all()
    return [List(id=db_list.id, name=db_list.name) for db_list in db_lists]


def get_list(id: strawberry.ID, info: strawberry.Info) -> List:
    db: Session = info.context["db"]
    db_list = (
        db.query(ListModel)
        .options(joinedload(ListModel.items))
        .filter(ListModel.id == id)
        .first()
    )
    if db_list:
        items = [
            Item(
                id=item.id,
                name=item.name,
                description=item.description,
                completed=item.completed,
            )
            for item in db_list.items
        ]
        return List(id=db_list.id, name=db_list.name, items=items)
    else:
        raise ValueError("List not found")


def put_list(input: ListInput, info: strawberry.Info) -> List:
    db: Session = info.context["db"]
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


def delete_list(id: strawberry.ID, info: strawberry.Info) -> ActionStatus:
    db: Session = info.context["db"]
    db_list = db.query(ListModel).filter(ListModel.id == id).first()
    if db_list:
        db.delete(db_list)
        db.commit()
        return ActionStatus.SUCCESS
    else:
        raise ValueError("List not found")
