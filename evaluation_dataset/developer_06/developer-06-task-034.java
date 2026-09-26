@Override
  public OIndexRIDContainer deserializeFromByteBufferObject(ByteBuffer buffer) {
    final long fileId = buffer.getLong();
    final boolean embedded = buffer.get() > 0;
    final boolean durable = buffer.get() > 0;
    if (embedded) {
      final int size = buffer.getInt();
      final Set<OIdentifiable> underlying = new HashSet<OIdentifiable>(Math.max((int) (size / .75f) + 1, 16));
      for (int i = 0; i < size; i++) {
        underlying.add(LINK_SERIALIZER.deserializeFromByteBufferObject(buffer));
      }
      return new OIndexRIDContainer(fileId, underlying, durable);
    } else {
      final long pageIndex = buffer.getLong();
      final int pageOffset = buffer.getInt();
      final OBonsaiBucketPointer rootPointer = new OBonsaiBucketPointer(pageIndex, pageOffset);
      final ODatabaseDocumentInternal db = ODatabaseRecordThreadLocal.instance().get();
      final OIndexRIDContainerSBTree underlying = new OIndexRIDContainerSBTree(fileId, rootPointer,
          (OAbstractPaginatedStorage) db.getStorage().getUnderlying());
      return new OIndexRIDContainer(fileId, underlying, durable);
    }
  }