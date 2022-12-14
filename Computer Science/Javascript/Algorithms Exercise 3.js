/* Algorithms Exercise */
//Question 3
// let userNumber = Number(prompt("What number do you want to go up to"));
// let winton = 0;
// //let number = userNumber*2
// document.write("<pre>");
// for(let row = 0; row < userNumber; row++){
//     winton++;
//     for(let amogus = 0; amogus < userNumber; amogus++){
//         if (row == amogus || amogus == userNumber - row - 1) {
//             document.write(winton, " ");
//         } else {
//             document.write("  ");
//     }
//     }
//     document.write("<br/>");
// }document.write("<pre>");


let User_Number = Number(prompt(" Please enter a number: "));
let bawb = 0;
let kevin = 0;
document.write("<pre>");
let critter = " "; 
let rows = User_Number * 2 - 1;
let collumns = User_Number * 2 - 3;
let spaces = collumns - 2;
    
for(let cheese = 1; cheese<=User_Number; cheese++){
 
if(cheese == 1){
    document.write(cheese);
    while(kevin != collumns){
        document.write(critter);
        kevin++;
    }
    document.write(cheese);
    kevin = 0;
    document.write("<br/>");
}
else if(cheese > 1 && cheese != User_Number){
     while(bawb != cheese - 1){
        document.write(critter);
        bawb++;
    }
    bawb = 0;
        document.write(cheese);
        while(kevin != collumns){
            document.write(critter);
            kevin++;
        }
        document.write(cheese);
        kevin = 0;
        document.write("<br/>");
}
else if(cheese == User_Number){
    while(bawb != cheese - 1){
        document.write(critter);
        bawb++;
    }
    bawb = 0;
    document.write(cheese);
}  
collumns = collumns - 2;
    // if(cheese < User_Number){
    //     document.write(cheese, critter, cheese);
    //     document.write("<br/>");
    // }else if(cheese = User_Number){
    //     document.write(cheese);
    //     document.write("<br/>");
    // }
}
document.write("<pre>");
