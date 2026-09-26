@SuppressWarnings({"UnnecessaryContinue"})
  public static boolean descendOnlyFilePath(String path) {
    String[] pathSegments = path.split("/");
    int i = 0;
    for (int indxOrigSegs = 0; indxOrigSegs < pathSegments.length; indxOrigSegs++) {
      String s = pathSegments[indxOrigSegs];
      if (s.equals("."))
        continue;
      else if (s.equals("..")) {
        if (i == 0)
          return false;
        i--;
      } else {
        i++;
      }
    }
    return true;
  }