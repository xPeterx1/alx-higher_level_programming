#!/usr/bin/node
exports.logMe = function (item) {
  let counter = 0;
  function printable (item) {
    console.log(counter + ': ' + item);
    counter++;
  }
  return printable(item);
};
