def mac(self, data, uid=None, algorithm=None):
        if not isinstance(data, six.binary_type):
            raise TypeError("data must be bytes")
        if uid is not None:
            if not isinstance(uid, six.string_types):
                raise TypeError("uid must be a string")
        if algorithm is not None:
            if not isinstance(algorithm, enums.CryptographicAlgorithm):
                raise TypeError(
                    "algorithm must be a CryptographicAlgorithm enumeration")
        parameters_attribute = self._build_cryptographic_parameters(
            {'cryptographic_algorithm': algorithm}
        )
        result = self.proxy.mac(data, uid, parameters_attribute)
        status = result.result_status.value
        if status == enums.ResultStatus.SUCCESS:
            uid = result.uuid.value
            mac_data = result.mac_data.value
            return uid, mac_data
        else:
            reason = result.result_reason.value
            message = result.result_message.value
            raise exceptions.KmipOperationFailure(status, reason, message)