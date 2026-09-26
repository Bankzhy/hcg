protected DatasetEnhancer readDatasetScanAddTimeCoverage(Element addTimeCovElem) {
    DatasetEnhancer timeCovEnhancer = null;
    String matchName = addTimeCovElem.getAttributeValue("datasetNameMatchPattern");
    String matchPath = addTimeCovElem.getAttributeValue("datasetPathMatchPattern");
    String subst = addTimeCovElem.getAttributeValue("startTimeSubstitutionPattern");
    String duration = addTimeCovElem.getAttributeValue("duration");
    if (matchName != null && subst != null && duration != null) {
      timeCovEnhancer = RegExpAndDurationTimeCoverageEnhancer
              .getInstanceToMatchOnDatasetName(matchName, subst, duration);
    } else if (matchPath != null && subst != null && duration != null) {
      timeCovEnhancer = RegExpAndDurationTimeCoverageEnhancer
              .getInstanceToMatchOnDatasetPath(matchPath, subst, duration);
    }
    return timeCovEnhancer;
  }