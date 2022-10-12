/*Javascript Assignment 6*/

//Question 1
let count = 1;
while(count <= 10){
    console.log(count);
    count++;
}

//Question 2
let count1 = 2
do{
    console.log(count1);
    count1 = count1 + 2;
}while(count1<=100);

//Question 3 
let userNo = Number(prompt("Please input a number"));
let userNo2 = Number(prompt("Please input a second number"));
let botNo = userNo;
let power = 1;
while(power != userNo2){
    power++;
    userNo = botNo * userNo;
}
console.log(userNo);

//Question 4
let userRow = Number(prompt("How many rows do you want?"));
let row = 0;
let star = "*";
let logufdasgogeshgd = star;
do{
    row++;
    console.log(star);
    star = star + logufdasgogeshgd;
    
}while(row != userRow);