/*Java Assignment 2*/

//Question 1 
let user_no = Number(prompt("Please enter a Number"));
user_no = user_no %= 2;
    if (user_no ==0)
        {
        console.log("Q1: Your Number is even");
    }
    else {
        console.log("Q1: Your Number is odd");
    }

//Question 2
let user_no2 = Number(prompt("Please enter a Number"));
let user_no3 = Number(prompt("Please enter another Number"));
if (user_no2 > user_no3){
    console.log("Q2: Number 1 is the bigger number");
}
else if (user_no2 < user_no3){
    console.log("Q2: Number 2 is the bigger number");
}
else{
    console.log("Q2: The numbers are Equal");
}

//Question 3
let user_no4 = Number(prompt("Please enter a Number"));
let user_no5 = Number(prompt("Please enter another Number"));
let user_no6 = Number(prompt("Please enter another Number"));
if (user_no4 > user_no5){
    if (user_no4 > user_no6){
    console.log("Q3: Number 1 is the bigger number");
    }
}
else if (user_no5 > user_no6){
    if (user_no5 > user_no6){
    console.log("Q3: Number 2 is the bigger number");
    }
}
else if (user_no6 > user_no5){
    if (user_no6 > user_no4){
    console.log("Q3: Number 3 is the bigger number");
    }
}
else{
    console.log("Q3: The numbers are Equal");
}

//Question 4
let user_no7 = Number(prompt("Please enter a Number"));
let user_no8 = Number(prompt("Please enter another Number"));
let user_no9 = Number(prompt("Please enter another Number"));
if (user_no7 == user_no8){
    if (user_no7 == user_no9){
        console.log("The Triangle is Equilateral");
    }
    else if (user_no7 != user_no9){
        console.log("The Triangle is Iscoceles");
    }
}
else if (user_no7 != user_no8){
    if (user_no7 == user_no9){
        console.log("The Triangle is Iscoceles");
    }
    else if (user_no8 == user_no9){
        console.log("The Triangle is Iscoceles");
    }
    else {
        console.log("The triangle is Scalene");
    }
}

//Question 5
let user_no10 = Number(prompt("Please enter the 1st Number"));
let user_no11 = Number(prompt("Please enter the 2nd Number"));
let user_choice = prompt("Please type what you would like to do");
if (user_choice == "add"){
    let x = user_no10 + user_no11;
    console.log(x);
}
else if (user_choice == "subtract"){
    let x = user_no10 - user_no11;
    console.log(x);
}
else if (user_choice == "multiply"){
    let x = user_no10 * user_no11;
    console.log(x);
}
else if (user_choice == "divide"){
    let x = user_no10 / user_no11;
    console.log(x);
}
else if (user_choice == "modulus"){
    let x = user_no10 % user_no11;
    console.log(x);
}
else {
    console.log(user_choice," Invalid Operator");
}