def APEValue(value, kind):
    if kind in (TEXT, EXTERNAL):
        if not isinstance(value, text_type):
            if PY3:
                raise TypeError("str only for text/external values")
        else:
            value = value.encode("utf-8")
    if kind == TEXT:
        return APETextValue(value, kind)
    elif kind == BINARY:
        return APEBinaryValue(value, kind)
    elif kind == EXTERNAL:
        return APEExtValue(value, kind)
    else:
        raise ValueError("kind must be TEXT, BINARY, or EXTERNAL")