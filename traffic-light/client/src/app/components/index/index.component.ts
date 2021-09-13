import {Component, OnInit} from '@angular/core';
import {MainService} from "../../services/main.service";

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
  public subDivs: any;

  constructor(public mainService: MainService) { }

  ngOnInit(): void {
    this.mainService.getSubdivisions().subscribe(value => {
      this.subDivs = value;
    });
  }

}
