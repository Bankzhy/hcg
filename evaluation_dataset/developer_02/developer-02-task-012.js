function(start, end) {
        var me = this,
            items = me.items,
            range = [],
            i;
        if (items.length < 1) {
            return range;
        }
        start = start || 0;
        end = Math.min(typeof end == 'undefined' ? me.length - 1 : end, me.length - 1);
        if (start <= end) {
            for (i = start; i <= end; i++) {
                range[range.length] = items[i];
            }
        } else {
            for (i = start; i >= end; i--) {
                range[range.length] = items[i];
            }
        }
        return range;
    }