import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcademicPlannerComponent } from './academic-planner.component';

describe('AcademicPlannerComponent', () => {
  let component: AcademicPlannerComponent;
  let fixture: ComponentFixture<AcademicPlannerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AcademicPlannerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AcademicPlannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
