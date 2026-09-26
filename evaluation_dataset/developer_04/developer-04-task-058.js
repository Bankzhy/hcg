function transformSnapshotList(name, snapshotList, depth, indentCodeBlocks) {
  let result = snapshotHeader(name, depth);
  for (let i = 0; i < snapshotList.length; i++) {
    if (i > 0 && indentCodeBlocks) {
      result += '---\n\n';
    }
    const snapshot = snapshotList[i];
    const lang = snapshot.lang;
    const code = snapshot.code;
    const delimiter = safeDelimiter(code);
    if (indentCodeBlocks) {
      const lines = code.split('\n');
      for (let i = 0; i < lines.length; i++) {
        result += '    ' + lines[i] + '\n';
      }
    } else {
      result += delimiter;
      if (lang) {
        result += lang;
      }
      result += '\n' + code + '\n' + delimiter + '\n';
    }
    result += '\n';
  }
  return result;
}