function _attributesFromObject(obj){
    if (!oj.isPlainObject(obj))
      return obj
    var k, v, ix,
      out = '',
      space = '',
      attrs = _keys(obj).sort()
    for (ix = 0; ix < attrs.length; ix++){
      k = attrs[ix]
      v = obj[k]
      if (v === true)
        out += "" + space + k
      else
        out += "" + space + k + "=\"" + v + "\""
      space = ' '
    }
    return out;
  }