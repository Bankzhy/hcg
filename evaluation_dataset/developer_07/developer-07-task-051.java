@Override
  protected List<ConfigIssue> init() {
    List<ConfigIssue> issues = super.init();
    errorRecordHandler = new DefaultErrorRecordHandler(getContext());
    double rateLimit = conf.rateLimit > 0 ? (1000.0 / conf.rateLimit) : Double.MAX_VALUE;
    rateLimiter = RateLimiter.create(rateLimit);
    httpClientCommon.init(issues, getContext());
    conf.dataFormatConfig.init(
        getContext(),
        conf.dataFormat,
        Groups.HTTP.name(),
        HttpClientCommon.DATA_FORMAT_CONFIG_PREFIX,
        issues
    );
    bodyVars = getContext().createELVars();
    bodyEval = getContext().createELEval(REQUEST_BODY_CONFIG_NAME);
    if (issues.isEmpty()) {
      parserFactory = conf.dataFormatConfig.getParserFactory();
    }
    return issues;
  }