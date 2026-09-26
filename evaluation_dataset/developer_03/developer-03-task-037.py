def verify_reg(self, obj, object_type):
        if obj.name not in self.global_symtab:
            raise QasmError('Cannot find definition for', object_type, "'"
                            + obj.name + "'", 'at line', str(obj.line),
                            'file', obj.file)
        g_sym = self.global_symtab[obj.name]
        if g_sym.type != object_type:
            raise QasmError("Type for '" + g_sym.name + "' should be '"
                            + object_type + "' but was found to be '"
                            + g_sym.type + "'", "line", str(obj.line),
                            "file", obj.file)
        if obj.type == 'indexed_id':
            bound = g_sym.index
            ndx = obj.index
            if ndx < 0 or ndx >= bound:
                raise QasmError("Register index for '" + g_sym.name
                                + "' out of bounds. Index is", str(ndx),
                                "bound is 0 <= index <", str(bound),
                                "at line", str(obj.line), "file", obj.file)