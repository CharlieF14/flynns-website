/* Javascript Assingment 5 */

//Question 1
let userLetter = prompt("Please input a letter");
switch(userLetter){
    case "a":
        console.log("Your letter is a vowel");
        break;
    case "e":
        console.log("Your letter is a vowel");
        break;
    case "i":
        console.log("Your letter is a vowel");
        break;
    case "o":
        console.log("Your letter is a vowel");
        break;
    case "u":
        console.log("Your letter is a vowel");
        break;
    default:
        console.log("Your letter is a consonant");
}

//Question 2
let userNumber = Number(prompt("Please input any number"));
mod1 = userNumber % 5;
mod2 = userNumber % 11;
if (mod1 == 0  && mod2 == 0){
        console.log("Your number is divisible 5 and 11");
}else {
    console.log("Your number is not divisible by 11 and 5");
}

//Question 3
let userMonth = Number(prompt("Please enter a months number"));
switch (userMonth){
    case 9:
    case 4:
    case 6:
    case 11:
        console.log("The month you chose has 30 days");
        break;
    case 2:
        console.log("The month you have chosen has 28 days");
        break;
    default:
        console.log("The month you have chosen has 31 days");
        break;
        
}

//Question 4
let userTime = Number(prompt("Please input the hour in 24h clock"));
if (userTime <= 12 && userTime > -1){
    console.log("Your time is in the AM");
}else if (userTime > 12 && userTime <= 24) {
    console.log("Your time is in the PM");
}else{
    console.log("Invalid time");
}