function(name) {
    "use strict";
    var trap = this.getTrap("deleteProperty");
    if (trap === undefined) {
      return Reflect.deleteProperty(this.target, name);
    }
    name = String(name);
    var res = trap.call(this.handler, this.target, name);
    res = !!res;
    if (res === true) {
      if (isSealed(name, this.target)) {
        throw new TypeError("property '"+name+"' is non-configurable "+
                            "and can't be deleted");
      }
    }
    return res;
  }