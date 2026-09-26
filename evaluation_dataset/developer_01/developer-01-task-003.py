def validate_grant_type(self, client_id, grant_type, client, request,
                            *args, **kwargs):
        if self._usergetter is None and grant_type == 'password':
            log.debug('Password credential authorization is disabled.')
            return False
        default_grant_types = (
            'authorization_code', 'password',
            'client_credentials', 'refresh_token',
        )
        if hasattr(client, 'allowed_grant_types'):
            if grant_type not in client.allowed_grant_types:
                return False
        else:
            if grant_type not in default_grant_types:
                return False
        if grant_type == 'client_credentials':
            if not hasattr(client, 'user'):
                log.debug('Client should have a user property')
                return False
            request.user = client.user
        return True