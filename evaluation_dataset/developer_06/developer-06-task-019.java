public boolean result(final Object iRecord) {
    final OIdentifiable id = (OIdentifiable) iRecord;
    if (id.getIdentity().isValid()) {
      final ODocument record = id.getRecord();
      ODatabaseDocumentInternal db = getDatabase();
      final OVertex v = toVertex(record);
      if (v != null) {
        v.delete();
        if (!txAlreadyBegun && batch > 0 && removed % batch == 0) {
          db.commit();
          db.begin();
        }
        if (returning.equalsIgnoreCase("BEFORE"))
          allDeletedRecords.add(record);
        removed++;
      }
    }
    return true;
  }