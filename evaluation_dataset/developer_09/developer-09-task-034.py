def _find_indent(self, line):
        indent_spaces = self.indent_spaces
        full_dedent = self._full_dedent
        inisp = num_ini_spaces(line)
        if inisp < indent_spaces:
            indent_spaces = inisp
            if indent_spaces <= 0:
                full_dedent = True
        if line.rstrip()[-1] == ':':
            indent_spaces += 4
        elif dedent_re.match(line):
            indent_spaces -= 4
            if indent_spaces <= 0:
                full_dedent = True
        if indent_spaces < 0:
            indent_spaces = 0
        return indent_spaces, full_dedent