def verify(cert, signature, data, digest):
    data = _text_to_bytes_and_warn("data", data)
    digest_obj = _lib.EVP_get_digestbyname(_byte_string(digest))
    if digest_obj == _ffi.NULL:
        raise ValueError("No such digest method")
    pkey = _lib.X509_get_pubkey(cert._x509)
    _openssl_assert(pkey != _ffi.NULL)
    pkey = _ffi.gc(pkey, _lib.EVP_PKEY_free)
    md_ctx = _lib.Cryptography_EVP_MD_CTX_new()
    md_ctx = _ffi.gc(md_ctx, _lib.Cryptography_EVP_MD_CTX_free)
    _lib.EVP_VerifyInit(md_ctx, digest_obj)
    _lib.EVP_VerifyUpdate(md_ctx, data, len(data))
    verify_result = _lib.EVP_VerifyFinal(
        md_ctx, signature, len(signature), pkey
    )
    if verify_result != 1:
        _raise_current_error()