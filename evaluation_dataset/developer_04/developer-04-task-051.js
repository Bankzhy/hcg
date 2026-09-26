function one(node) {
    var children = node.children
    var length = children.length
    var polarity = 0
    var index = -1
    var child
    var hasNegation
    while (++index < length) {
      child = children[index]
      if (child.data && child.data.polarity) {
        polarity += (hasNegation ? -1 : 1) * child.data.polarity
      }
      if (child.type === 'WordNode') {
        if (hasNegation) {
          hasNegation = false
        } else if (isNegation(child)) {
          hasNegation = true
        }
      }
    }
    patch(node, polarity)
  }