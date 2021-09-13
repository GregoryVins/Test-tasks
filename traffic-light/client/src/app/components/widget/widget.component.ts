import {Component, Input, OnInit} from '@angular/core';
import {MainService} from "../../services/main.service";

@Component({
  selector: 'app-widget',
  templateUrl: './widget.component.html',
  styleUrls: ['./widget.component.css']
})
export class WidgetComponent implements OnInit {
  @Input() userId: any;
  public data: any;

  constructor(public mainService: MainService) {
  }

  ngOnInit(): void {
    this.mainService.getObjectList(this.userId).subscribe(value => {
      this.data = value;
    });
  }

}
