function (attr) {
			attr = attr + "";
			var dotIndex = attr.indexOf('.');
			if( dotIndex >= 0 ) {
				var value = this.___get(attr);
				if (value !== undefined) {
					ObservationRecorder.add(this, attr);
					return value;
				}
				var first = attr.substr(0, dotIndex),
					second = attr.substr(dotIndex+1);
				var current = this.__get( first );
				return current && canReflect.getKeyValue(current, second);
			} else {
				return this.__get( attr );
			}
		}