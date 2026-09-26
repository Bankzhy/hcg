def _might_have_parameter(fn_or_cls, arg_name):
  if inspect.isclass(fn_or_cls):
    fn = _find_class_construction_fn(fn_or_cls)
  else:
    fn = fn_or_cls
  while hasattr(fn, '__wrapped__'):
    fn = fn.__wrapped__
  arg_spec = _get_cached_arg_spec(fn)
  if six.PY3:
    if arg_spec.varkw:
      return True
    return arg_name in arg_spec.args or arg_name in arg_spec.kwonlyargs
  else:
    if arg_spec.keywords:
      return True
    return arg_name in arg_spec.args