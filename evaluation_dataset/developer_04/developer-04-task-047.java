public PipelineConfiguration upgradeIfNecessary(
      StageLibraryTask library,
      PipelineConfiguration pipelineConf,
      List<Issue> issues
  ) {
    Preconditions.checkArgument(issues.isEmpty(), "Given list of issues must be empty.");
    boolean upgrade;
    upgrade = needsSchemaUpgrade(pipelineConf, issues);
    if(upgrade && issues.isEmpty()) {
      pipelineConf = upgradeSchema(library, pipelineConf, issues);
    }
    if(!issues.isEmpty()) {
      return null;
    }
    upgrade = needsUpgrade(library, pipelineConf, issues);
    if (upgrade && issues.isEmpty()) {
      pipelineConf = upgrade(library, pipelineConf, issues);
    }
    return (issues.isEmpty()) ? pipelineConf : null;
  }