// 1. Написать скриптик, который сосчитает и выведет результат от возведения 2 в степень 10, начиная со степени 1
let i = 1
while(i <= 10){
    console.log(Math.pow(2,i))
    i++
}

// 1*. Преобразовать 1 задачу в функцию, принимающую на вход степень, в которую будет возводиться число 2
const expo = function(qq){
    for (y = 1; y <= qq; y++) {
        console.log(Math.pow(2,y))
    }
}
expo(4)

// 2. Написать скрипт, который выведет 5 строк в консоль таким образом, чтобы в первой строчке выводилось :), во второй :):) и так далее
// Пример в консоли:
// :)
// :):)
// :):):)
// :):):):)
// :):):):):)
let smile = ":)"
let result = ''
for (item_1 = 1; item_1 <= 5; item_1++){
    result+=smile
    console.log(result)
}

// 2*. Преобразовать 2 задачу в функцию, принимающую на вход строку, которая и будет выводиться в консоль (как в условии смайлик), а также количество строк для вывода 
// e.g. function printSmile(stroka, numberOfRows)
let result2 = ''
const printSmile = function(stroka, numberOfRows){
    for (it_1 = 1; it_1 <= numberOfRows; it_1++){
        result2+=stroka
        console.log(result2)
    }
}
printSmile('+-', 7)

// 3**.  Написать функцию, которая принимает на вход слово. Задача функции посчитать и вывести в консоль, сколько в слове гласных, и сколько согласных букв.
// e.g. function getWordStructure(word)
// В консоли: 
// Слово (word) состоит из  (число) гласных и (число) согласных букв
// Проверки: 'case', 'Case', 'Check-list'
const getWordStructure = function(word){
    // let vowel = 0;
    // const vowels_list = ["a", "u", "e", "o", "i"];
    // for (let char of word.toLowerCase()){
    //     if (vowels_list.includes(char)){
    //         vowel++;
    //     } 
    // }

    // let consonant = 0;
    // const consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
    // for (let char of word.toLowerCase()){
    //     if (consonant_list.includes(char)){
    //         consonant++;
    //     } 
    // }
    let vowel = word.match(/[ауоыиэяюёеAUEOI]/igm).length;
    let consonant = word.match(/[бвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZ]/igm).length;
    console.log('Слово', word, 'состоит из', vowel,'гласных и', consonant, 'согласных букв')    
}
getWordStructure('case')
getWordStructure('Case')
getWordStructure('Check-list')

// 4**. Написать функцию, которая проверяет, является ли слово палиндромом
// e.g. function isPalindrom(word)
// Проверки: 'abba', 'Abba'
const isPalindrom = function(word){
    let checkingPalindrome = word.toLowerCase().split('').reverse().join('');
    if (checkingPalindrome === word.toLowerCase()){
        console.log('Слово', word,'является палиндромом')
    } else {
        console.log('Слово', word,'не является палиндромом')    
    }
    
}
isPalindrom('abba')
isPalindrom('Abba')
isPalindrom('Abbacd')