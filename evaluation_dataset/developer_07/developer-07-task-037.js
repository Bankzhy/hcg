function sessions(options, cb){
    if(!cb){
        cb = options;
        options = { is_bot: false };
    }
    var n = 32;
    Session.find(options)
        .sort({date: 'desc'})
        .limit(n)
        .exec(function(err, results){
            if(err)
                log.error('Sessions query error:', err);
            cb(err, results)
        });
}