def add(self, s):
        if self.is_terminated:
            raise TypeError("Impossible to add string to fitted trie")
        if s == "":
            self._set_final(self.root)
            return
        curr = self.root
        for i, a in enumerate(s):
            code = self.alphabet_codes[a]
            next = self.graph[curr][code]
            if next == Trie.NO_NODE:
                curr = self._add_descendant(curr, s[i:])
                break
            else:
                curr = next
        self._set_final(curr)
        return self