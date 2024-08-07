#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 1) {
  const x = args.map(Number);
  let maxnumber = x[0];
  let secndmax;
  for (const i of x) {
    if (i >= maxnumber) {
      secndmax = maxnumber;
      maxnumber = i;
    }
  }
  console.log(secndmax);
} else {
  console.log(0);
}
