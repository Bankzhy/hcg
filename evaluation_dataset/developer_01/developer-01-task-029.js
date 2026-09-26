function() {
    var pos = this.position();
    if (this.input) return;
    var prev = this.prev();
    while (prev.type !== 'root' && !prev.visited) {
      if (this.options.strict === true) {
        throw new SyntaxError('invalid syntax:' + util.inspect(prev, null, 2));
      }
      if (!hasDelims(prev)) {
        prev.parent.escaped = true;
        prev.escaped = true;
      }
      visit(prev, function(node) {
        if (!hasDelims(node.parent)) {
          node.parent.escaped = true;
          node.escaped = true;
        }
      });
      prev = prev.parent;
    }
    var tok = pos({
      type: 'eos',
      val: this.append || ''
    });
    define(tok, 'parent', this.ast);
    return tok;
  }