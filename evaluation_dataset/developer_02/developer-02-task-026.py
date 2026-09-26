def p_if(self, program):
        if len(program) == 3:
            raise QasmError("Ill-formed IF statement. Perhaps a"
                            + " missing '('?")
        if len(program) == 5:
            raise QasmError("Ill-formed IF statement.  Expected '==', "
                            + "received '" + str(program[4].value))
        if len(program) == 6:
            raise QasmError("Ill-formed IF statement.  Expected a number, "
                            + "received '" + str(program[5].value))
        if len(program) == 7:
            raise QasmError("Ill-formed IF statement, unmatched '('")
        if program[7].type == 'if':
            raise QasmError("Nested IF statements not allowed")
        if program[7].type == 'barrier':
            raise QasmError("barrier not permitted in IF statement")
        program[0] = node.If([program[3], node.Int(program[5]), program[7]])