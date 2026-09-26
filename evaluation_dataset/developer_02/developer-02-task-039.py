def chirp(fmin, fmax, sr=22050, length=None, duration=None, linear=False, phi=None):
    if fmin is None or fmax is None:
        raise ParameterError('both "fmin" and "fmax" must be provided')
    period = 1.0 / sr
    if length is None:
        if duration is None:
            raise ParameterError('either "length" or "duration" must be provided')
    else:
        duration = period * length
    if phi is None:
        phi = -np.pi * 0.5
    method = 'linear' if linear else 'logarithmic'
    return scipy.signal.chirp(
        np.arange(duration, step=period),
        fmin,
        duration,
        fmax,
        method=method,
        phi=phi / np.pi * 180,
    )