/* Javascript Assignment 9 */

//Question 1
const number = prompt("Enter a number");
const numberOfDigits = number.length;
let sum = 0;
let variable1 = number;
while (variable1 > 0) {
    let remainder = variable1 % 10;
    sum += remainder ** numberOfDigits;
    variable1 = parseInt(variable1 / 10);
}
if (sum == number) {
    console.log(number,"is an Armstrong number");
}
else {
    console.log(number, "is not an Armstrong number.");
}

//Question 2
let userInput = Number(prompt("Please input another number"));
let Input = userInput;
let factorial = userInput;
let ans = 1;
let total = 0;
while(userInput > 0){
    Input = userInput % 10;
    userInput = Math.floor(userInput / 10);
for(let n1=Input; n1>0; n1=n1-1){
    ans = ans * n1;
    console.log(ans);
}
total = total + ans;
ans = 1;
}
if (total == factorial){
    console.log(factorial, "is a strong number");
}else{
    console.log(factorial, "is not a strong number");
}

//Question 3
let userNo = Number(prompt("Please enter a number"));
while (userNo != 0){
switch(userNo % 10){
    case 1:
        console.log("1");
        break;
    case 2:
        console.log("2");
        break;
    case 3:
        console.log("3");
        break;
    case 4:
        console.log("4");
        break;
    case 5:
        console.log("5");
        break;
    case 6:
        console.log("6");
        break;
    case 7:
        console.log("7");
        break;
    case 8:
        console.log("8");
        break;
    case 9:
        console.log("9");
        break;
    case 0:
        console.log("0");
        break;
}
userNo = Math.floor(userNo / 10);
}