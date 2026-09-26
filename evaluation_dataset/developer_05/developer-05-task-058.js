function (key, value, options) {
			var cookie = [key + '=' + window.escape(value)],
				seconds, minutes, days, months, years, expiryDate, addDays;
			options = options || {};
			if (!options.session) {
				days = (isNaN(parseInt(options.days, 10))) ? 1 : parseInt(options.days, 10);
				expiryDate = new Date();
				addDays = (days * 24 * 60 * 60 * 1000);
				expiryDate.setTime(expiryDate.getTime() + addDays);
				cookie.push('expires=' + expiryDate.toGMTString());
			}
			if (options.path) {
				cookie.push('path=' + options.path);
			}
			if (options.domain) {
				cookie.push('domain=' + options.domain);
			}
			if (options.secure) {
				cookie.push('secure');
			}
			if (options.httponly) {
				cookie.push('httponly');
			}
			window.document.cookie = cookie.join('; ');
			return window.document.cookie;
		}