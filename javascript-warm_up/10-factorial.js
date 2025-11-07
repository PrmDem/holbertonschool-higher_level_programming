#!/usr/bin/node
const args = process.argv.slice(2);
const int = Number(args[0]);
function factorial (int) {
  if (isNaN(parseInt(int, 10)) | int <= 1) {
    return 1;
  } else {
    return (int * factorial(int - 1));
  }
}
console.log(factorial(int));
