@Override
  public List<InputSplit> getSplits(JobContext jobContext) throws IOException {
    Configuration configuration = ContextUtil.getConfiguration(jobContext);
    List<InputSplit> splits = new ArrayList<InputSplit>();
    if (isTaskSideMetaData(configuration)) {
      for (InputSplit split : super.getSplits(jobContext)) {
        Preconditions.checkArgument(split instanceof FileSplit,
            "Cannot wrap non-FileSplit: " + split);
        splits.add(ParquetInputSplit.from((FileSplit) split));
      }
      return splits;
    } else {
      splits.addAll(getSplits(configuration, getFooters(jobContext)));
    }
    return splits;
  }