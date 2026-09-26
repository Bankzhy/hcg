public static String backslashToDAP(String bs) {
    StringBuilder buf = new StringBuilder();
    int len = bs.length();
    for (int i = 0; i < len; i++) {
      char c = bs.charAt(i);
      if (i < (len - 1) && c == '\\') {
        c = bs.charAt(++i);
      }
      if (_allowableInDAP.indexOf(c) < 0) {
        buf.append(_URIEscape);
        String ashex = Integer.toHexString((int) c);
        if (ashex.length() < 2) buf.append('0');
        buf.append(ashex);
      } else
        buf.append(c);
    }
    return buf.toString();
  }