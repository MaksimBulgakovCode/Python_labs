function changeElem(array, n) {
  return array.map(item => item * n);
}

let array = [1, 2, 3, 4];
let result = changeElem(array, 3);
console.log(result);