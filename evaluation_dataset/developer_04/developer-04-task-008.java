protected AxisType getAxisType(NetcdfDataset ds, VariableEnhanced ve) {
    Variable v = (Variable) ve;
    String vname = v.getShortName();
    if (vname.equalsIgnoreCase("x"))
      return AxisType.GeoX;
    if (vname.equalsIgnoreCase("y"))
      return AxisType.GeoY;
    if (vname.equalsIgnoreCase("lat"))
      return AxisType.Lat;
    if (vname.equalsIgnoreCase("lon"))
      return AxisType.Lon;
    if (vname.equalsIgnoreCase("time"))
      return AxisType.Time;
    if (vname.equalsIgnoreCase("level"))
      return AxisType.GeoZ;
    return null;
  }