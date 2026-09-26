function handleErrors (errors) {
  clearOutdatedErrors()
  isFirstCompilation = false
  hasCompileErrors = true
  var formatted = formatWebpackMessages({
    errors: errors,
    warnings: []
  })
  ErrorOverlay.reportBuildError(formatted.errors[0])
  if (typeof console !== 'undefined' && typeof console.error === 'function') {
    for (var i = 0; i < formatted.errors.length; i++) {
      console.error(stripAnsi(formatted.errors[i]))
    }
  }
}