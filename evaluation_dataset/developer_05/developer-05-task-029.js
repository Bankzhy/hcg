function(store) {
        var initialConfig = this.getInitialConfig(),
            value = this.getValue();
        if (value || value == 0) {
            this.updateValue(this.applyValue(value));
        }
        if (this.getValue() === null) {
            if (initialConfig.hasOwnProperty('value')) {
                this.setValue(initialConfig.value);
            }
            if (this.getValue() === null && this.getAutoSelect()) {
                if (store.getCount() > 0) {
                    this.setValue(store.getAt(0));
                }
            }
        }
    }