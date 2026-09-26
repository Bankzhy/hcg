function() {
    var trap = this.getTrap("isSealed");
    if (trap === undefined) {
      return Reflect.isSealed(this.target);
    }
    var result = trap.call(this.handler, this.target);
    result = !!result;
    var state = Object_isSealed(this.target);
    if (result !== state) {
      if (result) {
        throw new TypeError("cannot report unsealed object as sealed: "+
                             this.target);
      } else {
        throw new TypeError("cannot report sealed object as unsealed: "+
                             this.target);
      }
    }
    return state;
  }