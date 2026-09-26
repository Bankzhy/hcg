def constant_q_lengths(sr, fmin, n_bins=84, bins_per_octave=12,
                       tuning=0.0, window='hann', filter_scale=1):
    if fmin <= 0:
        raise ParameterError('fmin must be positive')
    if bins_per_octave <= 0:
        raise ParameterError('bins_per_octave must be positive')
    if filter_scale <= 0:
        raise ParameterError('filter_scale must be positive')
    if n_bins <= 0 or not isinstance(n_bins, int):
        raise ParameterError('n_bins must be a positive integer')
    correction = 2.0**(float(tuning) / bins_per_octave)
    fmin = correction * fmin
    Q = float(filter_scale) / (2.0**(1. / bins_per_octave) - 1)
    freq = fmin * (2.0 ** (np.arange(n_bins, dtype=float) / bins_per_octave))
    if freq[-1] * (1 + 0.5 * window_bandwidth(window) / Q) > sr / 2.0:
        raise ParameterError('Filter pass-band lies beyond Nyquist')
    lengths = Q * sr / freq
    return lengths