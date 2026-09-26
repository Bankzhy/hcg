function(dispatches) {
			var self = this;
			this.bind(dispatches.join(' '), function(e) {
				var prop = 'on' + e.type.toLowerCase();
				if (Basic.typeOf(this[prop]) === 'function') {
					this[prop].apply(this, arguments);
				}
			});
			Basic.each(dispatches, function(prop) {
				prop = 'on' + prop.toLowerCase(prop);
				if (Basic.typeOf(self[prop]) === 'undefined') {
					self[prop] = null;
				}
			});
		}