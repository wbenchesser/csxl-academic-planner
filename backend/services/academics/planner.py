"""
The Planner Service allows the API to manipulate courses data in the database.
"""

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ...database import db_session
from ...models.academics import Course
from ...models.academics import CourseDetails
from ...models.user import User
from ...entities.academics import CourseEntity
from ..permission import PermissionService

from ...services.exceptions import ResourceNotFoundException
from datetime import datetime


class PlannerService:
    """Service that performs all of the actions on the `Course` table"""

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission_svc: PermissionService = Depends(),
    ):
        """Initializes the database session."""
        self._session = session
        self._permission_svc = permission_svc

    def add_user_course(self, subject: User, id: str):
        return True

    def delete_user_course(self, subject: User, id: str):
        return True
