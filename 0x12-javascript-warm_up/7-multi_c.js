#!/usr/bin/node

const x = process.argv?.slice(2);
if (Number(x[0])) {
  const modarg = Math.floor(x[0]);
  for (let i = 0; i < modarg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
