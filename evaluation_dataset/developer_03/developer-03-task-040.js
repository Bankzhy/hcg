function off$$1(targetOrType, typeOrListener, listener) {
    if (!targetOrType || isValidEventType(targetOrType)) {
      off(this.eventBusEl_, targetOrType, typeOrListener);
    } else {
      var target = targetOrType;
      var type = typeOrListener;
      validateTarget(target);
      validateEventType(type);
      validateListener(listener);
      listener = bind(this, listener);
      this.off('dispose', listener);
      if (target.nodeName) {
        off(target, type, listener);
        off(target, 'dispose', listener);
      } else if (isEvented(target)) {
        target.off(type, listener);
        target.off('dispose', listener);
      }
    }
  }