function parseTargetServer(value) {
  var target,
      path;
  if (value.indexOf('http://') !== 0 && value.indexOf('https://') !== 0) {
    value = 'http://' + value + '/';
  }
  target = url.parse(value);
  path = target.path;
  if (path === '/') {
    path = '';
  }
  if (/\$\d/.test(path) === false) {
    path = [path ,'$&'].join('');
  }
  return {
    host: target.hostname,
    port: target.port || ((target.protocol === 'https:') ? 443 : 80),
    originalPort: target.port,
    protocol: target.protocol,
    path: path
  };
}