function(block) {
      var received = false;
      var asts = [];
      utils.some(block, function(ast) {
        if (ast.condition) {
          if (received) {
            return true;
          }
          received = this.getExpression(ast.condition);
        } else if (ast.type === 'else') {
          if (received) {
            return true;
          }
          received = true;
        } else if (received) {
          asts.push(ast);
        }
        return false;
      }, this);
      return this._render(asts, this.condition);
    }