function iterator(traverse, obj, options) {
  return function reduce(stack, entity) {
    var base = obj ? obj[entity] : entity
      , name = options.name || entity;
    if (obj) options.name = entity;
    if (js(base)) {
      return stack.concat(init(
        base,
        'string' === is(name) ? name : '',
        options
      ));
    }
    if (Array.isArray(base)) {
      options.name = name;
      stack.push(traverse(base, options));
      return stack;
    }
    return stack.concat(traverse(base, options));
  };
}