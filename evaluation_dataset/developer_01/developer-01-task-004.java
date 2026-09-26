private void setExceptions(Configuration configuration) {
    this.exceptions.clear();
    this.stageLibExceptions.clear();
    for(String path : configuration.get(PROPERTY_EXCEPTIONS, "").split(",")) {
      this.exceptions.add(replaceVariables(path));
    }
    Configuration stageSpecific = configuration.getSubSetConfiguration(PROPERTY_STAGE_EXCEPTIONS, true);
    for(Map.Entry<String, String> entry : stageSpecific.getValues().entrySet()) {
      Set<String> stageExceptions = new HashSet<>();
      for(String path : entry.getValue().split(",")) {
        stageExceptions.add(replaceVariables(path));
      }
      this.stageLibExceptions.put(entry.getKey(), stageExceptions);
    }
  }