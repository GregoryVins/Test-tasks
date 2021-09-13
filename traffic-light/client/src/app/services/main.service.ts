import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class MainService {
  public headers: any;
  public selectedItems: string[] = [];

  constructor(public httpClient: HttpClient) {
    this.headers = {
      'Content-Type': "application/json",
      'Access-Control-Allow-Headers': "*",
      'Access-Control-Allow-Origin': "*",
    }
  }


  getObjectList(userId?: string): Observable<any> {
    return this.httpClient.get(`http://127.0.0.1:8000/users/?userId=${userId}`)
  }

  getSubdivisions(): Observable<any> {
    return this.httpClient.get('http://127.0.0.1:8000/subdivs')
  }

  addItemInSelectedList(item: string): void {
    this.selectedItems.push(item);
  }

  deleteItemInSelectedList(item: any): void {}

  checkItemInSelectedItems(item: string): boolean {
    return !!this.selectedItems.find(id => id == item)
  }

  showMe(data: any): void {
    console.log(data);
  }
}
