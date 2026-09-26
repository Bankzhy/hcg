def encode(self):
        header    = bytearray(1)
        varHeader = bytearray()
        payload   = bytearray()
        if self.qos:
            header[0] = 0x30 | self.retain | (self.qos << 1) | (self.dup << 3)
            varHeader.extend(encodeString(self.topic))
            varHeader.extend(encode16Int(self.msgId))
        else:
            header[0] = 0x30 | self.retain
            varHeader.extend(encodeString(self.topic))
        if isinstance(self.payload, bytearray):
            payload.extend(self.payload)
        elif isinstance(self.payload, str):
            payload.extend(bytearray(self.payload, encoding='utf-8'))
        else:
            raise PayloadTypeError(type(self.payload))
        totalLen = len(varHeader) + len(payload)
        if totalLen > 268435455:
            raise PayloadValueError(totalLen)
        header.extend(encodeLength(totalLen))
        header.extend(varHeader)
        header.extend(payload)
        self.encoded = header
        return str(header) if PY2 else bytes(header)