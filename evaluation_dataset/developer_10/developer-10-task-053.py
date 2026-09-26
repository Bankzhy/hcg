def _get_all(self, node, name, max_depth, shortcuts):
        if max_depth is None:
            max_depth = float('inf')
        if isinstance(name, list):
            split_name = name
        elif isinstance(name, tuple):
            split_name = list(name)
        elif isinstance(name, int):
            split_name = [name]
        else:
            split_name = name.split('.')
        for idx, key in enumerate(split_name):
            _, key = self._translate_shortcut(key)
            _, key = self._replace_wildcards(key)
            split_name[idx] = key
        return self._backwards_search(node, split_name, max_depth, shortcuts)