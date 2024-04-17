import { Component, OnInit } from '@angular/core';
import { CoursesHomeComponent } from '../course-catalog/course-catalog.component';
import { Course } from '../academics.models';
import { ActivatedRoute } from '@angular/router';
import { AcademicsService } from '../academics.service';
import { NagivationAdminGearService } from 'src/app/navigation/navigation-admin-gear.service';
import { profileResolver } from '/workspace/frontend/src/app/profile/profile.resolver';
import { courseResolver } from '../academics.resolver';
import { Profile } from 'src/app/models.module';
import { UserAdminService } from 'src/app/admin/users/user-admin.service';

@Component({
  selector: 'app-academic-planner',
  templateUrl: './academic-planner.component.html',
  styleUrls: ['./academic-planner.component.css']
})
export class AcademicPlannerComponent {
  public static Route = {
    path: 'planner',
    title: 'Academic Planner',
    component: AcademicPlannerComponent,
    canActivate: [],
    resolve: { profile: profileResolver, courses: courseResolver }
  };

  /** Store a list of Courses locally taken from the Database */
  public courses!: Course[];
  public userCourses!: Course[];
  public availableCourses: Course[] = [];
  public unavailableCourses: Course[] = [];
  /** Store the currently-logged-in user's profile.  */
  public profile: Profile;

  /** Constructor for the academic planner page. */
  constructor(
    private route: ActivatedRoute,
    public academicsService: AcademicsService,
    private gearService: NagivationAdminGearService
  ) {
    /** Initialize data from resolvers. */
    const data = this.route.snapshot.data as {
      profile: Profile;
    };
    this.profile = data.profile;
    academicsService.getCourses().subscribe((res) => {
      this.courses = res;
      this.populateCourseAvailability();
    });
  }

  ngOnInit() {
    this.gearService.showAdminGear(
      'academics.*',
      '*',
      '',
      'academics/admin/course'
    );
    this.getUserCourses();
  }

  getUserCourses() {
    this.academicsService.getUserCourses().subscribe((value) => {
      this.userCourses = value;
      this.populateCourseAvailability();
    });
  }

  populateCourseAvailability() {
    for (var i = 0; i < this.courses?.length; i++) {
      ((index) => {
        this.academicsService
          .arePrereqsMet(this.courses[index])
          .subscribe((value) => {
            if (
              value &&
              this.userCourses.find((x) => x.id === this.courses[index].id)
            ) {
              // userCourses already populated
              console.log('found in userCourses!');
            } else if (
              value &&
              //!this.availableCourses.includes(this.courses[index])
              !this.availableCourses.find(
                (x) => x.id === this.courses[index].id
              )
            ) {
              this.availableCourses.push(this.courses[index]);
            } else if (
              !value &&
              //!this.availableCourses.includes(this.courses[index])
              !this.availableCourses.find(
                (x) => x.id === this.courses[index].id
              )
            ) {
              this.unavailableCourses.push(this.courses[index]);
            }
          });
      })(i);
    }
  }

  handleButtonClick() {
    this.getUserCourses();
  }
}
