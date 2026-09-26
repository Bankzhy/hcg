function makeConceptEntry(concept) {
  if (concept instanceof TBD) {
    const ret = { code: 'TBD', codeSystem: 'urn:tbd' };
    if (concept.text) {
      ret.displayText = concept.text;
    }
    return ret;
  } else {
    const ret = { code: concept.code, codeSystem: concept.system };
    if (concept.display) {
      ret.displayText = concept.display;
    }
    return ret;
  }
}