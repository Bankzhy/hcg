function read(path, options, callback) {
  var str = readCache[path];
  var cached = options.cache && str && ('string' === typeof str);
  if (cached) {
    return callback(null, str);
  }
  fs.readFile(path, 'utf8', function (err, str) {
    if (err) {
      return callback(err);
    }
    str = str.replace(/^\uFEFF/, '');
    if (options.cache) {readCache[path] = str;}
    callback(null, str);
  });
}