def read(self, input_stream, kmip_version=enums.KMIPVersion.KMIP_1_0):
        super(ObtainLeaseResponsePayload, self).read(
            input_stream,
            kmip_version=kmip_version
        )
        local_stream = utils.BytearrayStream(input_stream.read(self.length))
        if self.is_tag_next(enums.Tags.UNIQUE_IDENTIFIER, local_stream):
            self._unique_identifier = primitives.TextString(
                tag=enums.Tags.UNIQUE_IDENTIFIER
            )
            self._unique_identifier.read(
                local_stream,
                kmip_version=kmip_version
            )
        if self.is_tag_next(enums.Tags.LEASE_TIME, local_stream):
            self._lease_time = primitives.Interval(
                tag=enums.Tags.LEASE_TIME
            )
            self._lease_time.read(local_stream, kmip_version=kmip_version)
        if self.is_tag_next(enums.Tags.LAST_CHANGE_DATE, local_stream):
            self._last_change_date = primitives.DateTime(
                tag=enums.Tags.LAST_CHANGE_DATE
            )
            self._last_change_date.read(
                local_stream,
                kmip_version=kmip_version
            )
        self.is_oversized(local_stream)