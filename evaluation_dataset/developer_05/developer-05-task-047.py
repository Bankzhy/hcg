def salience(S, freqs, h_range, weights=None, aggregate=None,
             filter_peaks=True, fill_value=np.nan,  kind='linear', axis=0):
    if aggregate is None:
        aggregate = np.average
    if weights is None:
        weights = np.ones((len(h_range), ))
    else:
        weights = np.array(weights, dtype=float)
    S_harm = interp_harmonics(S, freqs, h_range, kind=kind, axis=axis)
    if aggregate is np.average:
        S_sal = aggregate(S_harm, axis=0, weights=weights)
    else:
        S_sal = aggregate(S_harm, axis=0)
    if filter_peaks:
        S_peaks = scipy.signal.argrelmax(S, axis=0)
        S_out = np.empty(S.shape)
        S_out.fill(fill_value)
        S_out[S_peaks[0], S_peaks[1]] = S_sal[S_peaks[0], S_peaks[1]]
        S_sal = S_out
    return S_sal