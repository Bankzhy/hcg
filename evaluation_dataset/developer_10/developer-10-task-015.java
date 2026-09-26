public LiveFileReader getReader() throws IOException {
    Utils.checkState(open, "FileContext is closed");
    if (reader == null) {
      currentFile = getStartingCurrentFileName();
      long fileOffset = getStartingOffset();
      boolean needsToScan = currentFile == null || fileOffset == Long.MAX_VALUE;
      if (needsToScan) {
        if (currentFile != null) {
          currentFile = currentFile.refresh();
        }
        currentFile = scanner.scan(currentFile);
        fileOffset = 0;
      }
      if (currentFile != null) {
        reader = new SingleLineLiveFileReader(getRollMode(), getMultiFileInfo().getTag(), currentFile, charset,
                                              fileOffset, maxLineLength);
        if (!multiFileInfo.getMultiLineMainLinePatter().isEmpty()) {
          reader = new MultiLineLiveFileReader(getMultiFileInfo().getTag(), reader,
                                               Pattern.compile(multiFileInfo.getMultiLineMainLinePatter()));
        }
        if (fileOffset == 0) {
          eventPublisher.publish(new FileEvent(currentFile, FileEvent.Action.START));
        }
      }
    }
    return reader;
  }