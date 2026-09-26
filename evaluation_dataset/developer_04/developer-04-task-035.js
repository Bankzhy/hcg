function createScopedCss(html, scope, filepath, cssVariables) {
	scope = typeof scope === 'string' ? {ns: scope, vars: new Map()} : scope;
	const style = html.match(styleMatcher);
	if (!style) {
		return [{}, scope.vars, ''];
	}
	const cssom = css.parse(style[1], {source: filepath});
	const vars = new Map(scope.vars.entries());
	getVariables(cssom).forEach((value, key) => vars.set(key, value));
	if (cssVariables) {
		resolveScopeVariables(cssom, vars);
	}
	const [classes, transformMap] = rewriteSelectors(`${decamelize(scope.ns, '-')}`, cssom);
	return [classes, vars, css.stringify(cssom), transformMap];
}