#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}

module.exports = { add };
