def add(self, dist, entry=None, insert=True, replace=False):
        if insert:
            dist.insert_on(self.entries, entry)
        if entry is None:
            entry = dist.location
        keys = self.entry_keys.setdefault(entry,[])
        keys2 = self.entry_keys.setdefault(dist.location,[])
        if not replace and dist.key in self.by_key:
            return
        self.by_key[dist.key] = dist
        if dist.key not in keys:
            keys.append(dist.key)
        if dist.key not in keys2:
            keys2.append(dist.key)
        self._added_new(dist)