public static String join(Collection<?> list, String delimiter) {
    if (list == null || list.isEmpty()) {
      return "";
    }
    if (delimiter == null) {
      delimiter = "";
    }
    StringBuilder s = new StringBuilder();
    boolean first = true;
    for (Object e : list) {
      if (first) {
        first = false;
      } else {
        s.append(delimiter);
      }
      s.append(e);
    }
    return s.toString();
  }