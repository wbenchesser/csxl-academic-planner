import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-my-dialog',
  templateUrl: './planner-info.component.html',
  styleUrls: ['./planner-info.component.css']
})
export class PlannerInfoComponent {
  constructor(private dialogRef: MatDialogRef<PlannerInfoComponent>) {}

  closeDialog(): void {
    this.dialogRef.close();
  }
}
