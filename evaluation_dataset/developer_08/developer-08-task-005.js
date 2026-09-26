function _resolve(path, options, mod) {
  if (path) {
    var i = path.indexOf(':')
    if (i === -1) {
      return resolveModule(path, options, mod)
    } else {
      var namespace = path.substring(0, i)
      var p = path.substring(i + 1)
      if (namespace === "env") {
        return resolveEnv(p, options, mod)
      } else if (namespace === "http" || namespace === "https") {
        return resolveHttp(path, options, mod)
      } else if (namespace === "file") {
        return resolveFile(p, options, mod)
      } else {
        throw new Error("Unable to resolve path: '" + path + "'. Unknown namespace: " + namespace)
      }
    }
  }
}