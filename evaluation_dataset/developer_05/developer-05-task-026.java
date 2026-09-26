@Deprecated
  public Vertex getVertexByKey(final String iKey, Object iValue) {
    makeActive();
    String indexName;
    if (iKey.indexOf('.') > -1)
      indexName = iKey;
    else
      indexName = OrientVertexType.CLASS_NAME + "." + iKey;
    final OIndex<?> idx = getDatabase().getMetadata().getIndexManager().getIndex(indexName);
    if (idx != null) {
      iValue = convertKey(idx, iValue);
      Object v = idx.get(iValue);
      if (v != null)
        return getVertex(v);
      return null;
    } else
      throw new IllegalArgumentException("Index '" + indexName + "' not found");
  }