def _to_superop(rep, data, input_dim, output_dim):
    if rep == 'SuperOp':
        return data
    if rep == 'Operator':
        return _from_operator('SuperOp', data, input_dim, output_dim)
    if rep == 'Choi':
        return _choi_to_superop(data, input_dim, output_dim)
    if rep == 'Kraus':
        return _kraus_to_superop(data, input_dim, output_dim)
    if rep == 'Chi':
        data = _chi_to_choi(data, input_dim, output_dim)
        return _choi_to_superop(data, input_dim, output_dim)
    if rep == 'PTM':
        return _ptm_to_superop(data, input_dim, output_dim)
    if rep == 'Stinespring':
        return _stinespring_to_superop(data, input_dim, output_dim)
    raise QiskitError('Invalid QuantumChannel {}'.format(rep))