import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcademicCourseSelectComponent } from './academic-course-select.component';

describe('AcademicCourseSelectComponent', () => {
  let component: AcademicCourseSelectComponent;
  let fixture: ComponentFixture<AcademicCourseSelectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AcademicCourseSelectComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(AcademicCourseSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
