function proxy(config) {
  function fn(key, val) {
    if (typeof val === 'string') {
      config.alias.apply(config, arguments);
      return config;
    }
    if (typeof key === 'string') {
      config.map.apply(config, arguments);
      return config;
    }
    if (!utils.isObject(key)) {
      throw new TypeError('expected key to be a string or object');
    }
    for (var prop in key) {
      fn(prop, key[prop]);
    }
    return config;
  }
  fn.__proto__ = config;
  return fn;
}