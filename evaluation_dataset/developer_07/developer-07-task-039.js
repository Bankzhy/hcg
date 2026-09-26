function pick(object, keys) {
	var data = {};
	if (typeof keys === 'function') {
		for (var x in object) {
			if (object.hasOwnProperty(x) && keys(object[x], x)) {
				data[x] = object[x];
			}
		}
	} else {
		for (var i = 0, c = keys.length; i < c; i++) {
			data[keys[i]] = object[keys[i]];
		}
	}
	return data;
}