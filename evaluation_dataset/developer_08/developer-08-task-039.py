def read_next_data_block_int8(self):
        header, data_idx = self.read_header()
        self.file_obj.seek(data_idx)
        n_chan = int(header['OBSNCHAN'])
        n_pol = int(header['NPOL'])
        n_bit = int(header['NBITS'])
        n_samples = int(int(header['BLOCSIZE']) / (n_chan * n_pol * (n_bit / 8)))
        d = np.fromfile(self.file_obj, count=header['BLOCSIZE'], dtype='int8')
        if n_bit != 8:
            d = unpack(d, n_bit)
        d = d.reshape((n_chan, n_samples, n_pol))
        if self._d_x.shape != d[..., 0:2].shape:
            self._d_x = np.ascontiguousarray(np.zeros(d[..., 0:2].shape, dtype='int8'))
            self._d_y = np.ascontiguousarray(np.zeros(d[..., 2:4].shape, dtype='int8'))
        self._d_x[:] = d[..., 0:2]
        self._d_y[:] = d[..., 2:4]
        return header, self._d_x, self._d_y