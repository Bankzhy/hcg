function setNode (oldNode, newNode) {
  if (oldNode.nodeType === newNode.nodeType) {
    if (oldNode.nodeType === ELEMENT_TYPE) {
      if (isEqualNode(oldNode, newNode)) return
      setChildNodes(oldNode, newNode)
      if (oldNode.nodeName === newNode.nodeName) {
        setAttributes(oldNode.attributes, newNode.attributes)
      } else {
        var newPrev = newNode.cloneNode()
        while (oldNode.firstChild) newPrev.appendChild(oldNode.firstChild)
        oldNode.parentNode.replaceChild(newPrev, oldNode)
      }
    } else {
      if (oldNode.nodeValue !== newNode.nodeValue) {
        oldNode.nodeValue = newNode.nodeValue
      }
    }
  } else {
    oldNode.parentNode.replaceChild(newNode, dismount(oldNode))
    mount(newNode)
  }
}