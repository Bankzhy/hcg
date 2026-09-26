function extend(target, options){
    options = options||{};
    var parentClass = this;
    logger.trace("Extending from ",   parentClass._angoosemeta.name, options);
    var rv = null;
    if(typeof (target) == 'function'){
        rv = target;
        mixinInstance(parentClass, rv, options);
        bindMongooseMethods(rv);
    }
    else{
        rv = parentClass.$extend( target );
    }
    rv = mixinStatic(parentClass, rv, options);
    if(rv._angoosemeta.name){
    }
    return rv;
}