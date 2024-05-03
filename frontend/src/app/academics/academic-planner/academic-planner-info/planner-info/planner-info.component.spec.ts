import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlannerInfoComponent } from './planner-info.component';

describe('PlannerInfoComponent', () => {
  let component: PlannerInfoComponent;
  let fixture: ComponentFixture<PlannerInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlannerInfoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlannerInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
