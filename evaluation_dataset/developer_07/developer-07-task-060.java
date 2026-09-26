@Override
  public SortedMap<String, String> getColumnsToParameters(
      final Record record, int op,
      Map<String, String> parameters,
      Map<String, String> columnsToFields)
  {
    SortedMap<String, String> columnsToParameters = new TreeMap<>();
    for (Map.Entry<String, String> entry : columnsToFields.entrySet()) {
      String columnName = entry.getKey();
      String fieldPath = getFieldPath(columnName, columnsToFields, op);
      if (record.has(fieldPath)) {
        columnsToParameters.put(columnName, parameters.get(columnName));
      } else {
        LOG.trace("Record is missing a field for column {} for the operation code {}", columnName, op);
      }
    }
    return columnsToParameters;
  }