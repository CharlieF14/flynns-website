console.log("Hello World")//this prints hello world in the console
console.log("This is some testing on Javascript")
console.log("All of these should display in the console after pressing F12")
//hello this is a comment, nobody will see this hehehehaw
//this is a single line comment
/*
this is a multi line comment
it can span 
over
multiple lines

*/
/*
There are two ways to declare variables in Javascript

var a = 10;

let a = 10;      (seen everywhere in the code)

const x = 20;       (cannot change the value of x later, program will crash if it is changed)

*/
let a = 10;
console.log(a)

let b = 2*4;
console.log(b)

const x = 20;
console.log(x)

let c = (4+7)*(5+3);
console.log(c)

//Variables in Javascript are case sensitive
let bob = 20;       //variables are case sensitive in javascript
let boB = 10;       //these variables are spelt whith just one capital letter difference
console.log(bob)
console.log(boB)

// Datatypes
/*
Numbers
Strings
Booleans
*/
let temp = 10   //Datatype number
let temp1 = "10"    //Datatype string
/*
All numbers in Javascript are floating point numbers
*/
/*
All varibale names in Javascript must begin with a
letter or an underscore "_". You can not use a reserved word
as a variable name.
*/


/*Arithmetic Operators*/

//Addition
console.log(5+2);
console.log("abc"+"def");

//Subtraction
console.log(5-2);

//Multiplication
console.log(5*2);

//Division
console.log(5/2);

//Exponent
console.log(5**2);

//Increment
let h = 11;         
console.log(h++);   //Will log h first
console.log(h);     //And then print the new value of h

let k = 3
console.log(++k);   //Will print the new value of k only

//Decrement
let l = 5;
console.log(k--);
console.log(k);

let i = 6;
console.log(--i);


/*Comparison opperators */

//Equals == 
console.log(5 == 3);    //Will return False
console.log(4 == 4);    //Will return True

//Not Equals !=
console.log(5 != 3);    //Will return True
console.log(4 != 4);    //Will return False

//Greater than >
console.log(5 > 4);     //Will return True
console.log(4 > 5);     //Will return False

//Less than <
console.log(4 < 5);     //Will retunr True
console.log(5 < 4);     //Will return False

//Greater than or equal to >=
console.log(5 >= 4);
console.log(4 >= 5);

//Less than or equal to <=
console.log(5 <= 4);
console.log(4 <= 50);


/*ASSIGNMENT OPERATORS*/

// Equals

//This is the simple assignment
let n = 12;

//Add and Assignment

n+=12; // This is the same as writing n = n +12
console.log(n);

// Subtract and Assignment

n-=4; //This is the same as writing n = n - 4
console.log(n);

//Multiply and assign

n*=5; // This is n = n * 5
console.log(n);

//Divide and Assignment

let p =4;

p/=2 ;// This is the same as writing p = p/2

//Modulus and Assignment

y %= 2; // This is y = y y%2

console.log(y);


//CONDITIONAL OPERATOR ?:

/* The conditional operator evaluates an expression for true or false.

If true , it executes the first statement. Otherwise it executes

the second statement */

let first = 10;
let second = 12;
console.log(first>second?"True":"False");

// first>second? = Test condition
// Will print "False"

//TYPEOF OPERATOR
let myString = "Hello"
console.log(typeof(myString));  

let myNumber = 12
console.log(typeof(myNumber));  

//USER INPUT
/* The prompt() function is used to take input from the user.
The default datatype for input is string. To convert the input to
a number, wrap the prompt in a NUMBER() function call */

let mySecondString = prompt("Enter something");
console.log(mySecondString);
let mySecondNumber = Number(prompt("Enter a number"));
console.log(mySecondNumber);

//IF STATEMENT
/*The if statement is a control statement which executes if the
test condition evaluates to true */
let myage = 400
if(myage

   > 500){

  console.log("You are over 500 years old");

}