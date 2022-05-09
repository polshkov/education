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
//////

let gas = 1;

while (gas <= 10) {
    console.log(gas + " = цыкл while")
    gas++
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

for (let i = 0; i <= 10; i++){
    console.log(i, "= цыкл for")
}

for (let temp = 0; temp <= 40; temp++) {
    if (temp <= 17) {
        console.log('temperature - ', temp, ' cold')
    } else if (temp > 17 && temp <= 28) {
        console.log('temperature - ', temp, ' comfort')
    } else {
        console.log('temperature - ', temp, ' hot')
    }
}
//////

let names = [ 'Kate',
              'Pedro',
              'Roberto',
              'Igor',
              'Pam',
              'Andrew']

for (it_1 of names){
    console.log(it_1)
}
//////
