static byte[] extract(InputStream is, ByteArrayOutputStream overflowBuffer, int limit) throws IOException {
    byte[] message;
    if (copy(is, overflowBuffer, limit - overflowBuffer.size())) {
      if (overflowBuffer.size() == 0) {
        message = null;
      } else {
        byte[] data = overflowBuffer.toByteArray();
        message = new byte[data.length + 1];
        message[0] = JSON1_MAGIC_NUMBER;
        System.arraycopy(data, 0, message, 1, data.length);
        overflowBuffer.reset();
      }
    } else {
      byte[] data = overflowBuffer.toByteArray();
      int lastEOL = findEndOfLastLineBeforeLimit(data, limit);
      if (lastEOL == -1) {
        throw new IOException(Utils.format("Maximum message size '{}' exceeded", limit));
      }
      message = new byte[lastEOL + 1];
      message[0] = JSON1_MAGIC_NUMBER;
      System.arraycopy(data, 0, message, 1, lastEOL);
      overflowBuffer.reset();
      overflowBuffer.write(data, lastEOL, data.length - lastEOL);
    }
    return message;
  }