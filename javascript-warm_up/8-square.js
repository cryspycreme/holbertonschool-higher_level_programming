#!/usr/bin/node

const size = process.argv[2];
const sizeInt = parseInt(size);

if (isNaN(sizeInt)) {
  console.log('Missing size');
}

for (let row = 0; row < size; row++) {
  let line = '';
  for (let col = 0; col < size; col++) {
    line += 'X';
  }
  console.log(line);
}
