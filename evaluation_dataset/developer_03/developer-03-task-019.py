def fix_header(filename, keyword, new_value):
    hd = read_header(filename)
    hi = read_header(filename, return_idxs=True)
    idx = hi[keyword]
    dtype = header_keyword_types[keyword]
    dtype_to_type = {b'<l'  : np.int32,
                     b'str' : bytes,
                     b'<d'  : np.float64,
                     b'angle' : to_sigproc_angle}
    value_dtype = dtype_to_type[dtype]
    if isinstance(value_dtype, bytes):
        if len(hd[keyword]) == len(new_value):
            val_str = np.int32(len(new_value)).tostring() + new_value
        else:
            raise RuntimeError("String size mismatch. Cannot update without rewriting entire file.")
    else:
        val_str = value_dtype(new_value).tostring()
    with open(filename, 'rb+') as fh:
        fh.seek(idx)
        fh.write(val_str)