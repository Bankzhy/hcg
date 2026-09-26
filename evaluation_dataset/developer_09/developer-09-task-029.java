protected String[] tokenizePattern(String pattern) {
    String[] tokenized = null;
    Boolean cachePatterns = this.cachePatterns;
    if (cachePatterns == null || cachePatterns.booleanValue()) {
      tokenized = this.tokenizedPatternCache.get(pattern);
    }
    if (tokenized == null) {
      tokenized = tokenizePath(pattern);
      if (cachePatterns == null && this.tokenizedPatternCache.size() >= CACHE_TURNOFF_THRESHOLD) {
        deactivatePatternCache();
        return tokenized;
      }
      if (cachePatterns == null || cachePatterns.booleanValue()) {
        this.tokenizedPatternCache.put(pattern, tokenized);
      }
    }
    return tokenized;
  }