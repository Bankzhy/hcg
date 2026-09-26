def _build_key_wrapping_specification(self, value):
        if value is None:
            return None
        if not isinstance(value, dict):
            raise TypeError("Key wrapping specification must be a dictionary.")
        encryption_key_info = self._build_encryption_key_information(
            value.get('encryption_key_information')
        )
        mac_signature_key_info = self._build_mac_signature_key_information(
            value.get('mac_signature_key_information')
        )
        key_wrapping_specification = cobjects.KeyWrappingSpecification(
            wrapping_method=value.get('wrapping_method'),
            encryption_key_information=encryption_key_info,
            mac_signature_key_information=mac_signature_key_info,
            attribute_names=value.get('attribute_names'),
            encoding_option=value.get('encoding_option')
        )
        return key_wrapping_specification