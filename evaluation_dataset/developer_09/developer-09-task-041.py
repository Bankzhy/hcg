def read(self, input_buffer, kmip_version=enums.KMIPVersion.KMIP_2_0):
        if kmip_version < enums.KMIPVersion.KMIP_2_0:
            raise exceptions.VersionNotSupported(
                "KMIP {} does not support the DefaultsInformation "
                "object.".format(
                    kmip_version.value
                )
            )
        super(DefaultsInformation, self).read(
            input_buffer,
            kmip_version=kmip_version
        )
        local_buffer = utils.BytearrayStream(input_buffer.read(self.length))
        object_defaults = []
        while self.is_tag_next(enums.Tags.OBJECT_DEFAULTS, local_buffer):
            object_default = ObjectDefaults()
            object_default.read(local_buffer, kmip_version=kmip_version)
            object_defaults.append(object_default)
        if len(object_defaults) == 0:
            raise exceptions.InvalidKmipEncoding(
                "The DefaultsInformation encoding is missing the object "
                "defaults structure."
            )
        else:
            self._object_defaults = object_defaults
        self.is_oversized(local_buffer)