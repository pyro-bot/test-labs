import { Component } from '@angular/core';

interface Vars{
  a:number;
  b:number;
  c:number;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'app works!';
  vars:Vars;
  result:number|string;

  constructor(){
    this.vars={a:0,b:0,c:0};
    this.result=0;
    this.result=(this.factorial(this.vars.a)/this.vars.b)-this.vars.c;
  }

  factorial(i:number):number{
    let s=1;
    if (i<=0)return 1;
    for(let j:number=1;j<=i;j++)
      s*=j;
    return s;
  }

  onChange(e:any,varname:string){
    let buf:number;
    buf=Number.parseInt(e.target.value);
    if (!isNaN(buf)){
      this.vars[varname]=buf;
      this.result=(this.factorial(this.vars.a)/this.vars.b)-this.vars.c;
    }else{
      this.result='Ошибка ввода';
    }
  }
}
