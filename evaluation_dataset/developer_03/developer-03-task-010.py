def _from_operator(rep, data, input_dim, output_dim):
    if rep == 'Operator':
        return data
    if rep == 'SuperOp':
        return np.kron(np.conj(data), data)
    if rep == 'Choi':
        vec = np.ravel(data, order='F')
        return np.outer(vec, np.conj(vec))
    if rep == 'Kraus':
        return ([data], None)
    if rep == 'Stinespring':
        return (data, None)
    if rep == 'Chi':
        _check_nqubit_dim(input_dim, output_dim)
        data = _from_operator('Choi', data, input_dim, output_dim)
        return _choi_to_chi(data, input_dim, output_dim)
    if rep == 'PTM':
        _check_nqubit_dim(input_dim, output_dim)
        data = _from_operator('SuperOp', data, input_dim, output_dim)
        return _superop_to_ptm(data, input_dim, output_dim)
    raise QiskitError('Invalid QuantumChannel {}'.format(rep))