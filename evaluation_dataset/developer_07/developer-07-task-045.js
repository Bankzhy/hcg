function attemptRender(reporter, filename, src, resolve, reject, globals) {
	globals = globals || {};
	less.render(src, {
		paths : [
			"public/static/less"
		],
		filename : filename,
		modifyVars : globals,
		compress : false
	}, function(e, css) {
		if (e) {
			if ((/^variable @(.+?) is undefined$/).test(e.message)) {
				globals[(/^variable @(.+?) is undefined$/).exec(e.message)[1]] = "1";
				attemptRender(reporter, filename, src, resolve, reject, globals);
				return;
			}
			reporter("LESS", filename, e.line, e.message);
			reject();
			return;
		}
		resolve({
			filename : filename,
			src : css.css || css
		});
	});
}