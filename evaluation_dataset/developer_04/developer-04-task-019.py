def _maybe_parse_configurable_reference(self):
    if self._current_token.value != '@':
      return False, None
    location = self._current_location()
    self._advance_one_token()
    scoped_name = self._parse_selector(allow_periods_in_scope=True)
    evaluate = False
    if self._current_token.value == '(':
      evaluate = True
      self._advance()
      if self._current_token.value != ')':
        self._raise_syntax_error("Expected ')'.")
      self._advance_one_token()
    self._skip_whitespace_and_comments()
    with utils.try_with_location(location):
      reference = self._delegate.configurable_reference(scoped_name, evaluate)
    return True, reference