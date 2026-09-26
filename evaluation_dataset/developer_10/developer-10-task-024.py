def spectral_bandwidth(y=None, sr=22050, S=None, n_fft=2048, hop_length=512,
                       win_length=None, window='hann', center=True, pad_mode='reflect',
                       freq=None, centroid=None, norm=True, p=2):
    S, n_fft = _spectrogram(y=y, S=S, n_fft=n_fft, hop_length=hop_length,
                            win_length=win_length, window=window, center=center,
                            pad_mode=pad_mode)
    if not np.isrealobj(S):
        raise ParameterError('Spectral bandwidth is only defined '
                             'with real-valued input')
    elif np.any(S < 0):
        raise ParameterError('Spectral bandwidth is only defined '
                             'with non-negative energies')
    if centroid is None:
        centroid = spectral_centroid(y=y, sr=sr, S=S,
                                     n_fft=n_fft,
                                     hop_length=hop_length,
                                     freq=freq)
    if freq is None:
        freq = fft_frequencies(sr=sr, n_fft=n_fft)
    if freq.ndim == 1:
        deviation = np.abs(np.subtract.outer(freq, centroid[0]))
    else:
        deviation = np.abs(freq - centroid[0])
    if norm:
        S = util.normalize(S, norm=1, axis=0)
    return np.sum(S * deviation**p, axis=0, keepdims=True)**(1./p)