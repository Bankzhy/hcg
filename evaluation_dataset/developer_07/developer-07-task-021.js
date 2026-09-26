function mapperDeleteSuccess() {
  var _this2 = this;
  _id_map2.default.delete(this);
  this.isBusy = false;
  this.sourceState = DELETED;
  this._clearErrors();
  var _loop = function _loop(name) {
    var desc = _this2.associations[name];
    if (!desc.inverse) {
      return "continue";
    }
    if (desc.type === 'hasOne') {
      var m = void 0;
      if (m = _this2[name]) {
        m._inverseRemoved(desc.inverse, _this2);
      }
    } else if (desc.type === 'hasMany') {
      _this2[name].slice(0).forEach(function (m) {
        m._inverseRemoved(desc.inverse, _this2);
      });
    }
  };
  for (var name in this.associations) {
    var _ret = _loop(name);
    if (_ret === "continue") continue;
  }
}