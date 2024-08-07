#!/usr/bin/node

const arg = process.argv?.slice(2);
if (Number(arg[0])) {
  const modarg = Math.floor(arg[0]);
  process.stdout.write(('c is fun\n').repeat(modarg));
} else {
  console.log('Missing number of occurrences');
}
