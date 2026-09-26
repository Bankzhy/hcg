protected void addRule(final D ruleDefinition, final boolean include) {
		if (rules == null) {
			rules = new ArrayList<>();
		}
		if (include) {
			includesCount++;
		} else {
			excludesCount++;
		}
		Rule<R> newRule = new Rule<>(makeRule(ruleDefinition), include);
		if (rules.contains(newRule)) {
			return;
		}
		rules.add(newRule);
	}