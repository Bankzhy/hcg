function (travisYML, newVersion, newCodeName, existingVersions) {
  if (existingVersions.versions.length === 0) return travisYML
  const nodeVersionIndex = getNodeVersionIndex(existingVersions.versions, newVersion, newCodeName)
  const travisYMLLines = travisYML.split('\n')
  if (nodeVersionIndex === -1) {
    let delimiter = ''
    let leadingSpaces = ''
    if (existingVersions.versions && existingVersions.versions.length > 0) {
      if (existingVersions.versions[0].match(/"/)) {
        delimiter = '"'
      }
      if (existingVersions.versions[0].match(/'/)) {
        delimiter = "'"
      }
      leadingSpaces = existingVersions.versions[0].match(/^([ ]*)/)[1]
    }
    if (existingVersions.versions.length === 1 && existingVersions.startIndex === existingVersions.endIndex) {
      travisYMLLines.splice(existingVersions.startIndex, 1, 'node_js:')
      travisYMLLines.splice(existingVersions.startIndex + 1, 0, `${leadingSpaces}- ${existingVersions.versions[0]}`)
      travisYMLLines.splice(existingVersions.startIndex + 2, 0, `${leadingSpaces}- ${delimiter}${newVersion}${delimiter}`)
    } else {
      travisYMLLines.splice(existingVersions.endIndex + 1, 0, `${leadingSpaces}- ${delimiter}${newVersion}${delimiter}`)
    }
  }
  return travisYMLLines.join('\n')
}