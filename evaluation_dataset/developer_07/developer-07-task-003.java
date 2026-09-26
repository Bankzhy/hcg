protected void resetSoft() {
		columnCount = 0;
		paramCount = 0;
		hintCount = 0;
		if (tableRefs != null) {
			tableRefs.clear();
		}
		if (columnData != null) {
			columnData.clear();
		}
		if (parameters != null) {
			parameters.clear();
		}
		if (hints != null) {
			hints.clear();
		}
	}