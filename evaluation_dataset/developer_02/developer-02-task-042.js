function( type, item ) {
			var id = _.isString( item ) || _.isNumber( item ) ? item : null;
			if ( id === null ) {
				if ( item instanceof Backbone.RelationalModel ) {
					id = item.id;
				}
				else if ( _.isObject( item ) ) {
					id = item[ type.prototype.idAttribute ];
				}
			}
			if ( !id && id !== 0 ) {
				id = null;
			}
			return id;
		}