#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const occur = Number(firstArg);
if (isNaN(occur)) {
  console.log('Missing number of occurrences');
} else {
  for (let start = 0; start < occur; start++) {
    console.log('C is fun');
  }
}
