def transition_cycle(n_states, prob):
    if not isinstance(n_states, int) or n_states <= 1:
        raise ParameterError('n_states={} must be a positive integer > 1')
    transition = np.zeros((n_states, n_states), dtype=np.float)
    prob = np.asarray(prob, dtype=np.float)
    if prob.ndim == 0:
        prob = np.tile(prob, n_states)
    if prob.shape != (n_states,):
        raise ParameterError('prob={} must have length equal to n_states={}'.format(prob, n_states))
    if np.any(prob < 0) or np.any(prob > 1):
        raise ParameterError('prob={} must have values in the range [0, 1]'.format(prob))
    for i, prob_i in enumerate(prob):
        transition[i, np.mod(i + 1, n_states)] = 1. - prob_i
        transition[i, i] = prob_i
    return transition