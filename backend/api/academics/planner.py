"""Courses Planner API

This API is used to access course data."""

from fastapi import APIRouter, Depends
from ..authentication import registered_user
from ...services.academics import PlannerService
from ...models import User

# Currently authored by Asim Raja

api = APIRouter(prefix="/api/academics/planner")
openapi_tags = {
    "name": "Academics",
    "description": "Academic and course information are managed via these endpoints.",
}


@api.post("/{course_id}", response_model=None, tags=["Academics"])
def add_course(
    course_id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Adds a course to the user list of courses

    pulling course from courses list using id would prob be easiest

    Returns:
        Course: the added course? maybe?
    """
    return planner_service.add_user_course(subject, course_id)
    # This is copied from the term.py file and tweaked


@api.delete("/{course_id}", response_model=None, tags=["Academics"])
def remove_course(
    course_id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Deletes a course from the user list of courses

    PlannerService is not yet defined. Delete this comment when resolved, aka if
    PlannerService has no yellow line
    """
    return planner_service.delete_user_course(subject, course_id)
    # This is copied from the term.py file and tweaked


@api.get("/{course_id}", response_model=None, tags=["Academics"])
def is_course_added(
    course_id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Checks whether a course is added to the User's list,
    so the card-widget knows what button to display
    """
    return planner_service.is_course_added(subject, course_id)


@api.get("", response_model=None, tags=["Academics"])
def get_user_courses(
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Returns User's list of courses as Course Models
    """
    return planner_service.get_user_courses(subject)
  
@api.get("/prereqs/{course_id}", response_model=None, tags=["Academics"])
def get_prereq_status(
    course_id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Returns whether a given course's prereqs are met based on the user's courses.
    """
    return planner_service.get_prereq_status(subject, course_id)
