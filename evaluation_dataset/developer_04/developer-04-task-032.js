function retarget(a, b) {
  while (true) {
    if (!isNode(a)) {
      return a;
    }
    const aRoot = getRoot(a);
    if (
      !isShadowRoot(aRoot) ||
      (isNode(b) && isShadowInclusiveAncestor(aRoot, b))
    ) {
      return a;
    }
    a = getRoot(a).host;
  }
}