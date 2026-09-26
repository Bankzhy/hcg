def _convert_from_thrift_endpoint(self, thrift_endpoint):
        ipv4 = None
        ipv6 = None
        port = struct.unpack('H', struct.pack('h', thrift_endpoint.port))[0]
        if thrift_endpoint.ipv4 != 0:
            ipv4 = socket.inet_ntop(
                socket.AF_INET,
                struct.pack('!i', thrift_endpoint.ipv4),
            )
        if thrift_endpoint.ipv6:
            ipv6 = socket.inet_ntop(socket.AF_INET6, thrift_endpoint.ipv6)
        return Endpoint(
            service_name=thrift_endpoint.service_name,
            ipv4=ipv4,
            ipv6=ipv6,
            port=port,
        )