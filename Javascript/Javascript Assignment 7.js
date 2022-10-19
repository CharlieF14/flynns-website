/* Javascript Assignment 7 */

//Question 1
let userNumber = Number(prompt("Please enter a number"));
for(let n = 1;n<=userNumber;n=n+2){
    console.log(n);
}

//Question 2
let factorial = Number(prompt("Please enter a number to be factorialed")); 
let ans = 0;
for(let n1=factorial-1; n1>0; n1=n1-1){
    ans = factorial * n1;
    factorial = ans;
}
console.log(ans);

//Question 3
let theNumber = 12345678;
let guessAmount = 3;
for(let guessCounter=1; guessCounter<=4; guessCounter++){
    let userGuess = Number(prompt("Please enter your guess of 8 digits"));
    
    if (userGuess != theNumber){
        console.log("Wrong Guess", guessAmount, "Guesses Remaining")
        guessAmount = guessAmount - 1;
    }else if (userGuess == theNumber){
        console.log("Congratulations You Guessed Correctly")
        break;
    }
}

//Quesiton 4
let userNumber1 = Number(prompt("Please enter a number to have all numbers below it be added to it")); 
let ans1 = 0;
for(let n2=userNumber1-1; n2>0; n2=n2-1){
    ans1 = userNumber1 + n2;
    userNumber1 = ans1;
}
console.log(ans1);