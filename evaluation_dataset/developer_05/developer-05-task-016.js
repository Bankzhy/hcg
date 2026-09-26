function() {
        var args = arguments,
            ln = args.length,
            i, item;
        for (i = 0; i < ln; i++) {
            item = args[i];
            if (item) {
                if (Ext.isArray(item)) {
                    this.destroy.apply(this, item);
                }
                else if (Ext.isFunction(item.destroy)) {
                    item.destroy();
                }
            }
        }
    }