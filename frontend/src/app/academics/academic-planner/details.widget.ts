import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Course } from '../academics.models';
import { Profile } from '../../models.module';
import { AcademicsService } from '../academics.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'details-box',
  templateUrl: './details.widget.html',
  styleUrls: ['./details.widget.css']
})
export class DetailsWidget {
  @Input() course!: Course;

  constructor() {}
}
