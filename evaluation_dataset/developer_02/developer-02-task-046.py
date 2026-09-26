def _setup_freqs(self, f_start=None, f_stop=None):
        f0 = self.header[b'fch1']
        f_delt = self.header[b'foff']
        i_start, i_stop = 0, self.header[b'nchans']
        if f_start:
            i_start = int((f_start - f0) / f_delt)
        if f_stop:
            i_stop  = int((f_stop - f0)  / f_delt)
        chan_start_idx = np.int(i_start)
        chan_stop_idx  = np.int(i_stop)
        if i_start < i_stop:
            i_vals = np.arange(chan_start_idx, chan_stop_idx)
        else:
            i_vals = np.arange(chan_stop_idx, chan_start_idx)
        self.freqs = f_delt * i_vals + f0
        if chan_stop_idx < chan_start_idx:
            chan_stop_idx, chan_start_idx = chan_start_idx,chan_stop_idx
        return i_start, i_stop, chan_start_idx, chan_stop_idx