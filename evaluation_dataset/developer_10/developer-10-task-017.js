function(describe, fileBuffer) {
		if (describe && !util.isArray(describe) && describe.m) {
			describe = describe.m;
		}
		if (!Buffer.isBuffer(fileBuffer)) {
			return when.reject('fileBuffer was invalid');
		}
		var parser = new HalModuleParser();
		var fileInfo = {
			filename: 'user-file',
			fileBuffer: fileBuffer
		};
		var that = this;
		return pipeline([
			function() {
				return parser.parseBuffer(fileInfo);
			},
			function() {
				return that.resolveDependencies(describe, fileInfo);
			}
		]);
	}