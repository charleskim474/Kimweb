function time(){
    let intro = document.getElementById("intH1");
    let t = new Date();
    let h = t.getHours();
    let m = t.getMinutes();
    let s = t.getSeconds();

    if(h < 12){
          intro.textContent = "Good Morning!"
        }
     else if(h >= 12 && h < 16){
         intro.textContent = "Good Afternoon!"
       }
     else{
         intro.textContent = "Good Evening!"
     }
}

setInterval(time,1000);

let table = document.getElementById("myTable");
let rows = table.getElementsByTagName("tr");

for(let i = 0; i<rows.length; i++){
    if(i%2 == 0){
        rows[i].style.backgroundColor = 'lightgray';
    } else{
        rows[i].style.backgroundColor = 'lightblue';
    }
}