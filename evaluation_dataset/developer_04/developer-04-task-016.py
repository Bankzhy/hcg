def get_ip_address_info(ip_address, cache=None, nameservers=None,
                        timeout=2.0, parallel=False):
    ip_address = ip_address.lower()
    if cache:
        info = cache.get(ip_address, None)
        if info:
            return info
    info = OrderedDict()
    info["ip_address"] = ip_address
    reverse_dns = get_reverse_dns(ip_address,
                                  nameservers=nameservers,
                                  timeout=timeout)
    country = get_ip_address_country(ip_address, parallel=parallel)
    info["country"] = country
    info["reverse_dns"] = reverse_dns
    info["base_domain"] = None
    if reverse_dns is not None:
        base_domain = get_base_domain(reverse_dns)
        info["base_domain"] = base_domain
    return info