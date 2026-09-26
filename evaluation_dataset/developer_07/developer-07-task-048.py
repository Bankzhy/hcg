def mkrngs(self):
        bbool = bool_2_indices(self.bkg)
        if bbool is not None:
            self.bkgrng = self.Time[bbool]
        else:
            self.bkgrng = [[np.nan, np.nan]]
        sbool = bool_2_indices(self.sig)
        if sbool is not None:
            self.sigrng = self.Time[sbool]
        else:
            self.sigrng = [[np.nan, np.nan]]
        tbool = bool_2_indices(self.trn)
        if tbool is not None:
            self.trnrng = self.Time[tbool]
        else:
            self.trnrng = [[np.nan, np.nan]]
        self.ns = np.zeros(self.Time.size)
        n = 1
        for i in range(len(self.sig) - 1):
            if self.sig[i]:
                self.ns[i] = n
            if self.sig[i] and ~self.sig[i + 1]:
                n += 1
        self.n = int(max(self.ns))
        return