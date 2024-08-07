#!/usr/bin/node

const x = process.argv?.slice(2);
if (Number(x[0])) {
  const modarg = Math.floor(x[0]);
  process.stdout.write(('c is fun\n').repeat(modarg));
} else {
  console.log('Missing number of occurrences');
}
