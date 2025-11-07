#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const value = Number(firstArg);
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(value, 10));
}
