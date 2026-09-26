function setQueryParameters(params) {
    if (!params) return this;
    var error = SearchParameters.validate(this, params);
    if (error) {
      throw error;
    }
    var parsedParams = SearchParameters._parseNumbers(params);
    return this.mutateMe(function mergeWith(newInstance) {
      var ks = keys(params);
      forEach(ks, function(k) {
        newInstance[k] = parsedParams[k];
      });
      return newInstance;
    });
  }