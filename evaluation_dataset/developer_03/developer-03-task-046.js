function setInMessage(obj, root) {
    obj.inmessage = true;
    if (obj.type == 'static' || obj.type == 'struct' || obj.type == 'message') {
        for (var i = 0; i < obj.val.length; ++i) {
            var cval = obj.val[i];
            if (cval.hasOwnProperty('type2') && 'expand' == cval.type2) {
                continue ;
            }
            var mytype = getRealType(cval.type, root);
            if (isBaseType(mytype)) {
                continue ;
            }
            setInMessage(getGlobalObj(mytype, root), root);
        }
    }
}