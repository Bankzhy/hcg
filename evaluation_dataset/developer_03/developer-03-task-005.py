def authenticate(device, data, facet, check_only=False):
    if isinstance(data, string_types):
        data = json.loads(data)
    if data['version'] != VERSION:
        raise ValueError('Unsupported U2F version: %s' % data['version'])
    app_id = data.get('appId', facet)
    verify_facet(app_id, facet)
    app_param = sha256(app_id.encode('utf8')).digest()
    key_handle = websafe_decode(data['keyHandle'])
    client_data = {
        'typ': 'navigator.id.getAssertion',
        'challenge': data['challenge'],
        'origin': facet
    }
    client_data = json.dumps(client_data)
    client_param = sha256(client_data.encode('utf8')).digest()
    request = client_param + app_param + int2byte(
        len(key_handle)) + key_handle
    p1 = 0x07 if check_only else 0x03
    p2 = 0
    response = device.send_apdu(INS_SIGN, p1, p2, request)
    return {
        'clientData': websafe_encode(client_data),
        'signatureData': websafe_encode(response),
        'keyHandle': data['keyHandle']
    }