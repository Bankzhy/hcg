function(handler, options) {
  assert(handler instanceof Function, "A handler must be provided");
  assert(options,                     "options required");
  assert(options.drain,               "options.drain is required");
  assert(options.component,           "options.component is required");
  var reporter = series.HandlerReports.reporter(options.drain);
  return function(message) {
    var point = {
      component:      options.component,
      duration:       undefined,
      exchange:       message.exchange || '',
      redelivered:    (message.redelivered ? 'true' : 'false'),
      error:          'false'
    };
    var start = process.hrtime();
    return Promise.resolve(handler(message)).then(function() {
      var d = process.hrtime(start);
      point.duration = d[0] * 1000 + (d[1] / 1000000);
      reporter(point);
    }, function(err) {
      var d = process.hrtime(start);
      point.duration = d[0] * 1000 + (d[1] / 1000000);
      point.error = 'true';
      reporter(point);
      throw err;
    });
  };
}