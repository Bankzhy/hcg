function (cause, prevMin, prevMax) {
            var $this = this;
            var force = false;
            if (cause === 'init' || cause === 'refresh') {
                force = true;
            }
            var curMin = methods.get_current_min_value.call($this),
                curMax = methods.get_current_max_value.call($this);
            if (!force) {
                prevMin = methods.round_value_according_to_rounding.call($this, prevMin);
                prevMax = methods.round_value_according_to_rounding.call($this, prevMax);
            }
            if (force || curMin !== prevMin || curMax !== prevMax) {
                _methods.notify_changed_explicit.call($this, cause, prevMin, prevMax, curMin, curMax);
                force = 1;
            }
            return force;
        }