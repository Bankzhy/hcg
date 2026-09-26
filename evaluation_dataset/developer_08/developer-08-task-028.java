public static void copyRows(final Sheet srcSheet, final Sheet destSheet, final int srcRowStart, final int srcRowEnd,
			final int destRow, final boolean checkLock, final boolean setHiddenColumn) {
		int length = srcRowEnd - srcRowStart + 1;
		if (length <= 0) {
			return;
		}
		destSheet.shiftRows(destRow, destSheet.getLastRowNum(), length, true, false);
		for (int i = 0; i < length; i++) {
			copySingleRow(srcSheet, destSheet, srcRowStart + i, destRow + i, checkLock, setHiddenColumn);
		}
		for (int i = 0; i < srcSheet.getNumMergedRegions(); i++) {
			CellRangeAddress cellRangeAddress = srcSheet.getMergedRegion(i);
			if ((cellRangeAddress.getFirstRow() >= srcRowStart) && (cellRangeAddress.getLastRow() <= srcRowEnd)) {
				int targetRowFrom = cellRangeAddress.getFirstRow() - srcRowStart + destRow;
				int targetRowTo = cellRangeAddress.getLastRow() - srcRowStart + destRow;
				CellRangeAddress newCellRangeAddress = new CellRangeAddress(targetRowFrom, targetRowTo,
						cellRangeAddress.getFirstColumn(), cellRangeAddress.getLastColumn());
				destSheet.addMergedRegion(newCellRangeAddress);
			}
		}
	}