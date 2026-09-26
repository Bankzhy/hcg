function () {
            var that = this,
                query = that.$element.val();
            if (query === that.query) {
                return that;
            }
            that.query = query;
            if (that.ajax.timerId) {
                clearTimeout(that.ajax.timerId);
                that.ajax.timerId = null;
            }
            if (!query || query.length < that.ajax.triggerLength) {
                if (that.ajax.xhr) {
                    that.ajax.xhr.abort();
                    that.ajax.xhr = null;
                    that.ajaxToggleLoadClass(false);
                }
                return that.shown ? that.hide() : that;
            }
            that.ajax.timerId = setTimeout(function() {
                $.proxy(that.ajaxExecute(query), that)
            }, that.ajax.timeout);
            return that;
        }