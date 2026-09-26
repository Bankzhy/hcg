def chroma_cqt(y=None, sr=22050, C=None, hop_length=512, fmin=None,
               norm=np.inf, threshold=0.0, tuning=None, n_chroma=12,
               n_octaves=7, window=None, bins_per_octave=None, cqt_mode='full'):
    cqt_func = {'full': cqt, 'hybrid': hybrid_cqt}
    if bins_per_octave is None:
        bins_per_octave = n_chroma
    if C is None:
        C = np.abs(cqt_func[cqt_mode](y, sr=sr,
                                      hop_length=hop_length,
                                      fmin=fmin,
                                      n_bins=n_octaves * bins_per_octave,
                                      bins_per_octave=bins_per_octave,
                                      tuning=tuning))
    cq_to_chr = filters.cq_to_chroma(C.shape[0],
                                     bins_per_octave=bins_per_octave,
                                     n_chroma=n_chroma,
                                     fmin=fmin,
                                     window=window)
    chroma = cq_to_chr.dot(C)
    if threshold is not None:
        chroma[chroma < threshold] = 0.0
    if norm is not None:
        chroma = util.normalize(chroma, norm=norm, axis=0)
    return chroma