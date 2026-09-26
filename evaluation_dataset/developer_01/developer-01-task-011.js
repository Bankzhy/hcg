function (reference, options) {
    reference = reference.trim()
    if (reference.lastIndexOf('#', 0) < 0) {
      console.warn('Remote references not supported yet. Reference must start with "#" (but was ' + reference + ')')
      return {}
    }
    var components = reference.split('#')
    var hash = components[1]
    var hashParts = hash.split('/')
    var current = options.data.root
    hashParts.forEach(function (hashPart) {
      if (hashPart.trim().length > 0) {
        if (typeof current === 'undefined') {
          throw new Error("Reference '" + reference + "' cannot be resolved. '" + hashPart + "' is undefined.")
        }
        current = current[hashPart]
      }
    })
    return current
  }