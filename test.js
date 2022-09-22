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
console.log(4 != 4);    //Will retunr False

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