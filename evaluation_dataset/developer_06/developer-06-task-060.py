def _multirate_fb(center_freqs=None, sample_rates=None, Q=25.0,
                  passband_ripple=1, stopband_attenuation=50, ftype='ellip', flayout='ba'):
    if center_freqs is None:
        raise ParameterError('center_freqs must be provided.')
    if sample_rates is None:
        raise ParameterError('sample_rates must be provided.')
    if center_freqs.shape != sample_rates.shape:
        raise ParameterError('Number of provided center_freqs and sample_rates must be equal.')
    nyquist = 0.5 * sample_rates
    filter_bandwidths = center_freqs / float(Q)
    filterbank = []
    for cur_center_freq, cur_nyquist, cur_bw in zip(center_freqs, nyquist, filter_bandwidths):
        passband_freqs = [cur_center_freq - 0.5 * cur_bw, cur_center_freq + 0.5 * cur_bw] / cur_nyquist
        stopband_freqs = [cur_center_freq - cur_bw, cur_center_freq + cur_bw] / cur_nyquist
        cur_filter = scipy.signal.iirdesign(passband_freqs, stopband_freqs,
                                            passband_ripple, stopband_attenuation,
                                            analog=False, ftype=ftype, output=flayout)
        filterbank.append(cur_filter)
    return filterbank, sample_rates