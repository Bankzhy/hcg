def update_configuration(cfgfile=None):
    configobj.DEFAULT_INTERPOLATION = 'template'
    cfgfile = configuration_file(cfgfile)
    cfg = configobj.ConfigObj(cfgfile, configspec=cfgspec, encoding='utf-8')
    validator = Validator()
    val = cfg.validate(validator)
    if val is not True:
        raise ValueError('Invalid configuration: %s' % val)
    if len(cfg['capture']['files']) != len(cfg['capture']['flavors']):
        raise ValueError('List of files and flavors do not match')
    globals()['__config'] = cfg
    logger_init()
    if cfg['server'].get('url', '').endswith('/'):
        logger.warning('Base URL ends with /. This is most likely a '
                       'configuration error. The URL should contain nothing '
                       'of the service paths.')
    logger.info('Configuration loaded from %s' % cfgfile)
    check()
    return cfg