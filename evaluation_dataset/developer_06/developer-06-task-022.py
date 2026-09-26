def _get_argspec(func):
    if inspect.isclass(func):
        func = func.__init__
    if not inspect.isfunction(func):
        return [], False
    parameters = inspect.signature(func).parameters
    args = []
    uses_starstar = False
    for par in parameters.values():
        if (par.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD or
                    par.kind == inspect.Parameter.KEYWORD_ONLY):
            args.append(par.name)
        elif par.kind == inspect.Parameter.VAR_KEYWORD:
            uses_starstar = True
    return args, uses_starstar