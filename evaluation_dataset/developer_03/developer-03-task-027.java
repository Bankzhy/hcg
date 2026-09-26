@Override
  public FilterReply decide(Marker marker, Logger logger, Level level,
      String s, Object[] objects, Throwable throwable) {
    String mdcValue = MDC.get(this.key);
    if (!isStarted()) {
      return FilterReply.NEUTRAL;
    }
    Level levelAssociatedWithMDCValue = null;
    if (mdcValue != null) {
      levelAssociatedWithMDCValue = valueLevelMap.get(mdcValue);
    }
    if (levelAssociatedWithMDCValue == null) {
      levelAssociatedWithMDCValue = defaultThreshold;
    }
    if (level.isGreaterOrEqual(levelAssociatedWithMDCValue)) {
      return onHigherOrEqual;
    } else {
      return onLower;
    }
  }