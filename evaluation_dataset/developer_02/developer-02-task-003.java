private void flatten(List<DataDescriptor> result, List<DataDescriptor> tree) {
    for (DataDescriptor key : tree) {
      if (key.bad) {
        root.isBad = true;
        result.add(key);
        continue;
      }
      if ((key.f == 3) && (key.subKeys != null)) {
        flatten(result, key.subKeys);
      } else if (key.f == 1) {
        List<DataDescriptor> subTree = new ArrayList<DataDescriptor>();
        flatten(subTree, key.subKeys);
        key.subKeys = subTree;
        result.add(key);
      } else {
        result.add(key);
      }
    }
  }