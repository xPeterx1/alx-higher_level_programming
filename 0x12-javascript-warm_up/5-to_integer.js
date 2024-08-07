#!/usr/bin/node

const arg = process.argv?.slice(2);

if (Number(arg[0])) {
  const modarg = Math.floor(arg[0]);
  console.log('My number: ' + modarg);
} else {
  console.log('Not a number');
}
