public static boolean isStaticRow(final ConfigRange sourceConfigRange,
			final int rowIndex) {
		if (sourceConfigRange.getCommandList() != null) {
			for (int i = 0; i < sourceConfigRange.getCommandList()
					.size(); i++) {
				Command command = sourceConfigRange.getCommandList().get(i);
				if ((rowIndex >= command.getConfigRange().getFirstRowAddr()
						.getRow())
						&& (rowIndex < (command.getConfigRange()
								.getLastRowPlusAddr().getRow()))) {
					return false;
				}
			}
		}
		return true;
	}