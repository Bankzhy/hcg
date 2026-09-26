def read_next_data_block(self):
        header, data_idx = self.read_header()
        self.file_obj.seek(data_idx)
        n_chan = int(header['OBSNCHAN'])
        n_pol = int(header['NPOL'])
        n_bit = int(header['NBITS'])
        n_samples = int(int(header['BLOCSIZE']) / (n_chan * n_pol * (n_bit / 8)))
        d = np.ascontiguousarray(np.fromfile(self.file_obj, count=header['BLOCSIZE'], dtype='int8'))
        if n_bit != 8:
            d = unpack(d, n_bit)
        dshape = self.read_next_data_block_shape()
        d = d.reshape(dshape)
        if self._d.shape != d.shape:
            self._d = np.zeros(d.shape, dtype='float32')
        self._d[:] = d
        return header, self._d[:].view('complex64')