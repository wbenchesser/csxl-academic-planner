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
import { ConstantPool } from '@angular/compiler';
import { MatDialog } from '@angular/material/dialog';
import { PlannerInfoComponent } from './academic-planner-info/planner-info/planner-info.component';

@Component({
  selector: 'app-academic-planner',
  templateUrl: './academic-planner.component.html',
  styleUrls: ['./academic-planner.component.css']
})
export class AcademicPlannerComponent implements OnInit {
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
  public selected: string = 'all';
  /** Store the currently-logged-in user's profile.  */
  public profile: Profile;

  /** Constructor for the academic planner page. */
  constructor(
    private route: ActivatedRoute,
    public academicsService: AcademicsService,
    private gearService: NagivationAdminGearService,
    private dialog: MatDialog
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

  setSelected(value: string) {
    this.selected = value;
  }

  populateCourseAvailability() {
    this.academicsService.getUntakenCourses(true).subscribe((value) => {
      this.availableCourses = value;
    });
    this.academicsService.getUntakenCourses(false).subscribe((value) => {
      this.unavailableCourses = value;
    });
  }

  isCourseElective(course: Course) {
    if (
      Number(course.number) > 420 &&
      Number(course.number) != 496 &&
      Number(course.number) != 690
    ) {
      return true;
    }
    return false;
  }

  handleButtonClick() {
    this.getUserCourses();
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(PlannerInfoComponent, {
      width: '60%',
      height: 'auto',
      panelClass: 'custom-dialog-container'
    });
  }
}
