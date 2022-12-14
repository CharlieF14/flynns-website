/* Javascript Assignment 14 */

/*
Step 1 - Start
Step 2 - Ask the user to input a letter and store that in the variable letter
Step 3 - Use a switch statement to compare the letter to the vowels
Step 4 - If the users letter is equal to a vowel output that the letter is a vowel
Step 5 - If the user's letter is not a vowel it will output that it is a consonant
Step 6 - End
*/

let letter = prompt("Please input a letter");
switch(letter){
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        document.write("Your letter is a vowel");
        break;
    default:
        document.write("Your letter is a consonant");
}