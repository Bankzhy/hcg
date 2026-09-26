private static List<SerialRow> assembleRowsListFromRowsMapping(
			final List<SerialRow> all, final List<SerialRow> current) {
		List<SerialRow> list;
		if (all == null) {
			list = new ArrayList<>();
			list.addAll(current);
		} else {
			list = all;
			for (SerialRow row : current) {
				if (!all.contains(row)) {
					list.add(row);
				}
			}
		}
		return list;
	}