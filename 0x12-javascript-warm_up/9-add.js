#!/usr/bin/node

function add (a, b) {
  return Number(a) + Number(b);
}
const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
