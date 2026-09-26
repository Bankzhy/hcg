def get_wrap_size_limit(self, output_size, conf_req=True, qop_req=C.GSS_C_QOP_DEFAULT):
        minor_status = ffi.new('OM_uint32[1]')
        max_input_size = ffi.new('OM_uint32[1]')
        retval = C.gss_wrap_size_limit(
            minor_status,
            self._ctx[0],
            ffi.cast('int', conf_req),
            ffi.cast('gss_qop_t', qop_req),
            ffi.cast('OM_uint32', output_size),
            max_input_size
        )
        if GSS_ERROR(retval):
            if minor_status[0] and self.mech_type:
                raise _exception_for_status(retval, minor_status[0], self.mech_type)
            else:
                raise _exception_for_status(retval, minor_status[0])
        return max_input_size[0]