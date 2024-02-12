#!/usr/bin/node

const num = process.argv[2];
if (isNaN(Number(num))) {
  console.log('Not a number');
} else { console.log(`My number: ${Number(num)}`); }
