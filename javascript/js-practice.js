function greet(person){
	if(person=={ name : 'amy'}){
		return 'hey amy'
	}else{
		return 'hey arnold'
	}
}

console.log(greet({name: 'amy'}))
//these two objects has the same properties and values 
//but are still two different obnjects in memory

//FIX:

function greet(person){
	if(person.name === 'amy'){
		return 'hey amy'
	}
	return 'hey arnold'
}
console.log(greet({name:'amy'}))

// for(var i = 0; i < 4; i++){
// 	setTimeout(()=> console.log(i),0)
// }
// //four instances of setTimeout
//  //share the same instance of i

//  //FIX:
//  //change var to let 
// for(let i = 0; i < 4; i++){
// 	setTimeout(()=> console.log(i),0)
// }

// let dog = {
// 	name: 'doggo'
// 	sayName(){
// 		console.log(this.name)
// 	}
// }

// let sayName = dog.sayName
// dog.sayName
//doesnt recongize sayName on dog object

//FIX

class Dog {
	constructor(){
		this.name ='doggo'
	}
	sayName (){
		console.log(this.name)
	}
	bark(){
		console.log(this.name + 'says woof')
	}
}

let fido = new Dog('fido')
fido.bark()

function loopToFive(){
    for(var i=0; i < 5; i++){
        console.log(i);
    }
}
// loopToFive()

function displayEvenNumbers(){
    var numbers = [1,2,3,4,5,6,7,8];
    var evenNumbers = [];
    for(let i=0; i < numbers.length; i++){
        if(numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i])
        }
    }
    return evenNumbers;
}
console.log(displayEvenNumbers()); // should return [2,4,6,8] 
