"""Tests for Planner Planner Service."""

from unittest.mock import create_autospec
import pytest
from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)
from backend.services.permission import PermissionService
from backend.services.user import UserService
from ....services.academics import CourseService, PlannerService
from ....models.academics import CourseDetails

# Imported fixtures provide dependencies injected for the tests as parameters.
from .fixtures import permission_svc, course_svc, planner_svc, user_svc

# Import the setup_teardown fixture explicitly to load entities in database
from .course_data import fake_data_fixture as insert_course_fake_data


# Import the fake model data in a namespace for test assertions
from . import course_data
from .. import user_data

"""def add_user_course(self, subject: User, course_id: str):
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
        Fetches a user's courses and returns true if course_id is present
        courses = UserService.get_courses(self, subject)
        for course in courses:
            if course.id == course_id:
                return True
        return False

    def get_user_courses(self, subject: User):
        Returns a user's courses as a List[Course]
        courses = UserService.get_courses(self, subject)
        courseModels: list[Course] = []
        for course in courses:
            courseModels.append(course.to_model())
        return courseModels
      
    def get_prereq_status(self, subject: User, course_id: str) -> bool:
        
        Returns a bool for if a given course is available or unavailable
        to a student based on their taken courses.
        
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
"""

def test_add_user_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(user_data.user))
    assert (user_svc.get_courses(user_data.user) == [course_data.comp_110])

def test_delete_user_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(user_data.user))
    assert (user_svc.get_courses(user_data.user) == [course_data.comp_110])
    planner_svc.delete_user_course(current_user, "comp110")
    assert (user_svc.get_courses(user_data.user) == [])

def test_is_course_added(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(user_data.user))
    assert (planner_svc.is_course_added(user_data.user, "comp110"))

def test_get_user_courses(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(user_data.user))
    assert (planner_svc.get_user_courses(user_data.user) == [course_data.comp_110])

def test_get_prereq_status(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    assert(not planner_svc.get_prereq_status(current_user, "comp210"))
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(user_data.user))
    assert (planner_svc.get_prereq_status(current_user, "comp210"))