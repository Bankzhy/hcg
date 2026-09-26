def is_token_from_emulator(auth_header: str) -> bool:
        if not auth_header:
            return False
        parts = auth_header.split(' ')
        if len(parts) != 2:
            return False
        auth_scheme = parts[0]
        bearer_token = parts[1]
        if auth_scheme != 'Bearer':
            return False
        token = jwt.decode(bearer_token, verify=False)
        if not token:
            return False
        issuer = token['iss']
        if not issuer:
            return False
        issuer_list = EmulatorValidation.TO_BOT_FROM_EMULATOR_TOKEN_VALIDATION_PARAMETERS.issuer
        if issuer_list and not issuer in issuer_list:
            return False
        return True