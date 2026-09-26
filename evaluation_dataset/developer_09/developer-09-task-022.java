void addLevels(List<GridRecord> records) {
    for (GridRecord record : records) {
      Double d = new Double(record.getLevel1());
      if (!levels.contains(d)) {
        levels.add(d);
      }
      if (dontUseVertical && (levels.size() > 1)) {
        if (GridServiceProvider.debugVert) {
          System.out.println(
                  "GribCoordSys: unused level coordinate has > 1 levels = "
                          + verticalName + " " + record.getLevelType1() + " "
                          + levels.size());
        }
      }
    }
    Collections.sort(levels);
    if (positive.equals("down")) {
      Collections.reverse(levels);
    }
  }