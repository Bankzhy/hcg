function AuthorizationCodeGrantType(options) {
  options = options || {};
  if (!options.model) {
    throw new InvalidArgumentError('Missing parameter: `model`');
  }
  if (!options.model.getAuthorizationCode) {
    throw new InvalidArgumentError('Invalid argument: model does not implement `getAuthorizationCode()`');
  }
  if (!options.model.revokeAuthorizationCode) {
    throw new InvalidArgumentError('Invalid argument: model does not implement `revokeAuthorizationCode()`');
  }
  if (!options.model.saveToken) {
    throw new InvalidArgumentError('Invalid argument: model does not implement `saveToken()`');
  }
  AbstractGrantType.call(this, options);
}