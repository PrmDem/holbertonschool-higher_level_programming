#!/usr/bin/node
const args = process.argv.slice(2);
if (!args | args.length <= 1) {
  console.log('0');
} else {
  const argsAsInts = args.map(Number);
  function compareNumbers (a, b) {
    return a - b;
  }
  argsAsInts.sort(compareNumbers);
  console.log(argsAsInts[argsAsInts.length - 2]);
}
