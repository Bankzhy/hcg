private DatasetAndGroup findDatasetAndGroup(List<String> paths, GribCollectionImmutable gc) {
    if (paths.size() < 1 || paths.get(0).length() == 0) {
      GribCollectionImmutable.Dataset ds = gc.getDataset(0);
      GribCollectionImmutable.GroupGC dg = ds.getGroup(0);
      return new DatasetAndGroup(ds, dg);
    }
    GribCollectionImmutable.Dataset ds = getSingleDatasetOrByTypeName(gc, paths.get(0));
    if (ds == null) return null;
    boolean isSingleGroup = ds.getGroupsSize() == 1;
    if (isSingleGroup) {
      GribCollectionImmutable.GroupGC g = ds.getGroup(0);
      return new DatasetAndGroup(ds, g);
    }
    String groupName = (paths.size() == 1) ? paths.get(0) : paths.get(1);
    GribCollectionImmutable.GroupGC g = ds.findGroupById(groupName);
    if (g != null)
      return new DatasetAndGroup(ds, g);
    return null;
  }