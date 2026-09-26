public Array decodeVlenData(NcStreamProto.DataCol dproto) throws IOException {
    DataType dataType = NcStream.convertDataType(dproto.getDataType());
    ByteBuffer bb = dproto.getPrimdata().asReadOnlyByteBuffer();
    ByteOrder bo = dproto.getBigend() ? ByteOrder.BIG_ENDIAN : ByteOrder.LITTLE_ENDIAN;
    bb.order(bo);
    Array alldata = Array.factory(dataType, new int[]{dproto.getNelems()}, bb);
    IndexIterator all = alldata.getIndexIterator();
    Section section = NcStream.decodeSection(dproto.getSection());
    Array[] data = new Array[(int) section.computeSize()];
    int count = 0;
    for (int len : dproto.getVlensList()) {
      Array primdata = Array.factory(dataType, new int[]{len});
      IndexIterator prim = primdata.getIndexIterator();
      for (int i=0; i<len; i++) {
        prim.setObjectNext( all.getObjectNext());
      }
      data[count++] = primdata;
    }
    return Array.makeVlenArray(section.getShape(), data);
  }