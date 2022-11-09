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

//IF ELSE IF STATEMENT
/* Similar to the two control statements above:
This can test multiple different conditions,
if they all fail it will rin the else condition */
if(myage > 500){

  console.log("You are over 500 years old");

}

else if(myage < 500){

  console.log("You are less than 500 years old");

}

else{

  console.log("You are exactly 500 years old");

}



/*
Logical Operators
These test for true and false conditions
*/

/*
Logical AND (&&)
Returns true if both operands are true
*/
a1 = true;
let b1 = true;
console.log(a1 && b1);    //Will print true to the console
                          //as both a1 and b1 are true
b1 = false;
console.log(a1 && b1);    //Will print false to the console
                          //as a1 and b1 are noth BOTH true

let firstNumber = 10;
let secondNumber = 20;
if((firstNumber > 5) && (secondNumber > 15)){
  console.log("First is greater than 5 and the second than 15");
}else{
  console.log("One of the expressions failed the test");
}

/*
Logical OR (||) - If either A or B is true, it is all true
*/
a = true;
b = false;
console.log(a || b);

/*
Logical NOT (!) - Reverses the result. If true becomes false
If false becomes true
NOT true = false
NOT false = true
*/
console.log(!(a));

/*
Switch Statement
*/
let myVar = "A";
switch(myVar){
  case "A":
    console.log("You got an A");
    break;
  case "B":
    console.log("You got a B");
    break;
  default:
    console.log("Grade not recognised");
}


/*While Loops */

//While loops execute a statement
//as long as the expression is true
let count = 0;
while(count < 10){
    console.log(count);
    count = count + 1;    // or count++
}

// DO WHILE LOOP
// ALWAYS RUNS THE CODE
// AT LEAST ONCE
do{
    console.log(count);
    count++;
}while(count<20);


/* For Loops
for (initialization; test condition; increment statement){

  CODE IN HERE WILL RUN IF THE TEST CONDITION IS TRUE

}

INITIALIZATION: THIS STEP EXECUTES FIRST. IT ONLY EXECUTES
ONCE. YOU CAN DECLARE AND INITIALIZE A LOOP CONTROL VARIABLE
HERE. IT IS OPTIONAL, BUT YOU MUST PUT IN A SEMI-COLON AT THE
END ;

TEST CONDITION: IF THE TEST CONDITION IS TRUE THE BLOCK OF
CODE EXECUTES, OTHERWISE, IT DOES NOT.

INCREMENT STATEMENT: AFTERTHE BODY OF THE LOOP EXECUTES, 
CONTROL GOES TO THE INCREMENT STATEMENT WHICH ALLOWS YOU TO 
UPDATE ANY CONTROL VARIABLE VALUES THIS STATEMENT IS OPTIONAL
BUT A SEMI-COLON MUST BE AT THE END.
*/

//EXAMPLE

for(let i=0; i<2; i++){
  console.log("hello", i);
}
//WE GET THE SAME OUTPUT FROM THIS
let j=0;
for(;j<2;j++){
  console.log("hello", j);
}
//WE GET THE SAME OUTPUT FROM THIS
let m=0;
for(;m<2;){
  console.log("hello", m);
  m++;
}

//IFINITE LOOP - DONT RUN THIS
//for(;;){

//}

//BREAK STATEMENT
let d = 0;
document.write("Entering loop:<br>");
while(d<20){
  d = d + 1;
  if(d==5){
    break;                                  //Will stop at this command
  }
  document.write(d+"<br>");
}
document.write("Leaving Loop:<br>");

//CONTINUE STATEMENT
let d1 = 0;
document.write("Entering loop:<br>");
while(d<20){
  d1 = d1 + 1;
  if(d1==5){
    continue;                               //Will skip this one command
  }
  document.write(d1+"<br>");
}
document.write("Leaving Loop:<br>");