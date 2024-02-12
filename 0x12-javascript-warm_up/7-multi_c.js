#!/usr/bin/node

const x = process.argv[2];
let count = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (count < x) {
  console.log('C is fun');
  count++;
}
