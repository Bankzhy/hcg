function (currDeps, loc) {
      loc.deps = loc.deps || [];
      var covered = [];
      currDeps.forEach(function (obj) {
        if (covered.indexOf(obj.path) < 0) {
          covered.push(obj.path);
          var key = obj.name
            , isRelative = (['\\', '/', '.'].indexOf(key[0]) >= 0)
            , notCovered = notCoveredInArray(loc.deps, key)
            , isRecorded = (!isRelative || opts.showLocal) && notCovered
            , res = isRecorded ? { name: key } : loc;
          if (isRecorded) {
            res.path = obj.path;
            loc.deps.push(res);
          }
          traverse(lookup[obj.path] || [], res);
        }
      });
    }