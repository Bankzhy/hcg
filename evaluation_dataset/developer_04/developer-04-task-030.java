public static String breakTextAtWords(String text, String insert, int lineSize) {
    StringBuilder buff = new StringBuilder();
    StringTokenizer stoker = new StringTokenizer(text);
    int lineCount = 0;
    while (stoker.hasMoreTokens()) {
      String tok = stoker.nextToken();
      if (tok.length() + lineCount >= lineSize) {
        buff.append(insert);
        lineCount = 0;
      }
      buff.append(tok);
      buff.append(" ");
      lineCount += tok.length() + 1;
    }
    return buff.toString();
  }