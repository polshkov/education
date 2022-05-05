console.log(true && true)
console.log(true && false)

console.log(true || true)
console.log(true || false)

//////
let item_1 = 5;
let item_2 = 100;
let item_3 = 50;
let item_4 = (item_3 < 40)? console.log("yes"): console.log("no");

if (item_1 > 3 && item_2 < 15 || item_3 !=30) {
    console.log("good")
} else {
    console.log("bad")
}

let item_5 = 1;

while (item_5 <= 10) {
    console.log(item_5 + " = today")
    item_5++
}

//////
let temperature = 0;

while (temperature <= 40) {
    if (temperature <= 17) {
        console.log('temperature - ', temperature, ' cold')
    } else if (temperature > 17 && temperature <= 28) {
        console.log('temperature - ', temperature, ' comfort')
    } else {
        console.log('temperature - ', temperature, ' hot')
    }
    temperature++
}

//////
