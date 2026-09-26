def compute_step(self, state, lstm_cell=None, input=None, additional_inputs=None):
        if not self.initialized:
            input_dim = None
            if input and hasattr(input.tag, 'last_dim'):
                input_dim = input.tag.last_dim
            self.init(input_dim)
        input_map = self.merge_inputs(input, additional_inputs=additional_inputs)
        input_map.update({"state": state, "lstm_cell": lstm_cell})
        output_map = self.compute_new_state(input_map)
        outputs = [output_map.pop("state")]
        outputs += output_map.values()
        for tensor in outputs:
            tensor.tag.last_dim = self.hidden_size
        if len(outputs) == 1:
            return outputs[0]
        else:
            return outputs