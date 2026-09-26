def _exception_pprint(obj, p, cycle):
    if obj.__class__.__module__ in ('exceptions', 'builtins'):
        name = obj.__class__.__name__
    else:
        name = '%s.%s' % (
            obj.__class__.__module__,
            obj.__class__.__name__
        )
    step = len(name) + 1
    p.begin_group(step, name + '(')
    for idx, arg in enumerate(getattr(obj, 'args', ())):
        if idx:
            p.text(',')
            p.breakable()
        p.pretty(arg)
    p.end_group(step, ')')