import { Component } from '@angular/core';
import { AcademicsService } from '../../academics.service';
import { Profile } from 'src/app/models.module';
import { Course } from '../../academics.models';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-academic-course-select',
  templateUrl: './academic-course-select.component.html',
  styleUrls: ['./academic-course-select.component.css']
})
export class AcademicCourseSelectComponent {
  public static Route = {
    path: 'planner/select',
    title: 'Academic Planner',
    component: AcademicCourseSelectComponent
  };

  /** Store a list of Courses locally taken from the Database */
  public courses!: Course[];
  /** Store the currently-logged-in user's profile.  */
  public profile: Profile;

  constructor(
    private route: ActivatedRoute,
    public academicsService: AcademicsService
  ) {
    const data = this.route.snapshot.data as {
      profile: Profile;
    };
    this.profile = data.profile;
    academicsService.getCourses().subscribe((res) => (this.courses = res));
  }
}
