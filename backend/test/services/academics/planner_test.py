"""Tests for Planner Planner Service."""

from unittest.mock import create_autospec
import pytest
from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)
from ....services.permission import PermissionService
from ....services.user import UserService
from ....services.academics import CourseService, PlannerService
from ....models.academics import CourseDetails

from sqlalchemy.exc import IntegrityError

# Imported fixtures provide dependencies injected for the tests as parameters.
from .fixtures import permission_svc, course_svc, planner_svc
from ..fixtures import user_svc, user_svc_integration, permission_svc_mock

from ..core_data import setup_insert_data_fixture

# Import the setup_teardown fixture explicitly to load entities in database
from .course_data import fake_data_fixture as insert_course_fake_data


# Import the fake model data in a namespace for test assertions
from . import course_data
from ..user_data import user


def test_add_user_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(current_user))
    # Checks that the specific class 'comp110' is added to user's courses
    assert user_svc.get_courses(current_user)[0].to_model() == course_data.comp_110


def test_delete_user_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(current_user))
    # Checks that the user's course list has in fact changed and has what is added
    assert user_svc.get_courses(current_user)[0].to_model() == course_data.comp_110
    planner_svc.delete_user_course(current_user, "comp110")
    # Checks that that same list now is empty
    assert user_svc.get_courses(current_user) == []


def test_is_course_added(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(current_user))
    assert planner_svc.is_course_added(current_user, "comp110")


def test_get_user_courses(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    print(user_svc.get_courses(current_user))
    assert planner_svc.get_user_courses(current_user) == [course_data.comp_110]


def test_get_available_courses(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    exists = False
    for course in planner_svc.get_available_courses(current_user):
        if course.id == "comp210":
            exists = True
    for course in planner_svc.get_available_courses(current_user):
        if course.id == "comp110":
            exists = False
    assert exists


def test_get_unavailable_courses(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    exists = False
    for course in planner_svc.get_unavailable_courses(current_user):
        if course.id == "comp210":
            exists = True
    planner_svc.add_user_course(current_user, "comp110")
    planner_svc.add_user_course(current_user, "math231")
    for course in planner_svc.get_unavailable_courses(current_user):
        if course.id == "comp210":
            exists = False
    assert exists


def test_add_added_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    planner_svc.add_user_course(current_user, "comp110")
    assert len(user_svc.get_courses(current_user)) == 1
    with pytest.raises(IntegrityError):
        planner_svc.add_user_course(current_user, "comp110")


def test_delete_nonexistent_course(planner_svc: PlannerService, user_svc: UserService):
    current_user = user_svc.get(user.pid)
    assert current_user is not None
    with pytest.raises(ValueError):
        planner_svc.delete_user_course(current_user, "comp110")
