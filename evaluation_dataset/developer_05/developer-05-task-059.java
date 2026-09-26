private Node createIssueElement(final LintItem error) {
    final Element issueElement = getDocument().createElement(getIssueElementName());
    final String column = String.valueOf(error.getColumn());
    if (StringUtils.isNotBlank(column)) {
      issueElement.setAttribute(getColumnAttributeName(), column);
    }
    final String evidence = error.getEvidence();
    if (StringUtils.isNotBlank(evidence)) {
      issueElement.setAttribute(ATTR_EVIDENCE, evidence);
    }
    final String line = String.valueOf(error.getLine());
    if (StringUtils.isNotBlank(line)) {
      issueElement.setAttribute(ATTR_LINE, line);
    }
    final String reason = error.getReason();
    if (StringUtils.isNotBlank(reason)) {
      issueElement.setAttribute(getReasonAttributeName(), reason);
    }
    final String severity = error.getSeverity();
    if (StringUtils.isNotBlank(severity)) {
      issueElement.setAttribute(ATTR_SEVERITY, severity);
    }
    return issueElement;
  }