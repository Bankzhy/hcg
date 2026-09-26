function(name) {
    "use strict";
    var trap = this.getTrap("hasOwn");
    if (trap === undefined) {
      return Reflect.hasOwn(this.target, name);
    }
    name = String(name);
    var res = trap.call(this.handler, this.target, name);
    res = !!res;
    if (res === false) {
      if (isSealed(name, this.target)) {
        throw new TypeError("cannot report existing non-configurable own "+
                            "property '"+name + "' as a non-existent own "+
                            "property");
      }
      if (!Object.isExtensible(this.target) &&
          isFixed(name, this.target)) {
          throw new TypeError("cannot report existing own property '"+name+
                              "' as non-existent on a non-extensible object");
      }
    } else {
      if (!Object.isExtensible(this.target)) {
        if (!isFixed(name, this.target)) {
          throw new TypeError("cannot report a new own property '"+
                              name + "' on a non-extensible object");
        }
      }
    }
    return res;
  }