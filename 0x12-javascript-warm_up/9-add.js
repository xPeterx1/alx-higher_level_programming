#!/usr/bin/node
const args = process.argv?.slice(2);

function add (x, y) {
  const sum = Number(x) + Number(y);
  return sum;
}

console.log(add(args[0], args[1]));
