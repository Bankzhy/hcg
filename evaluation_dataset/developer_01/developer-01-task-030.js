function(environment, options) {
      this.environment = environment;
      this.options = options || {};
      this.preamble();
      this.stackSlot = 0;
      this.stackVars = [];
      this.registers = {list: []};
      this.compileChildren(environment, options);
      Handlebars.log(Handlebars.logger.DEBUG, environment.disassemble() + "\n\n");
      var opcodes = environment.opcodes, opcode, name, declareName, declareVal;
      this.i = 0;
      for(l=opcodes.length; this.i<l; this.i++) {
        opcode = this.nextOpcode(0);
        if(opcode[0] === 'DECLARE') {
          this.i = this.i + 2;
          this[opcode[1]] = opcode[2];
        } else {
          this.i = this.i + opcode[1].length;
          this[opcode[0]].apply(this, opcode[1]);
        }
      }
      return this.createFunction();
    }