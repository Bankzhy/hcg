private Class<?> getClassForType(String typeName) throws GPUdbException {
    typeName = typeName.replace(" ", "");
    if (typeName.equalsIgnoreCase(STRING_TYPE_NAME)) {
      return String.class;
    } else if (typeName.equalsIgnoreCase(LONG_TYPE_NAME)) {
      return Long.class;
    } else if (typeName.equalsIgnoreCase(INTEGER_TYPE_NAME)) {
      return Integer.class;
    } else if (typeName.equalsIgnoreCase(FLOAT_TYPE_NAME)) {
      return Float.class;
    } else if (typeName.equalsIgnoreCase(DOUBLE_TYPE_NAME)) {
      return Double.class;
    } else if (typeName.equalsIgnoreCase(BYTES_TYPE_NAME)) {
      return ByteBuffer.class;
    } else {
      throw new GPUdbException("Error: unknown type '" + typeName + "' in table schema");
    }
  }