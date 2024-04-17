"""
The Planner Service allows the API to manipulate courses data in the database.
"""

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.entities.user_entity import UserEntity
from backend.services.academics.course import CourseService
from backend.services.user import UserService

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
        user_svc: UserService = Depends(),
        course_svc: CourseService = Depends(),
    ):
        """Initializes the database session."""
        self._session = session
        self._permission_svc = permission_svc

    def add_user_course(self, subject: User, course_id: str):
        # print(UserService.get_courses(subject))
        member: UserEntity = (
            self._session.query(UserEntity).filter(UserEntity.id == subject.id).one()
        )
        course: CourseEntity = (
            self._session.query(CourseEntity).filter(CourseEntity.id == course_id).one()
        )
        member.courses.append(course)
        print("Added course to user")
        self._session.add(member)
        self._session.commit()
        print("Comitted session")
        return member.to_model()

    def delete_user_course(self, subject: User, course_id: str):
        # print("DELETE USER COURSE WORKS WOWOWOW")
        member: UserEntity = (
            self._session.query(UserEntity).filter(UserEntity.id == subject.id).one()
        )
        course: CourseEntity = (
            self._session.query(CourseEntity).filter(CourseEntity.id == course_id).one()
        )
        member.courses.remove(course)
        print("Deleted course from user")
        self._session.add(member)
        self._session.commit()
        print("Comitted session")
        return member.to_model()

    def is_course_added(self, subject: User, course_id: str):
        """Fetches a user's courses and returns true if course_id is present"""
        courses = UserService.get_courses(self, subject)
        for course in courses:
            if course.id == course_id:
                return True
        return False

    def get_user_courses(self, subject: User):
        """Returns a user's courses as a List[Course]"""
        courses = UserService.get_courses(self, subject)
        courseModels: list[Course] = []
        for course in courses:
            courseModels.append(course.to_model())
        return courseModels
      
    def get_prereq_status(self, subject: User, course_id: str) -> bool:
        """
        Returns a bool for if a given course is available or unavailable
        to a student based on their taken courses.
        """
        # optimize this later :/ embarassing highkey
        taken_courses = []
        # populate taken_courses with list of user course ids
        for course in self.get_user_courses(subject):
            taken_courses.append(course.id)

        courses = CourseService.all(self)
        for course in courses:
            if course.id == course_id:
                return eval(course.prereqs)
        return False
