// var x = 0;
// var y = ++x;
// console.log(y)
// console.log(x)

// for(let i = 0; i < 3; i++){
//     console.log(`${i}- hi`)
// }

// var name = 'nikan';
// for(let i = 0; i < name.length; i++){
//     console.log(`${name[i]}`)
// }

// اعداد زوج بین 0 تا 100 را در کنسول چاپ کنید


// فرض کنید یک وب سایت فروشگاهی دارید
//  که کاربر 5 محصول از فروشگاه را انتخاب کرده است

// قیمت 5 محصول را از کاربر گرفته
//  و مجموع مبلغ کل سبد خرید رو نمایش دهید


// عددی را از کاربر دریافت کرده و سپس مجموع رقم های آن را محاسبه کنید.

// :به عنوان مثال برای عدد 142 به صورت زیر محاسبه می شود

// 1 + 4 + 2 = 7

var x = 0
var a;
var y = true;
for(var i = 0; i < 5; i++){
    y = true
        for(var j = 0; y == true; j++){
            a = +prompt("enter a number")
            if (!isNaN(a)){
                y = false
            }
        }
         
         x += a

}
console.log(x)