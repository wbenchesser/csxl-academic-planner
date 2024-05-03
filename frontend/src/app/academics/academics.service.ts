/**
 * The Academics Service abstracts HTTP requests to the backend
 * from the components.
 *
 * @author Ajay Gandecha <agandecha@unc.edu>
 * @copyright 2023
 * @license MIT
 */

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from '../authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';
import { Course, Room, Section, Term } from './academics.models';

@Injectable({
  providedIn: 'root'
})
export class AcademicsService {
  constructor(
    protected http: HttpClient,
    protected auth: AuthenticationService,
    protected snackBar: MatSnackBar
  ) {}

  /** Returns all term entries from the backend database.
   * @returns {Observable<Term[]>}
   */
  getTerms(): Observable<Term[]> {
    return this.http.get<Term[]>('/api/academics/term');
  }

  /** Returns the current term from the backend database.
   * @returns {Observable<Term>}
   */
  getCurrentTerm(): Observable<Term> {
    return this.http.get<Term>('/api/academics/term/current');
  }

  /** Returns one term from the backend database.
   * @param id ID of the course to look up
   * @returns {Observable<Term>}
   */
  getTerm(id: string): Observable<Term> {
    return this.http.get<Term>(`/api/academics/term/${id}`);
  }

  /** Creates a new term.
   * @param term: Term to create
   * @returns {Observable<Term>}
   */
  createTerm(term: Term): Observable<Term> {
    return this.http.post<Term>('/api/academics/term', term);
  }

  /** Update a term.
   * @param term: Term to update
   * @returns {Observable<Term>}
   */
  updateTerm(term: Term): Observable<Term> {
    return this.http.put<Term>('/api/academics/term', term);
  }

  /** Delete a term.
   * @param course: Term to update
   * @returns {Observable<Term>}
   */
  deleteTerm(term: Term) {
    return this.http.delete(`/api/academics/term/${term.id}`);
  }

  /** Returns all course entries from the backend database.
   * @returns {Observable<Course[]>}
   */
  getCourses(): Observable<Course[]> {
    return this.http.get<Course[]>('/api/academics/course');
  }

  /** Returns one course from the backend database.
   * @param id ID of the course to look up
   * @returns {Observable<Course>}
   */
  getCourse(id: string): Observable<Course> {
    return this.http.get<Course>(`/api/academics/course/${id}`);
  }

  /** Creates a new course.
   * @param course: Course to create
   * @returns {Observable<Course>}
   */
  createCourse(course: Course): Observable<Course> {
    return this.http.post<Course>('/api/academics/course', course);
  }

  /** Update a course.
   * @param course: Course to update
   * @returns {Observable<Course>}
   */
  updateCourse(course: Course): Observable<Course> {
    return this.http.put<Course>('/api/academics/course', course);
  }

  /** Delete a course.
   * @param course: Course to delete
   * @returns {Observable<Course>}
   */
  deleteCourse(course: Course) {
    return this.http.delete(`/api/academics/course/${course.id}`);
  }

  /** Returns all section entries by a term.
   * @param term Term to get sections by
   * @returns {Observable<Section[]>}
   */
  getSectionsByTerm(term: Term): Observable<Section[]> {
    return this.http.get<Section[]>(`/api/academics/section/term/${term.id}`);
  }

  /** Returns one section from the backend database.
   * @param id ID of the section to look up
   * @returns {Observable<Section>}
   */
  getSection(id: number): Observable<Section> {
    return this.http.get<Section>(`/api/academics/section/${id}`);
  }

  /** Creates a new section.
   * @param section: Section to create
   * @returns {Observable<Section>}
   */
  createSection(section: Section): Observable<Section> {
    return this.http.post<Section>('/api/academics/section', section);
  }

  /** Update a section.
   * @param section: Section to update
   * @returns {Observable<Section>}
   */
  updateSection(section: Section): Observable<Section> {
    return this.http.put<Section>('/api/academics/section', section);
  }

