def transform_alias(self, alias,rest=''):
        nargs, cmd = self.alias_table[alias]
        if ' ' in cmd and os.path.isfile(cmd):
            cmd = '"%s"' % cmd
        if cmd.find('%l') >= 0:
            cmd = cmd.replace('%l', rest)
            rest = ''
        if nargs==0:
            cmd = '%s %s' % (cmd, rest)
        else:
            args = rest.split(None, nargs)
            if len(args) < nargs:
                raise AliasError('Alias <%s> requires %s arguments, %s given.' %
                      (alias, nargs, len(args)))
            cmd = '%s %s' % (cmd % tuple(args[:nargs]),' '.join(args[nargs:]))
        return cmd