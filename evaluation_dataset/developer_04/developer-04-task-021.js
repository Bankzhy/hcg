function createPipeStream(cmd                ){
    var proc;
    var command;
    if(Array.isArray(cmd)){
    var firstCmd = cmd.shift();
    var open = Array.isArray(firstCmd) ? createPipeStream.apply({}, firstCmd) : createPipeStream(firstCmd);
    cmd.forEach(function(p){
        open = open.pipe(p);
    });
    return open;
    } else if(cmd instanceof EventEmitter){
        proc = cmd;
        command = 'pre-defined';
    } else if(typeof cmd === 'object'){
        throw new TypeError('Invalid input, expected object type -> EventEmitter');
    } else {
        var input = utils.normalizeInput.apply(this, arguments);
        command = utils.getCommand(input);
        proc = spawn.apply({}, input);
    }
    proc._command = command;
    if(proc.exitCode){
        throw new Error('Process already dead');
    }
    return PipeStream(proc);
}