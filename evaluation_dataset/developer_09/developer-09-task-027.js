function _request(path, method, headers, body, withCredentials, callback) {
  const xhr = new XMLHttpRequest({});
  const handler = evt => {
    if (callback) {
      callback(evt);
    }
    xhr.removeEventListener('error', handler);
    xhr.removeEventListener('load', handler);
  };
  xhr.addEventListener('error', handler, false);
  xhr.addEventListener('load', handler, false);
  xhr.open(method, path, true);
  Object.keys(headers || {}).forEach(key => {
    xhr.setRequestHeader(key, headers[key]);
  });
  if (withCredentials) {
    xhr.withCredentials = withCredentials;
  }
  xhr.send(body || undefined);
  return xhr;
}