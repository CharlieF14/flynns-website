//Question 1
let digitNo = Number(prompt("Please enter a number")); 
let digits = 0;
while(digitNo > 0){
    digitNo = Math.floor(digitNo / 10);
    digits++;
}
console.log(digits);

//Question 2 
let userInput = Number(prompt("Please input a number"));
let digit1 = 0;
let lastDigit = userInput % 10;;
while(userInput > 10){
    userInput = Math.floor(userInput / 10);
}
console.log(userInput);
console.log(lastDigit);

//Question 3
let userNo = Number(prompt("Please enter a number"));
while (userNo != 0){
switch(userNo % 10){
    case 1:
        console.log("one");
        break;
    case 2:
        console.log("two");
        break;
    case 3:
        console.log("three");
        break;
    case 4:
        console.log("four");
        break;
    case 5:
        console.log("five");
        break;
    case 6:
        console.log("six");
        break;
    case 7:
        console.log("seven");
        break;
    case 8:
        console.log("eight");
        break;
    case 9:
        console.log("nine");
        break;
    case 0:
        console.log("zero");
        break;
}
userNo = Math.floor(userNo / 10);
}

//Question 4
let num1 = Number(prompt("Enter a number"));
let num2 = Number(prompt("Enter another number"));
max = Math.max(num1, num2);
lcm = max;
if (lcm % num1 == 0){
    if(lcm % num2 == 0){
    console.log(lcm);
    }
    else{
        max = Math.max(lcm); 
    }
}else if(lcm % num2 == 0){
    if(lcm % num1 == 0){
        console.log(lcm);
    }else{
        max = Math.max(lcm);
    }
}

