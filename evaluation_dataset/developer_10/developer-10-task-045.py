def lag_to_recurrence(lag, axis=-1):
    if axis not in [0, 1, -1]:
        raise ParameterError('Invalid target axis: {}'.format(axis))
    axis = np.abs(axis)
    if lag.ndim != 2 or (lag.shape[0] != lag.shape[1] and
                         lag.shape[1 - axis] != 2 * lag.shape[axis]):
        raise ParameterError('Invalid lag matrix shape: {}'.format(lag.shape))
    t = lag.shape[axis]
    sparse = scipy.sparse.issparse(lag)
    if sparse:
        rec = scipy.sparse.lil_matrix(lag)
        roll_ax = 1 - axis
    else:
        rec = lag.copy()
        roll_ax = None
    idx_slice = [slice(None)] * lag.ndim
    for i in range(1, t):
        idx_slice[axis] = i
        rec[tuple(idx_slice)] = util.roll_sparse(lag[tuple(idx_slice)], i, axis=roll_ax)
    sub_slice = [slice(None)] * rec.ndim
    sub_slice[1 - axis] = slice(t)
    rec = rec[tuple(sub_slice)]
    if sparse:
        return rec.asformat(lag.format)
    return np.ascontiguousarray(rec.T).T