def prepare_additional_parameters(additional_properties, language_hints, web_detection_params):
    if language_hints is None and web_detection_params is None:
        return additional_properties
    if additional_properties is None:
        return {}
    merged_additional_parameters = deepcopy(additional_properties)
    if 'image_context' not in merged_additional_parameters:
        merged_additional_parameters['image_context'] = {}
    merged_additional_parameters['image_context']['language_hints'] = merged_additional_parameters[
        'image_context'
    ].get('language_hints', language_hints)
    merged_additional_parameters['image_context']['web_detection_params'] = merged_additional_parameters[
        'image_context'
    ].get('web_detection_params', web_detection_params)
    return merged_additional_parameters