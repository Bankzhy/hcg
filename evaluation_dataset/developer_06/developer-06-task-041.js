function() {
    if (this.isFrozen) { throw new Ember.Error(Ember.FROZEN_ERROR); }
    var len = get(this, 'length');
    if (len === 0) { return this; }
    var guid;
    this.enumerableContentWillChange(len, 0);
    Ember.propertyWillChange(this, 'firstObject');
    Ember.propertyWillChange(this, 'lastObject');
    for (var i=0; i < len; i++) {
      guid = guidFor(this[i]);
      delete this[guid];
      delete this[i];
    }
    set(this, 'length', 0);
    Ember.propertyDidChange(this, 'firstObject');
    Ember.propertyDidChange(this, 'lastObject');
    this.enumerableContentDidChange(len, 0);
    return this;
  }