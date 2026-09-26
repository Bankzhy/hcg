function(){
      _a(oj.isDOM(this.el), this.typeName, 'constructor did not set this.el')
      _setInstanceOnElement(this.el, this)
      var u = oj.unionArguments(arguments),
        options = u.options,
        args = u.args
      if (this.__autonew__ && !options.__quiet__)
        this.emit()
      if (options.__quiet__ != null)
        delete options.__quiet__
      this.$el.addClass("oj-" + this.typeName)
      this.set(options)
      options = _clone(options)
      this.properties.forEach(function(v){return delete options[v]})
      this.addAttributes(options)
      return this._isConstructed = true
    }