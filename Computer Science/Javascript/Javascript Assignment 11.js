/* Javascript Assignment 11 */

//Question 1
let question1_Array = [];
question1_Array[0] = 1;
question1_Array[1] = -5;
question1_Array[2] = 6;
question1_Array[3] = -12;
question1_Array[4] = 9;
question1_Array[5] = -23;
question1_Array[6] = 45;

//Question 2
document.write(question1_Array);
document.write("<br>");
document.write("<br>");

//Question 3
for(let cashew = 0; cashew < 7; cashew++){
    question1_Array[cashew] = question1_Array[cashew];
    if(question1_Array[cashew]<0){
        document.write(question1_Array[cashew]);
        document.write("<br>");
    }
}document.write("<br>");

//Question 4
document.write(question1_Array[0]+question1_Array[1]+question1_Array[2]+question1_Array[3]+question1_Array[4]+question1_Array[5]+question1_Array[6]);
document.write("<br>");
document.write("<br>");

//Question 5
document.write(Math.max(...question1_Array));
document.write("<br>");
document.write(Math.min(...question1_Array));
document.write("<br>");
document.write("<br>");

//Question 6
question1_Array.pop(Math.max(...question1_Array));
document.write(Math.max(...question1_Array));
document.write("<br>");

//Question 7
for(let peanut = 0; peanut < 7; peanut++){
    question1_Array[peanut] = question1_Array[peanut];
    if(question1_Array[peanut]<0){
        document.write(question1_Array[peanut]);
        document.write("<br>");
    }
}document.write("<br>");
for(let cashew = 0; cashew < 7; cashew++){
    question1_Array[cashew] = question1_Array[cashew];
    if(question1_Array[cashew]<0){
        document.write(question1_Array[cashew]);
        document.write("<br>");
    }
}document.write("<br>");