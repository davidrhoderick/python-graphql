from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase
from database import Base


class Base(DeclarativeBase):
    pass


class ListModel(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    items = relationship(
        "ItemModel", back_populates="list", cascade="all, delete-orphan"
    )


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    list_id = Column(Integer, ForeignKey("lists.id"))

    list = relationship("ListModel", back_populates="items")
    children = relationship(
        "SubItemModel", back_populates="parent_item", cascade="all, delete-orphan"
    )


class SubItemModel(Base):
    __tablename__ = "subitems"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    parent_item_id = Column(Integer, ForeignKey("items.id"))

    parent_item = relationship("ItemModel", back_populates="children")
