void dumpClasses(Group g, PrintWriter out) {
    out.println("Dimensions:");
    for (Dimension ds : g.getDimensions()) {
      out.println("  " + ds.getShortName() + " " + ds.getClass().getName());
    }
    out.println("Atributes:");
    for (Attribute a : g.getAttributes()) {
      out.println("  " + a.getShortName() + " " + a.getClass().getName());
    }
    out.println("Variables:");
    dumpVariables(g.getVariables(), out);
    out.println("Groups:");
    for (Group nested : g.getGroups()) {
      out.println("  " + nested.getFullName() + " " + nested.getClass().getName());
      dumpClasses(nested, out);
    }
  }