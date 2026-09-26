function ( proto, parentProto ) {
        proto._initHooks = [];
        proto._destroyHooks = [];
        proto.callInitHooks = function () {
            if ( this._initHooksCalled ) { return; }
            if ( parentProto ) {
                parentProto.callInitHooks.call(this);
            }
            this._initHooksCalled = true;
            for (var i = 0, len = proto._initHooks.length; i < len; i++) {
                proto._initHooks[i].call(this);
            }
        };
        proto.callDestroyHooks = function () {
            if ( this._destroyHooksCalled ) { return; }
            if ( parentProto.callDestroyHooks ) {
                parentProto.callDestroyHooks.call(this);
            }
            this._destroyHooksCalled = true;
            for (var i = 0, len = proto._destroyHooks.length; i < len; i++) {
                proto._destroyHooks[i].call(this);
            }
        };
    }