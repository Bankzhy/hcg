def match(self, path):
        match = self._re.search(path)
        if match is None:
            return None
        args = []
        kwargs = {}
        for i, wildcard in enumerate(self._wildcards):
            if wildcard.name == '!':
                continue
            value = wildcard.value(match.groups()[i])
            if not wildcard.name:
                args.append(value)
            else:
                kwargs[wildcard.name] = value
        return self._callback, args, kwargs