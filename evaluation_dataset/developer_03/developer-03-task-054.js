function(type) {
    this.ast.tags[type] = null;
    this.names.push(type);
    var cached = this.regex.createTag(type);
    var file = this.file;
    var lexer = this;
    var fn = this.lexers[type] = function() {
      var pos = lexer.position();
      var m = lexer.match(cached.strict);
      if (!m) return;
      var name = utils.getName(m[1]);
      if (this.options.strict) {
        var isKnown = utils.has(lexer.known.tags, type);
        if (isKnown && file.hasOwnProperty(type) && !file.hasOwnProperty('isParsed')) {
          throw new Error(`only one "${type}" tag may be defined per template`);
        }
      }
      file[type] = name;
      lexer.ast.tags[type] = name;
      lexer.createNode(type, name, m, pos);
    };
    this.addLexer(fn);
    return this;
  }