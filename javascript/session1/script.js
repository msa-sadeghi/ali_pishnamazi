let a = 12

let b = a
b = 20
console.log(a)
console.log(b)

let person1 = {
    name: "ali",
    age: 20    
}

let person2 = person1
person1.age = 23
console.log(person1)
console.log(person2)

// یک سامانه فروش بلیط آنلاین پیاده سازی کنید

// به این صورت که مبدا سفر (استان) را از کاربر دریافت کرده 
// و سپس شهر های استان وارد شده را در کنسول نمایش دهید

// ساختار پروژه و ذخیره سازی اطلاعات بر عهده شما

var cities = {
    tehran: ['Tehran', 'Shahryar', 'rudehen', 'bumehen'],
    shiraz: ['shiraz', 'fars', 'jamshid', 'shiraz pars'],
    mashhad: ['Mashhad', 'Fariman', 'Guchan'],
    tabriz: ['Tabriz', 'Marand', 'Jolfa', 'Ahar'],
}

if('tehran' in cities){
    console.log(cities.tehran)
}

cities['tehran']