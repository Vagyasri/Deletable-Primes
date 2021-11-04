import './style.css';

// Count the number of ways you can reduce a deletable prime to a one digit number

const prime = (n) => {
  if (n === 2) return true;
  if (n % 2 === 0 || n <= 1) return false;

  for (let i = 3; i < Math.sqrt(n); i += 2) {
    if (n % i === 0) return false;
  }

  return true;
}

let num = 412567;
var digits = num.toString().split('');
var realDigits = digits.map(Number);

console.log(realDigits);
let count = 0;

// console.log(prime(412567));