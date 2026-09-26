static public String cleanCharacterData(String text) {
    if (text == null) return null;
    boolean bad = false;
    for (int i = 0, len = text.length(); i < len; i++) {
      int ch = text.charAt(i);
      if (!org.jdom2.Verifier.isXMLCharacter(ch)) {
        bad = true;
        break;
      }
    }
    if (!bad) return text;
    StringBuilder sbuff = new StringBuilder(text.length());
    for (int i = 0, len = text.length(); i < len; i++) {
      int ch = text.charAt(i);
      if (org.jdom2.Verifier.isXMLCharacter(ch))
        sbuff.append((char) ch);
    }
    return sbuff.toString();
  }