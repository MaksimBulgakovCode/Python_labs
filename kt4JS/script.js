//===================================================================== 1
/*
let obj = {       
    price1: 100, 
    price2: 150, 
    price3: 200, 
    price4: 100, 
    price5: 150 
};

const sum = Object.values(obj).reduce((acc, val) => acc + val, 0);
console.log(sum); // 700
*/
//===================================================================== 2
/*
let array = [                   
  {id: 1, name: 'apple'},
  {id: 2, name: 'watermelon'},
  {id: 3, name: 'qiwi'},
  {id: 4, name: 'lemon'}
];

const result = array.map(obj => Object.values(obj));
console.log(result);
*/
//===================================================================== 3
/*
function logString(...args) {                  
  console.log(args.join(' ') + ' ');
}

logString("Hello", "my", "world!"); 
*/ 
//===================================================================== 4
/*
function checkObj(obj) {
  return 'particle' in obj;
}

console.log(checkObj({id: 1, particle: 10}));
console.log(checkObj({id: 2, name: "tag"}));  
*/
//===================================================================== 5
/*
function generateArray(array) {
  for (let i = 0; i < array.length; i++) {
    if (!Array.isArray(array[i]) && typeof array[i] === 'object') {
      array[i] = Object.values(array[i]);
    }
  }
  return array;
}

let array = [[1], {id: 40}, [100], [300], {part: 10}];
console.log(generateArray(array));
// [[1], [40], [100], [300], [10]]
*/
//===================================================================== 6
/*
let users = [
  {id: 1, name: 'Alex', lastname: 'Wilyam', age: 20},
  {id: 2, name: 'Steven', lastname: 'King', age: 34}
];

function addUser(name, lastname, age) {
  users.push({ id: users.length + 1, name, lastname, age });
}

function updateUser(id, name, lastname, age) {
  const user = users.find(u => u.id === id);
  if (user) Object.assign(user, { name, lastname, age });
}

function deleteUser(id) {
  users = users.filter(u => u.id !== id);
}

addUser('Anna', 'Smith', 25);
console.log(users); 

updateUser(1, 'Alexey', 'Wilyam', 21);
console.log(users); 

deleteUser(2);
console.log(users); 
*/
//===================================================================== 7
/*
const products = [
  {id: 1, title: 'велосипед', price: 45000, count: 3, marks: [5,5,5]},
  {id: 2, title: 'самокат',   price: 850,   count: 15, marks: [4,3,5]},
  {id: 3, title: 'ролики',    price: 1200,  count: 8,  marks: [5,4,4]},
  {id: 4, title: 'скейт',     price: 800,   count: 12, marks: [3,4,4]},
  {id: 5, title: 'моноколесо',price: 900,   count: 5,  marks: [5,5,4]},
];

const task1 = products.filter(p => p.count > 10);
console.log(task1);

const task2 = products.find(p => p.price >= 800 && p.price <= 900);
console.log(task2);

const task3 = [...products].sort((a, b) => b.price - a.price);
console.log(task3);

const task4 = products.reduce((acc, p) => acc + p.price * p.count, 0);
console.log(task4);

const task5 = products
  .map(p => ({ ...p, marks_total: p.marks.reduce((a, b) => a + b, 0) }))
  .sort((a, b) => b.marks_total - a.marks_total);
console.log(task5);
*/
//===================================================================== 8
/*
class Email {
  constructor(email) {
    this.email = email;
  }

  get isValid() {
    const [login, domain] = this.email.split('@');
    const zone = domain?.split('.').pop();
    const forbidden = /[*#$%^]/;
    return !forbidden.test(login) && zone?.length <= 3;
  }

  set setEmail([login, domain, zone]) {
    this.email = `${login}@${domain}.${zone}`;
  }
}

const mail1 = new Email('example@ex.com');
console.log(mail1.isValid); 

const mail2 = new Email('ex$ample@gmail.com');
console.log(mail2.isValid); 

mail1.setEmail = ['newEmail', 'gmail', 'com'];
console.log(mail1.email); 
*/