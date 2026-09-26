def _report_message(message, level, request, extra_data, payload_data):
    if not _check_config():
        return
    filtered_message = events.on_message(message,
                                         request=request,
                                         extra_data=extra_data,
                                         payload_data=payload_data,
                                         level=level)
    if filtered_message is False:
        return
    data = _build_base_data(request, level=level)
    data['body'] = {
        'message': {
            'body': filtered_message
        }
    }
    if extra_data:
        extra_data = extra_data
        data['body']['message'].update(extra_data)
    request = _get_actual_request(request)
    _add_request_data(data, request)
    _add_person_data(data, request)
    _add_lambda_context_data(data)
    data['server'] = _build_server_data()
    if payload_data:
        data = dict_merge(data, payload_data)
    payload = _build_payload(data)
    send_payload(payload, payload.get('access_token'))
    return data['uuid']