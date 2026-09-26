def _evolve(self, state, qargs=None):
        if qargs is not None:
            return SuperOp(self)._evolve(state, qargs)
        state = self._format_state(state)
        if state.shape[0] != self._input_dim:
            raise QiskitError(
                "QuantumChannel input dimension is not equal to state dimension."
            )
        if state.ndim == 1 and self._data[1] is None and len(
                self._data[0]) == 1:
            return np.dot(self._data[0][0], state)
        state = self._format_state(state, density_matrix=True)
        kraus_l, kraus_r = self._data
        if kraus_r is None:
            kraus_r = kraus_l
        return np.einsum('AiB,BC,AjC->ij', kraus_l, state,
                         np.conjugate(kraus_r))