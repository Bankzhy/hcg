function getJsFiles(dir, fileArray) {
  const files = fs.readdirSync(dir);
  fileArray = fileArray || [];
  files.forEach(function(file) {
    if (file === 'node_modules') {
      return;
    }
    if (fs.statSync(dir + file).isDirectory()) {
      getJsFiles(dir + file + '/', fileArray);
      return;
    }
    if (file.substring(file.length-3, file.length) !== '.js') {
      return;
    }
    fileArray.push(dir+file);
  });
  return fileArray;
}