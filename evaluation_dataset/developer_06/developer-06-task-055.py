def _finish_log_prob_for_one_fiber(self, y, x, ildj, event_ndims,
                                     **distribution_kwargs):
    x = self._maybe_rotate_dims(x, rotate_right=True)
    log_prob = self.distribution.log_prob(x, **distribution_kwargs)
    if self._is_maybe_event_override:
      log_prob = tf.reduce_sum(
          input_tensor=log_prob, axis=self._reduce_event_indices)
    log_prob += tf.cast(ildj, log_prob.dtype)
    if self._is_maybe_event_override and isinstance(event_ndims, int):
      tensorshape_util.set_shape(
          log_prob,
          tf.broadcast_static_shape(
              tensorshape_util.with_rank_at_least(y.shape, 1)[:-event_ndims],
              self.batch_shape))
    return log_prob