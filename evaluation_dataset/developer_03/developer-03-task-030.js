function load_as_file(request, startpath) {
	var module_path;
	var resolved_path = path.posix.resolve(startpath, request);
	_.includes(registry.files, resolved_path) && (module_path = resolved_path);
	if(module_path) {
		return module_path;
	}
	var extension = path.extname(request);
	if(!extension) {
		var exts = [".js", ".json"];
		_.forEach(exts, function(ext) {
			resolved_path = path.posix.resolve(startpath, request + ext);
			_.includes(registry.files, resolved_path) && (module_path = resolved_path);
			if(!module_path) {
				return !module_path;
			}
		});
	}
	return module_path;
}