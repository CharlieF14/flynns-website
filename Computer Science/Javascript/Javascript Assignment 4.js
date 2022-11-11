/*Javascript Assignment 4*/

//Question 1
userChoice = Number(prompt("Chose a number between 1 and 3"));
let x = Math.floor(Math.random()*3)+1;
switch(x){
    case 1:
        x = "rock";
        break;
    case 2:
        x = "paper";
        break;
    case 3:
        x = "scissors";
        break;
}
switch(x){
    case "rock":
        if (userChoice == 1){
            console.log("A draw! The computer picked", x);
        }else if (userChoice == 2){
            console.log("You won! The computer picked", x);
        }else{
            console.log("You lost! The computer picked", x);
        }
        break;
    case "paper":
        if (userChoice == 1){
            console.log("You lost! The computer picked", x);
        }else if (userChoice == 2){
            console.log("A draw! The computer picked", x);
        }else{
            console.log("You won! The computer picked", x);
        }
        break;
    case "scissors":
        if (userChoice == 1){
            console.log("You won! The computer picked", x);
        }else if (userChoice == 2){
            console.log("You lost! The computer picked", x);
        }else{
            console.log("A draw! The computer picked", x);
        }
        break;
    }

//Question 2
userLvl = prompt("What level did you do?");
userGrade = prompt("What grade did you get?");

switch (userLvl){
    case "Higher":
        switch (userGrade){
            case "H1":
                console.log("You got 100 points.");
                break;
            case "H2":
                console.log("You got 88 points.");
                break;
            case "H3":
                console.log("You got 77 points.");
                break;
            case "H4":
                console.log("You got 66 points.");
                break;
            case "H5":
                console.log("You got 56 points.");
                break;
            case "H6":
                console.log("You got 46 points.");
                break;
            case "H7":
                console.log("You got 37 points.");
                break;
            case "H8":
                console.log("You got 0 points.");
                break;
        }
    break;
    case "Ordinary":
        switch (userGrade){
        case "O1":
            console.log("You got 56 points");
            break;
        case "O2":
            console.log("You got 46 points");
            break;
        case "O3":
            console.log("You got 37 points");
            break;
        case "O4":
            console.log("You got 28 points");
            break;
        case "O5":
            console.log("You got 20 points");
            break;
        case "O6":
            console.log("You got 12 points");
            break;
        case "O7":
            console.log("You got 0 points");
            break;
        case "O8":
            console.log("You got 0 points");
            break;
        }
    break;
}