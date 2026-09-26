function(config) {
            if (!config.success) {
                Ext.Logger.error('You must specify a `success` callback for `#purchase` to work.');
                return false;
            }
            if (!config.failure) {
                Ext.Logger.error('You must specify a `failure` callback for `#purchase` to work.');
                return false;
            }
            Ext.device.Communicator.send({
                command: 'Purchase#purchase',
                identifier: this.get('productIdentifier'),
                callbacks: {
                    success: config.success,
                    failure: config.failure
                },
                scope: config.scope || this
            });
        }