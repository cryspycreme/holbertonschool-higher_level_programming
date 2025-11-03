#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

function factorial (a) {
  if (a <= 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

if (isNaN(num)) {
  console.log('1');
} else {
  console.log(factorial(num));
}
