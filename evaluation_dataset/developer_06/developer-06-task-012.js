function TextTrackList() {
    var _this, _ret;
    var tracks = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
    classCallCheck(this, TextTrackList);
    var list = void 0;
    if (IS_IE8) {
      list = document.createElement('custom');
      for (var prop in TrackList.prototype) {
        if (prop !== 'constructor') {
          list[prop] = TrackList.prototype[prop];
        }
      }
      for (var _prop in TextTrackList.prototype) {
        if (_prop !== 'constructor') {
          list[_prop] = TextTrackList.prototype[_prop];
        }
      }
    }
    list = (_this = possibleConstructorReturn(this, _TrackList.call(this, tracks, list)), _this);
    return _ret = list, possibleConstructorReturn(_this, _ret);
  }