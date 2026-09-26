function classify(value) {
  var type = null
  var normal
  value = value.replace(digits, toWords).split(split, 1)[0]
  normal = lower(value)
  if (requiresA(value)) {
    type = 'a'
  }
  if (requiresAn(value)) {
    type = type === 'a' ? 'a-or-an' : 'an'
  }
  if (!type && normal === value) {
    type = vowel.test(normal.charAt(0)) ? 'an' : 'a'
  }
  return type
}