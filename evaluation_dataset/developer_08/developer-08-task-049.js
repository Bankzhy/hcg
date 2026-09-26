function(action, addToHistory) {
        action = action || {};
        Ext.applyIf(action, {
            application: this
        });
        action = Ext.factory(action, Ext.app.Action);
        if (action) {
            var profile    = this.getCurrentProfile(),
                profileNS  = profile ? profile.getNamespace() : undefined,
                controller = this.getController(action.getController(), profileNS);
            if (controller) {
                if (addToHistory !== false) {
                    this.getHistory().add(action, true);
                }
                controller.execute(action);
            }
        }
    }