class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.index = 0;
      this.array = ['X', 'C'];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(this.array[this.index]);
      }
      console.log('');
    }
  }
}
module.exports = Rectangle;
