def load_pkcs7_data(type, buffer):
    if isinstance(buffer, _text_type):
        buffer = buffer.encode("ascii")
    bio = _new_mem_buf(buffer)
    if type == FILETYPE_PEM:
        pkcs7 = _lib.PEM_read_bio_PKCS7(bio, _ffi.NULL, _ffi.NULL, _ffi.NULL)
    elif type == FILETYPE_ASN1:
        pkcs7 = _lib.d2i_PKCS7_bio(bio, _ffi.NULL)
    else:
        raise ValueError("type argument must be FILETYPE_PEM or FILETYPE_ASN1")
    if pkcs7 == _ffi.NULL:
        _raise_current_error()
    pypkcs7 = PKCS7.__new__(PKCS7)
    pypkcs7._pkcs7 = _ffi.gc(pkcs7, _lib.PKCS7_free)
    return pypkcs7