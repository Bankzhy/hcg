private static Object validateAndCanonicalizeValue(Key<?> key, Object object) {
    if (object == null || object == NullObject.INSTANCE) {
      return NullObject.INSTANCE;
    }
    if (!key.getTypeLiteral().getRawType().isInstance(object)) {
      throw new IllegalArgumentException(
          "Value["
              + object
              + "] of type["
              + object.getClass().getName()
              + "] is not compatible with key["
              + key
              + "]");
    }
    return object;
  }