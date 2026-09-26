@Override
  public Array readData(Variable v2, Section section) throws IOException, InvalidRangeException {
    long start = System.currentTimeMillis();
    Array dataArray = Array.factory(DataType.FLOAT, section.getShape());
    GridVariable pv = (GridVariable) v2.getSPobject();
    int rangeIdx = 0;
    Range ensRange = pv.hasEnsemble() ? section.getRange(rangeIdx++) : new Range( 0, 0 );
    Range timeRange = (section.getRank() > 2) ? section.getRange(rangeIdx++) : new Range( 0, 0 );
    Range levRange = pv.hasVert() ? section.getRange(rangeIdx++) : new Range( 0, 0 );
    Range yRange = section.getRange(rangeIdx++);
    Range xRange = section.getRange(rangeIdx);
    IndexIterator ii = dataArray.getIndexIterator();
    for (int ensIdx : ensRange) {
      for (int timeIdx : timeRange) {
        for (int levelIdx : levRange) {
          readXY(v2, ensIdx, timeIdx, levelIdx, yRange, xRange, ii);
        }
      }
    }
    if (debugTiming) {
      long took = System.currentTimeMillis() - start;
      System.out.println("  read data took=" + took + " msec ");
    }
    return dataArray;
  }