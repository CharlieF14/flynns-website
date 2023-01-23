// /* Functions Exercise */

// //Question 1
// // function sum(number1, number2)
// // {
// //     return number1 + number2;
// // }
// // ans = sum(6, 8);
// // document.write(ans);

// // document.write("<br/>");
// // document.write("<br/>");

// // //Question 2
// // function maths(number3, number4, operator)
// // {
// //     if(operator == "+"){
// //         return number3 + number4;
// //     }else if(operator == "-"){
// //         return number3 - number4;
// //     }else if(operator == "*"){
// //         return number3 * number4;
// //     }else{
// //         return number3 / number4;
// //     }
// // }
// // ans2 = maths(4, 7, "/");
// // document.write(ans2);

// // document.write("<br/>");
// // document.write("<br/>");

// //Question 3
// function palindrome(word)
// {
//     let count = 0;
//     for(i = 0; i<(Math.floor(word.legnth/2)); i++){
//         word[i] = word[i];
//         if(word[i] == word[word.legnth - i]){
//             return count++;
//         }else{
//             return;
//         }
//     }
//     if(count == (Math.floor(word.legnth/2))){
//         return true//, count;
//     }else{
//         return false//, count;
//     }
// }
// ans3 = palindrome("racecar");
// document.write(ans3);

// //Question 4
// let count1 = 0;
// let vow_count = 0;
// vowels("Hello")
// function vowels(string){
//     for(; count1 < string.length; count1++){
//     switch(string[count1]){
//         case "a":
//             case "e":
//                 case "i":
//                     case "o":
//                         case "u":
//                             vow_count++;
//                             break;
//         default:
//             break;
//     }
// }
// return vow_count;
// }
// ans4 = vowels("Hello");
// console.log(ans4);

// //Question 5
// let count2 = 0;
// let vow_count1 = 0;
// vowels2("Alexander")
// function vowels2(string1){
//     for(; count2 < string1.length; count2++){
//     switch(string1[count2]){
//         case "a":
//             case "e":
//                 case "i":
//                     case "o":
//                         case "u":
//                             case "A":
//                                 case "E":
//                                     case "I":
//                                         case "O":
//                                             case "U":
//                             vow_count1++;
//                             break;
//         default:
//             break;
//     }
// }
// return vow_count1;
// }
// ans5 = vowels2("Alexander");
// console.log(ans5);

// //Question 6
// let count3 = 0;
// let upp_count = 0;
// vowels3("HeLLo My NamE iS ChaRLiE")
// function vowels3(string2){
//     for(; count3 < string2.length; count3++){
//     switch(string2[count3]){
//         case "A":
//         case "B":
//         case "C":
//         case "D":
//         case "E":
//         case "F":
//         case "G":
//         case "H":
//         case "I":
//         case "J":
//         case "K":
//         case "L":
//         case "M":
//         case "N":
//         case "O":
//         case "P":
//         case "Q":
//         case "R":
//         case "S":
//         case "T":
//         case "U":
//         case "V":
//         case "W":
//         case "X":
//         case "Y":
//         case "Z":
//         upp_count++;
//         break;
//         default:
//             break;
//     }
// }
// return upp_count;
// }
// ans6 = vowels3("HeLLo My NamE iS ChaRLiE");
// console.log(ans6);

// //Question 7
// let count4 = 0;
// let num_count = 0;
// nums("Hello 377 2 m65 ik3")
// function nums(string3){
//     for(; count4 < string3.length; count4++){
//     switch(string3[count4]){
//         case "A":
//         case "B":
//         case "C":
//         case "D":
//         case "E":
//         case "F":
//         case "G":
//         case "H":
//         case "I":
//         case "J":
//         case "K":
//         case "L":
//         case "M":
//         case "N":
//         case "O":
//         case "P":
//         case "Q":
//         case "R":
//         case "S":
//         case "T":
//         case "U":
//         case "V":
//         case "W":
//         case "X":
//         case "Y":
//         case "Z":
//         case "a":
//         case "b":
//         case "c":
//         case "d":
//         case "e":
//         case "f":
//         case "g":
//         case "h":
//         case "i":
//         case "j":
//         case "k":
//         case "l":
//         case "m":
//         case "n":
//         case "o":
//         case "p":
//         case "q":
//         case "r":
//         case "s":
//         case "t":
//         case "u":
//         case "v":
//         case "w":
//         case "x":
//         case "y":
//         case "z":
//         case " ":
//         break;
//         default:
//             num_count++;
//             break;
//     }
// }
// return num_count;
// }
// ans7 = nums("Hello 377 2 m65 ik3");
// console.log(ans7);

// //Question 8
// numbors = [1,2,3,4,5];
// let mean_ = 0;
// mean(numbors);
// function mean(q8){
//     for (i=0; i<q8.length; i++){
//         mean_ = mean_ + q8[i];
//       }
//       return (mean_ / q8.length)/2;
// }
// ans8 = mean(numbors);
// console.log(ans8);

// //Question 9
// numbers = [3,5,3,4,8];
// q9_Array = [];
// //let mode_ = 0;
// mode(numbers);
// function mode(q9){
//     for (i=0; i<q9.length; i++){
//         q9[i] = q9[i];
//         if (!q9_Array.includes(q9[i])){
//             q9_Array.push(q9[i]);
//         }else if(q9_Array.includes(q9[i])){
//             q9[i];
//         }
//       }
//       return q9_Array;
// }
// ans9 = mode(numbers);
// console.log(ans9);

// //Question 9
// numbers = [3,5,3,4,8];
// q9_Array = [];
// //let mode_ = 0;
// mode(numbers);
// function mode(q9){
//     for (i=0; i<q9.length; i++){

//     }
// }

//Qiestion 10
// numbis = [1,8,3,6,9,4];        //1,3,4,6,8,9
// even1 = 0;
// even2 = 0;
// median(numbis);
// function median(q10){
//     q10.sort();
//     if(q10.length % 2 != 0){
//         return q10[Math.ceil(q10.length/2) -1]
//     }
//     else{
//         even1 = q10[(q10.length/2)-1];
//         even2 = q10[(q10.length/2)];
//         return (even1 + even2) / 2;
//     }
// }
// ans10 = median(numbis);
// console.log(ans10);

//Question 11
// numbers = [3,6,8,3,2,6,3];              //2,3,3,3,6,6,8
// q11_Array = [];
// frequency[numbers];
// function frequency(q11){
//     let count4 = 0;
//     q11.sort();

//     for (i=0; i<q11.length; i++){  
//     if(q11_Array.indexOf(i) == -1){
//     q11_Array.push(q11[i]);
//         count4 = 0;
//         for (j=0; j<q11.length; j++){
//             if(q11[i] == q11[j]){
//                 count4++;
//             }
//        }
//     }
//        console.log(q11_Array[i], "occurs", count4);
//     }
// }
// ans11 = frequency(numbers);

//Question 11
numbers = [3,6,8,3,2,6,3];              //2,3,3,3,6,6,8
q11_Array = [];
frequency[numbers];
function frequency(q11){
    let count4 = 0;
    let k = 0;
    //q11.sort();
    for (i=0; i<q11.length; i++){ 
        count4 = 0;
        console.log(q11_Array);
        //console.log(i); 
        if(!q11_Array.includes(q11[i])){
        q11_Array.push(q11[i]);
        k++;
        for (j=0; j<q11.length; j++){
            if(q11[i] == q11[j]){
                count4++;
            }
        }
    }
        
       console.log(q11_Array[i], "occurs", count4);
}
    }
ans11 = frequency(numbers);