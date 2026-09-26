def _build_purchase_item(course_id, course_url, cost_in_cents, mode, course_data, sku):
    item = {
        'id': "{}-{}".format(course_id, mode),
        'url': course_url,
        'price': cost_in_cents,
        'qty': 1,
    }
    if 'title' in course_data:
        item['title'] = course_data['title']
    else:
        item['title'] = 'Course {} mode: {}'.format(course_id, mode)
    if 'tags' in course_data:
        item['tags'] = course_data['tags']
    item['vars'] = dict(course_data.get('vars', {}), mode=mode, course_run_id=course_id)
    item['vars']['purchase_sku'] = sku
    return item