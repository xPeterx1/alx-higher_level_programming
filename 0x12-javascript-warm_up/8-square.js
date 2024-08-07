#!/usr/bin/node

const x = process.argv?.slice(2);
if (Number(x[0])) {
  const modarg = Math.floor(x[0]);
  for (let i = 0; i < modarg; i++) {
    for (let j = 0; j < modarg; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
