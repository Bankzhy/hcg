function cleanupStyles(item) {
  var prop;
  var reactProps;
  if (item.props.style) {
    reactProps = {};
    for(prop in item.props.style) {
      reactProps[prop] = item._node.style[prop];
    }
  }
  item._node.removeAttribute('style');
  if (reactProps) {
    for(prop in reactProps) {
      item._node.style[prop] = reactProps[prop];
    }
  }
  if (item._prevStyles) {
    for(prop in item._prevStyles) {
      item._node.style[prop] = item._prevStyles[prop];
    }
  }
}