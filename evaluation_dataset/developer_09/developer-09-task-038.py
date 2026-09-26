def reconstruct_anc(self, method='probabilistic', infer_gtr=False,
                        marginal=False, **kwargs):
        self.logger("TreeAnc.infer_ancestral_sequences with method: %s, %s"%(method, 'marginal' if marginal else 'joint'), 1)
        if (self.tree is None) or (self.aln is None):
            self.logger("TreeAnc.infer_ancestral_sequences: ERROR, alignment or tree are missing", 0)
            return ttconf.ERROR
        if method in ['ml', 'probabilistic']:
            if marginal:
                _ml_anc = self._ml_anc_marginal
            else:
                _ml_anc = self._ml_anc_joint
        else:
            _ml_anc = self._fitch_anc
        if infer_gtr:
            tmp = self.infer_gtr(marginal=marginal, **kwargs)
            if tmp==ttconf.ERROR:
                return tmp
            N_diff = _ml_anc(**kwargs)
        else:
            N_diff = _ml_anc(**kwargs)
        return N_diff