function extractStyles(src) {
	var isInBlock = false,
		lines = [];
	src.replace(/\r/g, "").split("\n").forEach(function(l) {
		if (l.indexOf("</style") > -1) {
			lines[lines.length] = "";
			isInBlock = false;
			return;
		}
		if (isInBlock) {
			lines[lines.length] = l;
		} else {
			lines[lines.length] = "";
		}
		if (l.indexOf("<style") > -1) {
			isInBlock = true;
		}
	});
	return lines.join("\n").replace(/\{\$(\w+\.)*\w+\}/g, "{}");
}