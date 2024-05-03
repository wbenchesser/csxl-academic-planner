import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Course } from '../academics.models';
import { Profile } from '../../models.module';
import { AcademicsService } from '../academics.service';
import { Observable } from 'rxjs';
import { DetailsWidget } from './details.widget';

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
  isAdded: boolean = false;
  showDetailsWidget: boolean = false;
  chevronRotation: number = 0;

  @Input() isElective: boolean = false;

  /** Should this card display the add/remove button? */
  @Input() showAddRemoveButton!: boolean;

  /** When button in course-card clicked, emit event */
  @Output() public clicked = new EventEmitter();

  /**
   * Determines whether or not the tooltip on the card is disabled
   * @param element: The HTML element
   * @returns {boolean}
   */
  isTooltipDisabled(element: HTMLElement): boolean {
    return element.scrollHeight <= element.clientHeight;
  }

  addCourse() {
    this.service.addPlannerCourse(this.course).subscribe((value) => {
      console.log('add course subscribed');
      this.isCourseAdded();
      this.clicked.emit();
    });
  }

  removeCourse() {
    this.service.deletePlannerCourse(this.course).subscribe((value) => {
      console.log('remove course subscribed');
      this.isCourseAdded();
      this.clicked.emit();
    });
  }

  toggleCourse() {
    if (this.isAdded) {
      this.removeCourse();
    } else {
      this.addCourse();
    }
  }

  isCourseAdded() {
    this.service.isCourseAdded(this.course).subscribe((value) => {
      this.isAdded = value;
    });
  }

  toggleDetails() {
    this.showDetailsWidget = !this.showDetailsWidget;
    this.chevronRotation = this.showDetailsWidget ? 90 : 0;
  }

  // on initialization of page, calls isCourseAdded
  ngOnInit(): void {
    this.isCourseAdded();
  }

  constructor(private service: AcademicsService) {}
}
