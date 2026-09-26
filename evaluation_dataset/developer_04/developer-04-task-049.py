def _odds_val(self):
        if len(self.odds) == 0:
            self.odds = [(1.00, [self.min, self.max])]
        rand_val = rand.random()
        total = 0
        for percent,v in self.odds:
            if total <= rand_val < total+percent:
                found_v = v
                break
            total += percent
        res = None
        if isinstance(v, (tuple,list)):
            rand_func = rand.randfloat if type(v[0]) is float else rand.randint
            if len(v) == 2:
                res = rand_func(v[0], v[1])
            elif len(v) == 1:
                res = v[0]
        else:
            res = v
        return res