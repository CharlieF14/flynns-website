/* Javascript Assignment 10 */

//Question 1
// let userRow = Number(prompt("How many rows do you want?"));
// let userCollumn = userRow;
// for(let row = 0; row != userRow; row++){
//     for(let collumn = 0; collumn != userCollumn; collumn++){
//         document.write("*");
//     }document.write("<br>");
// }document.write("<br>");

// //Question 2
// let userRow1 = Number(prompt("How many rows do you want?"));
// let userCollumn1 = Number(prompt("How many collumns do you want?"));
// for(let row1 = 0; row1 != userRow1; row1++){
//     for(let collumn1 = 0; collumn1 != userCollumn1; collumn1++){
//         document.write("*");
//     }document.write("<br>");
// }document.write("<br>");

//Question 3
// let userRow2 = Number(prompt("How many rows do you want?"));
// let userCollumn2 = userRow2;
// document.write("<pre>");
// for(let row2 = 0; row2 != userRow2; row2++){
//     if(row2 == 0|| row2 == userRow2 - 1){
//         for (let o =0; o<userCollumn2; o++){
//             document.write("*");
//         }
//     }
//     else{
//         for(r=0; r < userCollumn2; ){
//             if(r == 0 || r == userCollumn2 -1){
//                 document.write("*");
//             }
//             document.write("&nbsp");
//             r++;
//         }
//     }
//     document.write("<br/>");
// }document.write("<pre>");

//Question 4
// let userRow3 = Number(prompt("How many rows do you want?"));
// //let userCollumn3 = userRow3;
// //let b = userRow3 - b + 1;
// document.write("<pre>");
// for(let row3 = 0; row3 < userRow3; row3++){
//     for(let y = 0; y < userRow3; y++){
//         if (row3 == 0 || row3 == userRow3 - 1 || y == 0 || y == userRow3 - 1 || row3 == y || y == userRow3 - row3 - 1) {
//             document.write("* ");
//         } else {
//             document.write("  ");
//     }
//     }
//     document.write("<br/>");
// }document.write("<pre>");

//Question 5
let userRow4 = Number(prompt("How many rows do you want?"));
let userCollumn4 = userRow4;
//let blank = "&nbsp";
document.write("<pre>");
for(let row4 = 0; row4 != userRow4; row4++){
    for (let spaces = userRow4 - 1; spaces > 0; spaces = spaces - 1){
        if (spaces == 1){
            document.write("* ")
        }else{
        document.write("  ");
        }
    }
    for(let collumn4 = 0; collumn4 != userCollumn4; collumn4++){
        document.write("*");
        }document.write("<br>");
}document.write("<br>");
document.write("<pre>");
