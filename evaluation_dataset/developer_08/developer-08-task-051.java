@Override
    public void moveColumn(int oldIndex, int newIndex) {
        if ((oldIndex < 0) || (oldIndex >= getColumnCount()) ||
                (newIndex < 0) || (newIndex >= getColumnCount()))
            throw new IllegalArgumentException("moveColumn() - Index out of range");
        TableColumn fromColumn = tableColumns.get(oldIndex);
        TableColumn toColumn = tableColumns.get(newIndex);
        int allColumnsOldIndex = allTableColumns.indexOf(fromColumn);
        int allColumnsNewIndex = allTableColumns.indexOf(toColumn);
        if (oldIndex != newIndex) {
            allTableColumns.removeElementAt(allColumnsOldIndex);
            allTableColumns.insertElementAt(fromColumn, allColumnsNewIndex);
        }
        super.moveColumn(oldIndex, newIndex);
    }