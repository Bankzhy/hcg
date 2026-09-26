def get_case_groups(adapter, total_cases, institute_id=None, slice_query=None):
    cases = [{'status': 'all', 'count': total_cases, 'percent': 1}]
    pipeline = []
    group = {'$group' : {'_id': '$status', 'count': {'$sum': 1}}}
    subquery = {}
    if institute_id and slice_query:
        subquery = adapter.cases(owner=institute_id, name_query=slice_query,
                              yield_query=True)
    elif institute_id:
        subquery = adapter.cases(owner=institute_id, yield_query=True)
    elif slice_query:
        subquery = adapter.cases(name_query=slice_query, yield_query=True)
    query = {'$match': subquery} if subquery else {}
    if query:
        pipeline.append(query)
    pipeline.append(group)
    res = adapter.case_collection.aggregate(pipeline)
    for status_group in res:
        cases.append({'status': status_group['_id'],
                      'count': status_group['count'],
                      'percent': status_group['count'] / total_cases})
    return cases