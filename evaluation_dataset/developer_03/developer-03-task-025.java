private void getInfo(Formatter buf) {
    int countGridset = 0;
    for (Gridset gs : gridsetHash.values()) {
      GridCoordSystem gcs = gs.getGeoCoordSystem();
      buf.format("%nGridset %d  coordSys=%s", countGridset,  gcs);
      buf.format(" LLbb=%s ", gcs.getLatLonBoundingBox());
      if ((gcs.getProjection() != null)  && !gcs.getProjection().isLatLon())
        buf.format(" bb= %s", gcs.getBoundingBox());
      buf.format("%n");
      buf.format("Name__________________________Unit__________________________hasMissing_Description%n");
      for (GridDatatype grid : gs.getGrids()) {
        buf.format("%s%n", grid.getInfo());
      }
      countGridset++;
      buf.format("%n");
    }
    buf.format("%nGeoReferencing Coordinate Axes%n");
    buf.format("Name__________________________Units_______________Type______Description%n");
    for (CoordinateAxis axis : ncd.getCoordinateAxes()) {
      if (axis.getAxisType() == null) continue;
      axis.getInfo(buf);
      buf.format("%n");
    }
  }