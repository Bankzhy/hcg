@Override
    public AttributesDao getAttributesDao(Contents contents) {
        if (contents == null) {
            throw new GeoPackageException("Non null "
                    + Contents.class.getSimpleName()
                    + " is required to create "
                    + AttributesDao.class.getSimpleName());
        }
        if (contents.getDataType() != ContentsDataType.ATTRIBUTES) {
            throw new GeoPackageException(Contents.class.getSimpleName()
                    + " is required to be of type "
                    + ContentsDataType.ATTRIBUTES + ". Actual: "
                    + contents.getDataTypeString());
        }
        AttributesTableReader tableReader = new AttributesTableReader(
                contents.getTableName());
        final AttributesTable attributesTable = tableReader.readTable(new AttributesWrapperConnection(database));
        attributesTable.setContents(contents);
        AttributesConnection userDb = new AttributesConnection(database);
        AttributesDao dao = new AttributesDao(getName(), database, userDb,
                attributesTable);
        registerCursorWrapper(attributesTable.getTableName(),
                new GeoPackageCursorWrapper() {
                    @Override
                    public Cursor wrapCursor(Cursor cursor) {
                        return new AttributesCursor(attributesTable, cursor);
                    }
                });
        return dao;
    }