public Key findKey(String name) {
    if (keys == null) {
      return null;
    }
    for (Key key : keys.kkrow) {
      if (key.name.equals(name)) {
        return key;
      }
    }
    for (Key key : keys.kkcol) {
      if (key.name.equals(name)) {
        return key;
      }
    }
    return null;
  }