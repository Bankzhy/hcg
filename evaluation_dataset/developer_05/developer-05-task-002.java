static public String buildConventionAttribute(String mainConv, String... convAtts) {
    List<String> result = new ArrayList<>();
    result.add(mainConv);
    for (String convs : convAtts) {
      if (convs == null) continue;
      List<String> ss = breakupConventionNames(convs);
      for (String s : ss) {
        if (matchConvention(s) == null)
          result.add(s);
      }
    }
    boolean start = true;
    Formatter f = new Formatter();
    for (String s : result) {
      if (start)
        f.format("%s", s);
      else
        f.format(", %s", s);
      start = false;
    }
    return f.toString();
  }