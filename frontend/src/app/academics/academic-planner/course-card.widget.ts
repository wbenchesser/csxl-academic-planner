import { Component, Input } from '@angular/core';
import { Course } from '../academics.models';
import { Profile } from '../../models.module';
import { AcademicsService } from '../academics.service';

@Component({
  selector: 'course-card',
  templateUrl: './course-card.widget.html',
  styleUrls: ['./course-card.widget.css']
})
export class CourseCard {
  /** The organization to show */
  @Input() course!: Course;
  /** The profile of the currently signed in user */
  @Input() profile?: Profile;
  /** @deprecated Stores the permission values for a profile */
  @Input() profilePermissions!: Map<number, number>;

  /** Is course added to profile? */
  isAdded: boolean;

  /**
   * Determines whether or not the tooltip on the card is disabled
   * @param element: The HTML element
   * @returns {boolean}
   */
  isTooltipDisabled(element: HTMLElement): boolean {
    return element.scrollHeight <= element.clientHeight;
  }

  addCourse() {
    this.service.addPlannerCourse(this.course);
  }

  removeCourse() {
    this.service.deletePlannerCourse(this.course);
  }

  constructor(private service: AcademicsService) {
    this.isAdded = false;
  }
}
