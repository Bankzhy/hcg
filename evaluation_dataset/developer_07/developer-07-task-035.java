private void calculateShardingStrategy(QueryPlanningInfo info, OCommandContext ctx) {
    ODatabaseDocumentInternal db = (ODatabaseDocumentInternal) ctx.getDatabase();
    info.distributedFetchExecutionPlans = new LinkedHashMap<>();
    Map<String, Set<String>> clusterMap = db.getActiveClusterMap();
    Set<String> queryClusters = calculateTargetClusters(info, ctx);
    if (queryClusters == null || queryClusters.size() == 0) {
      String localNode = db.getLocalNodeName();
      info.serverToClusters = new LinkedHashMap<>();
      info.serverToClusters.put(localNode, clusterMap.get(localNode));
      info.distributedFetchExecutionPlans.put(localNode, new OSelectExecutionPlan(ctx));
      return;
    }
    Map<String, Set<String>> minimalSetOfNodes = getMinimalSetOfNodesForShardedQuery(db.getLocalNodeName(), clusterMap,
        queryClusters);
    if (minimalSetOfNodes == null) {
      throw new OCommandExecutionException("Cannot execute sharded query");
    }
    info.serverToClusters = minimalSetOfNodes;
    for (String node : info.serverToClusters.keySet()) {
      info.distributedFetchExecutionPlans.put(node, new OSelectExecutionPlan(ctx));
    }
  }