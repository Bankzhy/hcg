function lowChain(_, array, save) {
  var chain = _.chain(array);
  _.functionsIn(chain).forEach(function (method) {
    chain[method] = _.flow(chain[method], function (arg) {
      var v = void 0;
      if (arg) {
        v = _.isFunction(arg.value) ? arg.value() : arg;
      }
      var s = save();
      if (s) return s.then(function () {
        return Promise.resolve(v);
      });
      return v;
    });
  });
  return chain;
}