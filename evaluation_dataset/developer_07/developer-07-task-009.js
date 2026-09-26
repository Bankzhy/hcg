function(buffer, attributeBindings) {
    var attributeValue,
        unspecifiedAttributeBindings = this._unspecifiedAttributeBindings = this._unspecifiedAttributeBindings || {};
    a_forEach(attributeBindings, function(binding) {
      var split = binding.split(':'),
          property = split[0],
          attributeName = split[1] || property;
      if (property in this) {
        this._setupAttributeBindingObservation(property, attributeName);
        attributeValue = get(this, property);
        Ember.View.applyAttributeBindings(buffer, attributeName, attributeValue);
      } else {
        unspecifiedAttributeBindings[property] = attributeName;
      }
    }, this);
    this.setUnknownProperty = this._setUnknownProperty;
  }