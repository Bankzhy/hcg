def set_hosts(hosts, use_ssl=False, ssl_cert_path=None):
    if type(hosts) != list:
        hosts = [hosts]
    conn_params = {
        "hosts": hosts,
        "timeout": 20
    }
    if use_ssl:
        conn_params['use_ssl'] = True
        if ssl_cert_path:
            conn_params['verify_certs'] = True
            conn_params['ca_certs'] = ssl_cert_path
        else:
            conn_params['verify_certs'] = False
    connections.create_connection(**conn_params)