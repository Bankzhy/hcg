def cases(institute_id):
    institute_obj = institute_and_case(store, institute_id)
    query = request.args.get('query')
    limit = 100
    if request.args.get('limit'):
        limit = int(request.args.get('limit'))
    skip_assigned = request.args.get('skip_assigned')
    is_research = request.args.get('is_research')
    all_cases = store.cases(collaborator=institute_id, name_query=query,
                        skip_assigned=skip_assigned, is_research=is_research)
    data = controllers.cases(store, all_cases, limit)
    sanger_unevaluated = controllers.get_sanger_unevaluated(store, institute_id, current_user.email)
    if len(sanger_unevaluated)> 0:
        data['sanger_unevaluated'] = sanger_unevaluated
    return dict(institute=institute_obj, skip_assigned=skip_assigned,
                is_research=is_research, query=query, **data)