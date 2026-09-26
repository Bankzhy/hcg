function(user, identifier, comment, out, cb) {
    logger.info('compile system: ' + identifier);
    var systemId = _sr.findSystem(identifier);
    var system;
    if (!systemId) { logger.error(ERR_NOSYSID); return cb(new Error(ERR_NOSYSID)); }
    var repoPath = _sr.repoPath(systemId);
    _compiler.compile(systemId, repoPath, out, function(err, systems) {
      if (err) { return cb(err); }
      async.eachSeries(_.keys(systems), function(key, next) {
          system = systems[key];
          _sr.writeFile(system.id, key + '.json', JSON.stringify(system, null, 2), next);
        },
        function(err) {
          cb(err);
        });
    });
  }