def verify(
            cls,
            timestamp: int,
            message_hash: SHA512Hash,
            signature: bytes,
    ) -> bool:
        if timestamp < 1496176860:
            verifier = cls._VERIFIER_20130905
        elif timestamp < 1502202360:
            verifier = None
        else:
            verifier = cls._VERIFIER_20170808
        if verifier:
            result = verifier.verify(
                message_hash,
                signature,
            )
        else:
            result = False
        if isinstance(result, int):
            result = True if result == 1 else False
        return result