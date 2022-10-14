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

//Question 5
let digitNo = Number(prompt("Please enter a number")); 
let digits = 0;
while(digitNo > 0){
    digitNo = Math.floor(digitNo / 10);
    digits++;
}
console.log(digits);

//Question 6
let userInput = Number(prompt("Please input a number for which the digits will be added"));
let digit = 0;
let Input = userInput ;
while(userInput > 0){
    Input = userInput % 10;
    userInput = Math.floor(userInput / 10);
    digit = digit + Input;
}
console.log(digit);

