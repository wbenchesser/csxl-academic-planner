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


@api.post("/{id}", response_model=None, tags=["Academics"])
def new_term(
    id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Adds a course to the user list of courses

    pulling course from courses list using id would prob be easiest

    Returns:
        Course: the added course? maybe?
    """
    return planner_service.add_user_course(subject, id)
    # This is copied from the term.py file and tweaked


@api.delete("/{id}", response_model=None, tags=["Academics"])
def delete_term(
    id: str,
    subject: User = Depends(registered_user),
    planner_service: PlannerService = Depends(),
):
    """
    Deletes a course from the user list of courses

    PlannerService is not yet defined. Delete this comment when resolved, aka if
    PlannerService has no yellow line
    """
    return planner_service.delete_user_course(subject, id)
    # This is copied from the term.py file and tweaked
