private void doScanIssues(Formatter f, MCollection dcm, boolean useIndex, boolean eachFile, boolean extraInfo) throws IOException {
    Counters countersAll = new Counters();
    for (MFile mfile : dcm.getFilesSorted()) {
      Counters countersOneFile = countersAll.makeSubCounters();
      String path = mfile.getPath();
      f.format(" %s%n", path);
      if (useIndex)
        doScanIssuesWithIndex(f, mfile, extraInfo, countersOneFile);
      else
        doScanIssuesNoIndex(f, mfile, extraInfo, countersOneFile);
      if (eachFile) {
        countersOneFile.show(f);
      }
      countersAll.addTo(countersOneFile);
    }
    f.format("ScanIssues - all files%n");
    countersAll.show(f);
  }