private void addGrantedAuthorityCollection(Collection<GrantedAuthority> result,
			Object value) {
		if (value == null) {
			return;
		}
		if (value instanceof Collection<?>) {
			addGrantedAuthorityCollection(result, (Collection<?>) value);
		}
		else if (value instanceof Object[]) {
			addGrantedAuthorityCollection(result, (Object[]) value);
		}
		else if (value instanceof String) {
			addGrantedAuthorityCollection(result, (String) value);
		}
		else if (value instanceof GrantedAuthority) {
			result.add((GrantedAuthority) value);
		}
		else {
			throw new IllegalArgumentException("Invalid object type: "
					+ value.getClass().getName());
		}
	}