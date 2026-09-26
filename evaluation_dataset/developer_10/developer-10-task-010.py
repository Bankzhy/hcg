def make_response(self, rv):
        status = headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if rv is None:
            raise ValueError('View function did not return a response')
        if not isinstance(rv, self.response_class):
            if isinstance(rv, (text_type, bytes, bytearray)):
                rv = self.response_class(rv, headers=headers, status=status)
                headers = status = None
            else:
                rv = self.response_class.force_type(rv, request.environ)
        if status is not None:
            if isinstance(status, string_types):
                rv.status = status
            else:
                rv.status_code = status
        if headers:
            rv.headers.extend(headers)
        return rv