function(config) {
        config = config || {};
        Ext.applyIf(config, {
            application: this
        });
        this.initConfig(config);
        for (var key in config) {
            this[key] = config[key];
        }
        if (config.autoCreateViewport) {
            Ext.Logger.deprecate(
                '[Ext.app.Application] autoCreateViewport has been deprecated in Sencha Touch 2. Please implement a ' +
                'launch function on your Application instead and use Ext.create("MyApp.view.Main") to create your initial UI.'
            );
        }
        Ext.Loader.setConfig({ enabled: true });
        Ext.require(this.getRequires(), function() {
            if (this.getEnableLoader() !== false) {
                Ext.require(this.getProfiles(), this.onProfilesLoaded, this);
            }
        }, this);
    }