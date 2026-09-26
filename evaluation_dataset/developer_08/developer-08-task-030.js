function redact(_options, callback) {
	var imports = [],
		output = '',
		errors = [];
	theme['core'] = {};
	_.each(_options.build.core, function(objects, family) {
		theme['core'][family] = {};
		_.each(objects, function(objectName) {
			luiTheme('core.' + family + '.' + objectName);
			imports.push('core/' + family + '/' + objectName);
		});
	});
	if (_options.build.plugins) {
		theme['plugins'] = {};
		_.each(_options.build.plugins, function(plugin) {
			luiTheme('plugins.' + plugin);
		});
	}
	output = tosass.format({theme: theme, imports: imports});
	if (typeof(callback) === 'function') {
		callback(output);
	}
	return output;
}