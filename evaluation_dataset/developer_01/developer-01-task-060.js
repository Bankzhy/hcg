function list(opts, cb) {
    "use strict";
    if (typeof opts === 'function') {
        cb = opts;
        opts = undefined;
    }
    var params = ['list', '-H'];
    if (opts && opts.name) {
        params.push(opts.name);
    }
    zpool(params, function (err, stdout) {
        if (cb && typeof cb === 'function') {
            if (err) {
                cb(err);
                return;
            }
            var lines = util.compact(stdout.split('\n'));
            var list = lines.map(function (x) { return new ZPool(x); });
            cb(err, list);
        }
    });
}