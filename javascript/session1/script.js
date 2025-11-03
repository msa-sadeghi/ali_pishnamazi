// var userBasket = [
// 	{id: 1, name: 'laptop', price: 5000000},
// 	{id: 2, name: 'phone', price: 3000000},
// 	{id: 3, name: 'milk', price: 35000},
// 	{id: 4, name: 'water', price: 6000},
// 	{id: 5, name: 'coolpad', price: 400000},
// 	{id: 6, name: 'pencil', price: 9000},
// ]

// let filteredProducts = userBasket.filter(function(product){
//   return product.price < 10000
// })

// let postCost = filteredProducts.length * 100
// let total = 0

// userBasket.forEach(function(p){
//   total += p.price
// })
// total += postCost

// console.log(total)

// let scores = [19, 29, 29, 67]
// console.log(scores.indexOf(29))
// console.log(scores.lastIndexOf(29))
// console.log(scores.findIndex(function(n){
//   return n == 29
// }))

// // console.log(scores.reverse())

// scores.sort((a,b) => a-b)
// console.log(scores)




// let add = (a,b) => {return a + b}
// console.log(add(1,2))

let m = "gig"
console.log(m.split(''))

var todosArray = [
    { id: 1, title: 'learn js', isDoing: false },
    { id: 2, title: 'make footer', isDoing: true },
    { id: 3, title: 'design', isDoing: false },
    { id: 4, title: 'vue js', isDoing: false },
]

var userMenu = prompt('Choose one of them: \n 1. Add Todo \n 2. Remove Todo \n 3. Do Todo')
