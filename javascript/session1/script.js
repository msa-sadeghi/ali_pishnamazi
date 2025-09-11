// alert("hi")

// console.log("hi")

// var userCount = 4
// console.log(userCount)
// console.log(typeof userCount)

// var name = "sara"
// console.log(name)
// console.log(typeof name)


// var x = true
// console.log(typeof x)

// var x = prompt("enter a number: ")
// var y =  Number(x)
// console.log(typeof x)
// console.log(typeof y)

// var a = "12"
// var b = -a

// console.log(a)
// console.log(b)
// console.log(typeof a)
// console.log(typeof b)

// var z = "abcd"
// var u = Number(z)
// console.log(typeof u)
// console.log(u)

// var x1 = 12
// var x2 = String(x1)

// console.log(typeof x2)

// برنامه ای بنویسید که 2 عدد
//  از کاربر دریافت کرده و عملیات ضرب، تقسیم،
//  جمع و تفریق را روی آن ها پیاده سازی کنید

// "use strict"

// var x = 12

// var x = 12;
// var y = 5;
// console.log(x / y)
// console.log(Math.floor(x / y))

// var message = "hi"
// var name = "ali"

// console.log(message + " " + name)
// console.log(`${message / 4} ${name}\nHow are you?`)

// var message = `hek
// sdfsdf`


// var x = "salaam"
// var y = x / 4

// console.log(y)
// console.log(typeof y)

// var a = "2"
// console.log(2 / a)

// var a = 2
// var b = "2"

// console.log(a != b)
// console.log(a === b)

// var x1 = 12
// var x2 = 13

// if (x1 < x2) {
//     console.log("*");
//     console.log("-")
// }else if(x == y){
//     console.log("++")
// }else{

// }
// Number("12")
// عددی را از کاربر دریافت کرده
//  و زوج یا فرد بودن آن را به کاربر نمایش دهید

// if(isNaN("bababab")){

// }
// 'use strict'
// function isDec(num){
    
//     return typeof num === 'number' && !Number.isInteger(num)
// }

// var x = new isDec(12)
// console.log(x.num)
// console.log("blalalal")

// if (1 ==1){
//     if (2 == 2){

//     }
// }

// console.log(!isDec(12))
// سن کاربر را دریافت کنید.
// اگر سن کاربر کمتر از 18 بود،
//  به او پیغام "شما مجاز به ورود نیستید" را نمایش بدهید 
// و در غیر این صورت پیغام "ورود به پنل" را نمایش بدهید.



// دو عدد را از کاربر دریافت کرده
//  و عدد اول را به توان دومی برسانید و حاصل را نمایش دهید


// یک زمان را بر حسب دقیقه از کاربر دریافت کرده 
// و آن را به ساعت تبدیل کنید و سپس نمایش دهید


// از کاربر سن و جنسیت را دریافت کنید.
// در صورتی که جنسیت کاربر مونث بوده 
// یا سن کمتر از 18 را دارد، به اون خطا نمایش داده
// و در غیر این صورت به اون مجوز ورود به پنل را نمایش دهید.



// var x = 12
// var y = 2

// x * y === 24 ? console.log("yes") : console.log("no")




// var num1 = 3;
// var num2 = 4;
// var res = num1 * num2;
// switch(res){
//     case 8:
//     case 9:
//     case 10:
//         console.log(res)
//         break
//     case 11:
//         console.log(res)
//         break
//     case 12:
//         console.log(res)
//         break
//     default:
//         console.log("blala");
//         break

// }




// معدل کاربر را دریافت کرده و سپس سطح او را تعیین کنید

// A برای معدل 18 الی 20 سطح
// B برای معدل 15 الی 17 سطح
// C برای معدل 12 الی 14 سطح
// معدل کمتر از 12 مشروط میشه :(
// function addNumbers(x,y){
    //     return `${x} + ${y} = ${x + y}`
    // }
        
const addNumbers = function(x,y){
    return `${x} + ${y} = ${x + y}`
}
console.log(addNumbers(1,2))

// تابعی بنویسید که عددی را دریافت کرده
//  و زوج یا فرد بودن آن را نمایش دهد