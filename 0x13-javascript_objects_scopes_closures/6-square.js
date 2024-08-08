#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (c) {
      this.index++;
      super.print();
      this.index--;
    } else {
      super.print();
    }
  }
}
module.exports = Square;
