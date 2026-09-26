def export(self, cert, key, type=FILETYPE_PEM, days=100,
               digest=_UNSPECIFIED):
        if not isinstance(cert, X509):
            raise TypeError("cert must be an X509 instance")
        if not isinstance(key, PKey):
            raise TypeError("key must be a PKey instance")
        if not isinstance(type, int):
            raise TypeError("type must be an integer")
        if digest is _UNSPECIFIED:
            raise TypeError("digest must be provided")
        digest_obj = _lib.EVP_get_digestbyname(digest)
        if digest_obj == _ffi.NULL:
            raise ValueError("No such digest method")
        bio = _lib.BIO_new(_lib.BIO_s_mem())
        _openssl_assert(bio != _ffi.NULL)
        sometime = _lib.ASN1_TIME_new()
        _openssl_assert(sometime != _ffi.NULL)
        _lib.X509_gmtime_adj(sometime, 0)
        _lib.X509_CRL_set_lastUpdate(self._crl, sometime)
        _lib.X509_gmtime_adj(sometime, days * 24 * 60 * 60)
        _lib.X509_CRL_set_nextUpdate(self._crl, sometime)
        _lib.X509_CRL_set_issuer_name(
            self._crl, _lib.X509_get_subject_name(cert._x509)
        )
        sign_result = _lib.X509_CRL_sign(self._crl, key._pkey, digest_obj)
        if not sign_result:
            _raise_current_error()
        return dump_crl(type, self)