from backend.entities.entity_base import EntityBase
from typing import Self
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


# class UserCourseEntity(EntityBase):
#     """Serves as the association table between the course and user table."""

#     # Name for the course and user table in the PostgreSQL database
#     __tablename__ = "user-course"

#     # Fields
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

#     # Two foreign key fields, as shown in the table above, to connect the
#     # course and user tables together.
#     course_id: Mapped[int] = mapped_column(
#         ForeignKey("academics__course.id"), primary_key=True, nullable=True
#     )
#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)

#     # Relationship Fields
#     course: Mapped["CourseEntity"] = relationship(back_populates="planner")
#     user: Mapped["UserEntity"] = relationship(back_populates="planner")

user_course_table = Table(
    "user_course",
    EntityBase.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("course_id", ForeignKey("academics__course.id"), primary_key=True),
)
