import './style.css';

// Count the number of ways you can reduce a deletable prime to a one digit number

const prime = (n) => {
  if (n === 2) return true;
  if (n % 2 === 0 || n <= 1) return false;

  for (let i = 3; i < Math.sqrt(n); i += 2) {
    if (n % i === 0) return false;
  }

  return true;
};

const splitNumberToDigits = (n) => n.toString().split('').map(Number);

const decomposeNumber = (n) => {
  const arr = [];
  const digits = splitNumberToDigits(n);
  for (let i = 0; i < digits.length; i += 1) {
    const before = digits.slice(0, i);
    const after = digits.slice(i + 1);
    arr.push(`${before.join('')}${after.join('')}`);
  }
  return arr.map(Number);
};

const countPossibilities = (n) => {
  if (splitNumberToDigits(n).length === 1 && prime(n)) {
    return 1;
  }

  const arrayPrime = decomposeNumber(n).filter(prime);
  if (arrayPrime.length === 0) {
    return 0;
  }

  return arrayPrime.reduce((acc, curr) => acc + countPossibilities(curr), 0);
};

const numbers = [537499093, 2147483059, 410256793, 567629137, 46216567629137];
console.log(numbers.map(countPossibilities));