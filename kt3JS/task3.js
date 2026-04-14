function sumElems(array) {
  return array.reduce((sum, item) => {
    let num = Number(item);
    if (!isNaN(num)) {
      return sum + num;
    }
    return sum;
  }, 0);
}

let array = ['10', 'Строка', '5g', '15', '05'];
let result = sumElems(array);
console.log(result);