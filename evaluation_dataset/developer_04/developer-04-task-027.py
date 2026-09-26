def _try_reduce(self) -> Tuple[bool, List[HdlStatement]]:
        io_change = False
        self.ifTrue, rank_decrease, _io_change = self._try_reduce_list(
            self.ifTrue)
        self.rank -= rank_decrease
        io_change |= _io_change
        new_elifs = []
        for cond, statements in self.elIfs:
            _statements, rank_decrease, _io_change = self._try_reduce_list(
                statements)
            self.rank -= rank_decrease
            io_change |= _io_change
            new_elifs.append((cond, _statements))
        if self.ifFalse is not None:
            self.ifFalse, rank_decrease, _io_update_required = self._try_reduce_list(
                self.ifFalse)
            self.rank -= rank_decrease
            io_change |= _io_change
        reduce_self = not self.condHasEffect(
            self.ifTrue, self.ifFalse, self.elIfs)
        if reduce_self:
            res = self.ifTrue
        else:
            res = [self, ]
        self._on_reduce(reduce_self, io_change, res)
        if self.ifFalse is not None and len(self.ifFalse) == 1:
            child = self.ifFalse[0]
            if isinstance(child, IfContainer):
                self._merge_nested_if_from_else(child)
        return res, io_change