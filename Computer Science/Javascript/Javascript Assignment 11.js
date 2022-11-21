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
document.write("Question 2:");
document.write("<br>");
document.write(question1_Array);
document.write("<br>");
document.write("<br>");

//Question 3
document.write("Question 3:");
document.write("<br>");
for(let cashew = 0; cashew < question1_Array.length; cashew++){
    question1_Array[cashew] = question1_Array[cashew];
    if(question1_Array[cashew]<0){
        document.write(question1_Array[cashew]);
        document.write("<br>");
    }
}document.write("<br>");

//Question 4
document.write("Question 4:");
document.write("<br>");
document.write(question1_Array[0]+question1_Array[1]+question1_Array[2]+question1_Array[3]+question1_Array[4]+question1_Array[5]+question1_Array[6]);
document.write("<br>");
document.write("<br>");

//Question 5
document.write("Question 5");
document.write("<br>");
let q5 = 0;
let q5_2 = 0;
for(let pistaccio = 0; pistaccio < question1_Array.length; pistaccio++){
    question1_Array[pistaccio] = question1_Array[pistaccio];
    if(question1_Array[pistaccio] > q5){
        q5 = question1_Array[pistaccio];
    }
    else if(question1_Array[pistaccio]< q5_2){
        q5_2 = question1_Array[pistaccio];
    }
}
document.write(q5);
document.write("<br>");
document.write(q5_2);
document.write("<br>");
document.write("<br>");

//Question 6
document.write("Question 6");
document.write("<br>");
let q6 = 0;
for(let peacan = 0; peacan < question1_Array.length; peacan++){
    question1_Array[peacan] = question1_Array[peacan];
    if(question1_Array[peacan] != q5 && question1_Array[peacan] > q6){
        q6 = question1_Array[peacan];  
    }
}document.write(q6);
document.write("<br>");
document.write("<br>");

//Question 7
document.write("Question 7");
document.write("<br>");
let odd = 0;
let even = 0;
for(let peanut = 0; peanut < question1_Array.length; peanut++){
    question1_Array[peanut] = question1_Array[peanut];
    if(question1_Array[peanut] % 2 == 0){
        even++;
    }
    else if(question1_Array[peanut] % 2 != 0){
        odd++;
    }
}
document.write("There are ", odd, " odd numbers");
document.write("<br>");
document.write("There are ", even, " even numbers");
document.write("<br>");
document.write("<br>");

//Question 8
document.write("Question 8");
document.write("<br>");
let q8 = 0;
let array2 = [];
for(let walnut = 0; walnut < question1_Array.length; walnut++){
    question1_Array[walnut] = question1_Array[walnut];
    array2.push(question1_Array[walnut]);
}
document.write(array2);
document.write("<br>");
document.write("<br>");

//Question 9
document.write("Question 9");
document.write("<br>");
question1_Array.push(64);
document.write(question1_Array);
document.write("<br>");
document.write("<br>");

//Question 10
document.write("Question 10");
document.write("<br>");
question1_Array.pop();
document.write(question1_Array);
document.write("<br>");
document.write("<br>");