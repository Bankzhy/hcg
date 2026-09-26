def cache_from_source(path, debug_override=None):
    debug = not sys.flags.optimize if debug_override is None else debug_override
    if debug:
        suffixes = DEBUG_BYTECODE_SUFFIXES
    else:
        suffixes = OPTIMIZED_BYTECODE_SUFFIXES
        pass
    head, tail = os.path.split(path)
    base_filename, sep, _ = tail.partition('.')
    if not hasattr(sys, 'implementation'):
        raise NotImplementedError('No sys.implementation')
    tag = sys.implementation.cache_tag
    if tag is None:
        raise NotImplementedError('sys.implementation.cache_tag is None')
    filename = ''.join([base_filename, sep, tag, suffixes[0]])
    return os.path.join(head, _PYCACHE, filename)