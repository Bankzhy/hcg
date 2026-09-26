function findSlot(slotable, openFlag) {
  const { parentNode: parent } = slotable;
  if (!parent) {
    return null;
  }
  const shadow = parent._shadowRoot;
  if (!shadow || (openFlag && shadow.mode !== "open")) {
    return null;
  }
  for (const child of domSymbolTree.treeIterator(shadow)) {
    if (isSlot(child) && child.name === slotable._slotableName) {
      return child;
    }
  }
  return null;
}