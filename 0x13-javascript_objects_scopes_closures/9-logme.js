#!/usr/bin/node
exports.logMe = (function () {
  let counter = 0;
  function printable (item) {
    console.log(counter + ': ' + item);
    counter++;
  }
  return printable;
}());
