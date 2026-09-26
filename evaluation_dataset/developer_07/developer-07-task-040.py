def _multiplex(self, target_gate, list_of_angles):
        list_len = len(list_of_angles)
        local_num_qubits = int(math.log2(list_len)) + 1
        q = QuantumRegister(local_num_qubits)
        circuit = QuantumCircuit(q, name="multiplex" + local_num_qubits.__str__())
        lsb = q[0]
        msb = q[local_num_qubits - 1]
        if local_num_qubits == 1:
            circuit.append(target_gate(list_of_angles[0]), [q[0]])
            return circuit
        angle_weight = scipy.kron([[0.5, 0.5], [0.5, -0.5]],
                                  np.identity(2 ** (local_num_qubits - 2)))
        list_of_angles = angle_weight.dot(np.array(list_of_angles)).tolist()
        multiplex_1 = self._multiplex(target_gate, list_of_angles[0:(list_len // 2)])
        circuit.append(multiplex_1.to_instruction(), q[0:-1])
        circuit.append(CnotGate(), [msb, lsb])
        multiplex_2 = self._multiplex(target_gate, list_of_angles[(list_len // 2):])
        if list_len > 1:
            circuit.append(multiplex_2.to_instruction().mirror(), q[0:-1])
        else:
            circuit.append(multiplex_2.to_instruction(), q[0:-1])
        circuit.append(CnotGate(), [msb, lsb])
        return circuit