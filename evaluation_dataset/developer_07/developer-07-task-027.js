function() {
    var trap = this.getTrap("freeze");
    if (trap === undefined) {
      return Reflect.freeze(this.target);
    }
    var success = trap.call(this.handler, this.target);
    success = !!success;
    if (success) {
      if (!Object_isFrozen(this.target)) {
        throw new TypeError("can't report non-frozen object as frozen: "+
                            this.target);
      }
    }
    return success;
  }