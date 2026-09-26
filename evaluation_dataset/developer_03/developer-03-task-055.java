static public String backslashEscape(String x, String reservedChars) {
    if (x == null) {
      return null;
    } else if (reservedChars == null) {
      return x;
    }
    boolean ok = true;
    for (int pos = 0; pos < x.length(); pos++) {
      char c = x.charAt(pos);
      if (reservedChars.indexOf(c) >= 0) {
        ok = false;
        break;
      }
    }
    if (ok) return x;
    StringBuilder sb = new StringBuilder(x);
    for (int pos = 0; pos < sb.length(); pos++) {
      char c = sb.charAt(pos);
      if (reservedChars.indexOf(c) < 0) {
        continue;
      }
      sb.setCharAt(pos, '\\');
      pos++;
      sb.insert(pos, c);
      pos++;
    }
    return sb.toString();
  }