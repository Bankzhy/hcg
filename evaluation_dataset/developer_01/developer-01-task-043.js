function(newProto) {
    var trap = this.getTrap("setPrototypeOf");
    if (trap === undefined) {
      return Reflect.setPrototypeOf(this.target, newProto);
    }
    var success = trap.call(this.handler, this.target, newProto);
    success = !!success;
    if (success && !Object_isExtensible(this.target)) {
      var actualProto = Object_getPrototypeOf(this.target);
      if (!sameValue(newProto, actualProto)) {
        throw new TypeError("prototype value does not match: " + this.target);
      }
    }
    return success;
  }