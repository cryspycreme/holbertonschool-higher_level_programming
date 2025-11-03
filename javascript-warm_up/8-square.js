#!/usr/bin/node

const size = process.argv[2];
const sizeInt = parseInt(size);

if (isNaN(sizeInt)) {
  console.log('Missing size');
}

// let i = 0;
// while (i < size) {
//     console.log('X')
//     let j = 0;
//     while (j < size) {
//         console.log('X')
//         j++;
//     }
//     i++;
// }

for (let row = 0; row < size; row++) {
  let line = '';
  for (let col = 0; col < size; col++) {
    line += 'X';
  }
  console.log(line);
}
