def transition_local(n_states, width, window='triangle', wrap=False):
    if not isinstance(n_states, int) or n_states <= 1:
        raise ParameterError('n_states={} must be a positive integer > 1')
    width = np.asarray(width, dtype=int)
    if width.ndim == 0:
        width = np.tile(width, n_states)
    if width.shape != (n_states,):
        raise ParameterError('width={} must have length equal to n_states={}'.format(width, n_states))
    if np.any(width < 1):
        raise ParameterError('width={} must be at least 1')
    transition = np.zeros((n_states, n_states), dtype=np.float)
    for i, width_i in enumerate(width):
        trans_row = pad_center(get_window(window, width_i, fftbins=False), n_states)
        trans_row = np.roll(trans_row, n_states//2 + i + 1)
        if not wrap:
            trans_row[min(n_states, i + width_i//2 + 1):] = 0
            trans_row[:max(0, i - width_i//2)] = 0
        transition[i] = trans_row
    transition /= transition.sum(axis=1, keepdims=True)
    return transition