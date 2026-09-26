function advanceTo(input, endChar) {
  var ch = input.charAt(0);
  var tok = { len: 1, val: '', esc: '' };
  var idx = 0;
  function advance() {
    if (ch !== '\\') {
      tok.esc += '\\' + ch;
      tok.val += ch;
    }
    ch = input.charAt(++idx);
    tok.len++;
    if (ch === '\\') {
      advance();
      advance();
    }
  }
  while (ch && ch !== endChar) {
    advance();
  }
  return tok;
}