function(parent, name            ) {
				var wrap,
					ret;
				if (parent.indexOf('depth') === 0) {
					wrap = true;
				}
				if (/^[0-9]+$/.test(name)) {
					ret = parent + "[" + name + "]";
				} else if (JavaScriptCompiler.isValidJavaScriptVariableName(name)) {
					ret = parent + "." + name;
				}
				else {
					ret = parent + "['" + name + "']";
				}
				if (wrap) {
					return '(' + parent + ' && ' + ret + ')';
				} else {
					return ret;
				}
			}