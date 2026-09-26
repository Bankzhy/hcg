function numberOfLeadingZeros(value) {
    if (value.equals(Long.ZERO)) {
      return 64;
    }
    let n = 1;
    let x = value.getHighBits();
    if (x === 0) {
      n += 32;
      x = value.getLowBits();
    }
    if (x >>> 16 === 0) {
      n += 16;
      x <<= 16;
    }
    if (x >>> 24 === 0) {
      n += 8;
      x <<= 8;
    }
    if (x >>> 28 === 0) {
      n += 4;
      x <<= 4;
    }
    if (x >>> 30 === 0) {
      n += 2;
      x <<= 2;
    }
    n -= x >>> 31;
    return n;
  }