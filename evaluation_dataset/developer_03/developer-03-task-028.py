def extract_constant(code, symbol, default=-1):
    if symbol not in code.co_names:
        return None
    name_idx = list(code.co_names).index(symbol)
    STORE_NAME = 90
    STORE_GLOBAL = 97
    LOAD_CONST = 100
    const = default
    for op, arg in _iter_code(code):
        if op==LOAD_CONST:
            const = code.co_consts[arg]
        elif arg==name_idx and (op==STORE_NAME or op==STORE_GLOBAL):
            return const
        else:
            const = default