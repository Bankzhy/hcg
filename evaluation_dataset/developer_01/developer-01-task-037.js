function(systemId, revisionId, target, cb) {
    if (revisionId === EDITS) {
      _getOnDiskVersion(systemId, revisionId, target, cb);
    }
    else {
      findRevision(systemId, revisionId, function(err, rev) {
        if (err) { return cb(err); }
        if (rev === EDITS) {
          _getOnDiskVersion(systemId, revisionId, target, cb);
        }
        else {
          _getRevision(systemId, rev, target, cb);
        }
      });
    }
  }