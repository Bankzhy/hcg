static public VarAtt findVariableWithAttribute(NetcdfDataset ds, String attName) {
    for (Variable v : ds.getVariables()) {
      Attribute att = v.findAttributeIgnoreCase(attName);
      if (att != null) return new VarAtt(v, att);
    }
    for (Variable v : ds.getVariables()) {
      if (v instanceof Structure) {
        Structure s = (Structure) v;
        for (Variable vs : s.getVariables()) {
          Attribute att = vs.findAttributeIgnoreCase(attName);
          if (att != null) return new VarAtt(vs, att);
        }
      }
    }
    return null;
  }