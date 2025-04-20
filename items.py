import strawberry
from sqlalchemy.orm import Session
from models import ItemModel, SubItemModel
from gqltypes import Item, ItemInput, SubItemInput, SubItem, ActionStatus


def put_item(input: ItemInput, info: strawberry.Info) -> Item:
    db: Session = info.context["db"]

    if input.id:
        db_item = db.query(ItemModel).filter(ItemModel.id == input.id).first()
        if db_item:
            db_item.name = input.name
            db_item.description = input.description
        else:
            raise ValueError("Item not found")
    else:
        db_item = ItemModel(
            name=input.name,
            description=input.description,
            completed=False,
            list_id=input.listId,
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_item)

    return Item(
        id=db_item.id,
        name=db_item.name,
        description=db_item.description,
        completed=db_item.completed,
    )


def put_sub_item(input: SubItemInput, info: strawberry.Info) -> SubItem:
    db: Session = info.context["db"]
    parent = db.query(ItemModel).filter(ItemModel.id == input.itemId).first()

    if not parent:
        raise ValueError("Parent item not found")

    sub_item = db.query(SubItemModel).filter(SubItemModel.id == input.id).first()

    if sub_item:
        sub_item.name = input.name
        sub_item.description = input.description
    else:
        sub_item = SubItemModel(
            name=input.name,
            parent_item=parent,
            description=input.description,
            completed=False,
        )
        db.add(sub_item)

    db.commit()

    return SubItem(
        id=sub_item.id,
        name=sub_item.name,
        parent=sub_item.parent_item.id,
        description=sub_item.description,
        completed=sub_item.completed,
    )


def toggle_item_completion(id: strawberry.ID, info: strawberry.Info) -> Item:
    db: Session = info.context["db"]
    item = db.query(ItemModel).filter(ItemModel.id == id).first()

    if not item:
        raise ValueError("Item not found")

    item.completed = not item.completed

    db.commit()

    return item


def toggle_sub_item_completion(id: strawberry.ID, info: strawberry.Info) -> Item:
    db: Session = info.context["db"]
    sub_item = db.query(SubItemModel).filter(SubItemModel.id == id).first()

    if not sub_item:
        raise ValueError("Item not found")

    sub_item.completed = not sub_item.completed

    db.commit()

    return sub_item


def delete_item(id: strawberry.ID, info: strawberry.Info) -> ActionStatus:
    db: Session = info.context["db"]
    db_list = db.query(ItemModel).filter(ItemModel.id == id).first()
    if db_list:
        db.delete(db_list)
        db.commit()
        return ActionStatus.SUCCESS
    else:
        raise ValueError("Item not found")


def delete_sub_item(id: strawberry.ID, info: strawberry.Info) -> ActionStatus:
    db: Session = info.context["db"]
    db_list = db.query(SubItemModel).filter(SubItemModel.id == id).first()
    if db_list:
        db.delete(db_list)
        db.commit()
        return ActionStatus.SUCCESS
    else:
        raise ValueError("Subitem not found")
