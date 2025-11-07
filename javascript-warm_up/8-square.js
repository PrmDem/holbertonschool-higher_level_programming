#!/usr/bin/node
const args = process.argv.slice(2);
const size = Number(args[0]);
let times = 0;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (times < size) {
    console.log('X'.repeat(size));
    times++;
  }
}
