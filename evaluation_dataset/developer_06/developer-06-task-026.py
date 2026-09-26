def _broadcast_cat_event_and_params(event, params, base_dtype):
  if dtype_util.is_integer(event.dtype):
    pass
  elif dtype_util.is_floating(event.dtype):
    event = tf.cast(event, dtype=tf.int32)
  else:
    raise TypeError("`value` should have integer `dtype` or "
                    "`self.dtype` ({})".format(base_dtype))
  shape_known_statically = (
      tensorshape_util.rank(params.shape) is not None and
      tensorshape_util.is_fully_defined(params.shape[:-1]) and
      tensorshape_util.is_fully_defined(event.shape))
  if not shape_known_statically or params.shape[:-1] != event.shape:
    params *= tf.ones_like(event[..., tf.newaxis],
                           dtype=params.dtype)
    params_shape = tf.shape(input=params)[:-1]
    event *= tf.ones(params_shape, dtype=event.dtype)
    if tensorshape_util.rank(params.shape) is not None:
      tensorshape_util.set_shape(event, params.shape[:-1])
  return event, params