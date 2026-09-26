def compute_alignments(self, prev_state, precomputed_values, mask=None):
        WaSp = T.dot(prev_state, self.Wa)
        UaH = precomputed_values
        if UaH.ndim == 2:
            preact = WaSp[:, None, :] + UaH[None, :, :]
        else:
            preact = WaSp[:, None, :] + UaH
        act = T.activate(preact, 'tanh')
        align_scores = T.dot(act, self.Va)
        if mask:
            mask = (1 - mask) * -99.00
            if align_scores.ndim == 3:
                align_scores += mask[None, :]
            else:
                align_scores += mask
        align_weights = T.nnet.softmax(align_scores)
        return align_weights