  /** Delete a section.
   * @param section: Section to delete
   * @returns {Observable<Section>}
   */
  deleteSection(section: Section) {
    return this.http.delete(`/api/academics/section/${section.id}`);
  }

  /** Returns all room entries from the backend database.
   * @returns {Observable<Room[]>}
   */
  getRooms(): Observable<Room[]> {
    return this.http.get<Room[]>('/api/room');
  }

  /** Returns one soom from the backend database.
   * @param id ID of the room to look up
   * @returns {Observable<Room>}
   */
  getRoom(id: string): Observable<Room> {
    return this.http.get<Room>(`/api/room/${id}`);
  }

  /** Creates a new room.
   * @param room: room to create
   * @returns {Observable<Room>}
   */
  createRoom(room: Room): Observable<Room> {
    return this.http.post<Room>('/api/room', room);
  }

  /** Update a room.
   * @param room: room to update
   * @returns {Observable<Room>}
   */
  updateRoom(room: Room): Observable<Room> {
    return this.http.put<Room>('/api/room', room);
  }

  /** Delete a room.
   * @param room: room to delete
   * @returns {Observable<Room>}
   */
  deleteRoom(room: Room) {
    return this.http.delete(`/api/academics/room/${room.id}`);
  }

  /** Add a course to user's list in planner
   * @param course: class to add
   * @returns
   */
  addPlannerCourse(course: Course) {
    console.log(`AcademicService: addPlannerCourse called with ${course}`);

    const dummyCourse = {
      id: 'identification',
      subject_code: 'subject code',
      number: '423',
      title: 'Foundations of Software engineering',
      description: 'Kris Jordan mode',
      credit_hours: '3',
      sections: null,
      prereqs: ''
    };
    return this.http.post<Course>(
      `/api/academics/planner/${course.id}`,
      course
    );
  }

  /** Delete a course from a user's list in planner
   * @param course
   * @returns
   */
  deletePlannerCourse(course: Course) {
    console.log(`AcademicService: deletePlannerCourse called with ${course}`);

    const dummyCourse = {
      id: 'identification',
      subject_code: 'subject code',
      number: '423',
      title: 'Foundations of Software engineering',
      description: 'Kris Jordan mode',
      credit_hours: '3',
      sections: null,
      prereqs: ''
    };
    return this.http.delete(`/api/academics/planner/${course.id}`);
  }

  /** Checks for the widget if a course is already added
   * @param course
   * @returns Observable<boolean>
   */
  isCourseAdded(course: Course) {
    console.group(`AcademicService: isCourseAdded called`);

    return this.http.get<boolean>(`/api/academics/planner/${course.id}`);
  }

  /** returns the courses a user has added
   * @param
   * @returns {Observable<Course[]>}
   */
  getUserCourses() {
    return this.http.get<Course[]>('/api/academics/planner');
  }

  /** Checks prereqs for one course
   * @param
   * @returns {Observable<boolean>}
   */
  arePrereqsMet(course: Course) {
    console.log('prereqs API called');
    return this.http.get<boolean>(
      `/api/academics/planner/prereqs/${course.id}`
    );
  }

  /** Checks prereqs for all the courses
   * @param courses
   * @returns {Observable<Map<string, boolean>>}
   */
  arePrereqsMetAll(): Observable<Map<string, boolean>> {
    console.log('all prereqs api called');
    return this.http.get<Map<string, boolean>>(
      `/api/academics/planner/prereqs`
    );
  }

  /** Returns the courses to be put in the available or unavailable lists
   * @param availableOrUnavailable
   * @returns {Ovservable<Course[]>}
   */
  getUntakenCourses(availableOrUnavailable: boolean) {
    if (availableOrUnavailable) {
      return this.http.get<Course[]>('api/academics/planner/available');
    } else {
      return this.http.get<Course[]>('api/academics/planner/unavailable');
    }
  }
}
