#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(n => parseInt(n));
if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
