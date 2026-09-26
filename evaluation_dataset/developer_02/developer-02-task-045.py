def flattened(self, pred=flattened_pred_default):
    if self.is_value:
      return self
    new_children = []
    for child in self.children:
      if child.is_empty:
        continue
      new_child = child.flattened(pred)
      if pred(new_child, self):
        new_children.extend(new_child.children)
      else:
        new_children.append(new_child)
    return ParseNode(self.node_type,
                     children=new_children,
                     consumed=self.consumed,
                     position=self.position,
                     ignored=self.ignored)