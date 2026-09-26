def _resolve_distribution_names(dist_fn_args, dist_names, leaf_name):
  if dist_names is None:
    dist_names = []
  else:
    dist_names = dist_names.copy()
  n = len(dist_fn_args)
  dist_names.extend([None]*(n - len(dist_names)))
  for i_, args in enumerate(reversed(dist_fn_args)):
    if not args:
      continue
    i = n - i_ - 1
    for j, arg_name in enumerate(args):
      dist_names[i - j - 1] = arg_name
  j = 0
  for i_ in range(len(dist_names)):
    i = n - i_ - 1
    if dist_names[i] is None:
      dist_names[i] = leaf_name if j == 0 else leaf_name + str(j)
      j += 1
  return tuple(dist_names)