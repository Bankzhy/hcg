def print_source_location_info(print_fn, filename, lineno, fn_name=None,
                               f_lasti=None, remapped_file=None):
    if remapped_file:
        mess = '(%s:%s remapped %s' % (remapped_file, lineno, filename)
    else:
        mess = '(%s:%s' % (filename, lineno)
    if f_lasti and f_lasti != -1:
        mess += ' @%d' % f_lasti
        pass
    mess += '):'
    if fn_name and fn_name != '?':
        mess += " %s" % fn_name
        pass
    print_fn(mess)
    return