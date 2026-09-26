function parentSetter (x) {
    var previousValue = memoizedObject[key]
    var returnValue
    memoizedObject[key] = x
    if (x === previousValue) return x
    if (definition && x !== null && x !== void 0)
      bindKeys(scope, x, definition, parentNode, keyPath)
    else if (change) {
      returnValue = change(parentNode, x,
        previousValue === void 0 ? null : previousValue, keyPath)
      if (returnValue !== void 0)
        changeValue(parentNode, returnValue, branch[replaceAttributeKey])
    }
    return x
  }