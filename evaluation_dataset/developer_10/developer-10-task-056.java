public String[] getProfilesFor(final String propKeyNameWildcard) {
		HashSet<String> profiles = new HashSet<>();
		profile:
		for (Map.Entry<String, Map<String, PropsEntry>> entries : data.profileProperties.entrySet()) {
			String profileName = entries.getKey();
			Map<String, PropsEntry> value = entries.getValue();
			for (String propKeyName : value.keySet()) {
				if (Wildcard.equalsOrMatch(propKeyName, propKeyNameWildcard)) {
					profiles.add(profileName);
					continue profile;
				}
			}
		}
		return profiles.toArray(new String[0]);
	}