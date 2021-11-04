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

const splitNumberToDigits = (n) =>  n.toString().split('').map(Number);
const decomposeNumber = (n) => {
  const arr = [];
  let digits = splitNumberToDigits(n);
   for(let i=0; i<digits.length; i++) {
     const before = digits.slice(0, i);
     const after = digits.slice(i+1);
     arr.push(`${before.join('')}${after.join('')}`);
   }
   return arr.map(Number);
}

console.log(decomposeNumber(4567));

let count = 0;

// console.log(prime(412567));