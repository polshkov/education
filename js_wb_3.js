function yolochka1(item_1, item_2){

    let mass = 'Hello!!'
    console.log(mass + item_1 + item_2)
}
yolochka1(11,22)
////// - стрелочные функции
let t1 = 10
let t2 = 20
let t3 = 30
let t4 = 40

let f1 = (t1 > t2) ?
    (tt1, tt2) => console.log('order = ', tt1 + tt2) :
    (tt1, tt2) => console.log('order = ', tt1 - tt2) ;
f1(t4,t3)

function yolo4ka2(){};

yolo4ka2.prototype.fast = function(){
    console.log('Fast!')
}

yolo4ka2.prototype.green = function(sun, co2){
    console.log('Green ==', sun, ' + ', co2)
}

yolo4ka2.prototype.shishki = function(){
    console.log('shishki == yolki')
}

let forest = new yolo4ka2()

forest.fast()
forest.green(5700, 50)
forest.shishki()