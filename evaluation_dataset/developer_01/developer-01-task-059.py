def read(self, istream, kmip_version=enums.KMIPVersion.KMIP_1_0):
        super(ExtensionInformation, self).read(
            istream,
            kmip_version=kmip_version
        )
        tstream = BytearrayStream(istream.read(self.length))
        self.extension_name.read(tstream, kmip_version=kmip_version)
        if self.is_tag_next(Tags.EXTENSION_TAG, tstream):
            self.extension_tag = ExtensionTag()
            self.extension_tag.read(tstream, kmip_version=kmip_version)
        if self.is_tag_next(Tags.EXTENSION_TYPE, tstream):
            self.extension_type = ExtensionType()
            self.extension_type.read(tstream, kmip_version=kmip_version)
        self.is_oversized(tstream)
        self.validate()