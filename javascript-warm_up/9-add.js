#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
  process.exit(1);
}

function add (a, b) {
  return a + b;
}

const result = add(a, b);
console.log(result);
