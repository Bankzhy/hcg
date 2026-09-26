def get_credential_cache():
    from sregistry.defaults import ( CREDENTIAL_CACHE, SREGISTRY_CLIENT )
    client_credential_cache = None
    if CREDENTIAL_CACHE is not None:
        env = 'SREGISTRY_DISABLE_CREDENTIAL_%s' %SREGISTRY_CLIENT.upper()
        if os.environ.get(env) is not None:
            bot.debug('[%s] cache disabled' %SREGISTRY_CLIENT)
            CREDENTIAL_CACHE = None
    if CREDENTIAL_CACHE is not None:
        if not os.path.exists(CREDENTIAL_CACHE):
            mkdir_p(CREDENTIAL_CACHE)
        client_credential_cache = '%s/%s' %(CREDENTIAL_CACHE, SREGISTRY_CLIENT)
    if client_credential_cache is not None:
        bot.debug('credentials cache')
    return client_credential_cache