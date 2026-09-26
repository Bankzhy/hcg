function performRequest (options, isFirstRequest) {
  const requester = options.requester;
  const request = requester(options);
  if (request.getHeader('host') === HOST) {
    request.setHeader('host', request.uri.host);
  }
  if (typeof request.callback !== 'function') {
    throw new TypeError('Expected a callback function, got ' +
        typeof (request.callback) + ' instead.');
  }
  if (isFirstRequest) {
    options.callback = request.callback;
  }
  request.removeAllListeners('error')
    .once('error', function (error) {
      onRequestResponse(options, error);
    });
  request.removeAllListeners('complete')
    .once('complete', function (response, body) {
      onRequestResponse(options, null, response, body);
    });
  request.cloudscraper = true;
  return request;
}