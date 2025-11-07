#!/usr/bin/node
const args = process.argv;
const printMe = args[2];
if (printMe) {
  console.log(printMe);
} else {
  console.log('No argument');
}
