function ( source, target, alias, type ) {
        if (
            Util.isnt.Class( source ) ||
            Util.isnt.Class( target ) ||
            Util.isnt.String( alias ) || ! alias ||
            Association.types.indexOf( type ) === -1
        ) {
            return false;
        }
        this.id = Util.uniqId();
        this.source = source;
        this.target = target;
        this.alias = Util.String.capitalize( alias );
        this.type = type;
        return this.complete();
    }