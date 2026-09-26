function() {
        var filters = this.getFilters().items;
        this.filterFn = function(item) {
            var isMatch = true,
                length = filters.length,
                i;
            for (i = 0; i < length; i++) {
                var filter = filters[i],
                    fn     = filter.getFilterFn(),
                    scope  = filter.getScope() || this;
                isMatch = isMatch && fn.call(scope, item);
            }
            return isMatch;
        };
        this.dirtyFilterFn = false;
        return this.filterFn;
    }