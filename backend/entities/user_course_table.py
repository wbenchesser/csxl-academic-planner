from backend.entities.entity_base import EntityBase
from typing import Self
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

user_course_table = Table(
    "user_course",
    EntityBase.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("course_id", ForeignKey("academics__course.id"), primary_key=True),
)
