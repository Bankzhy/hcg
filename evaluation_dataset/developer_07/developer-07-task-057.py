def matchmaker_match(institute_id, case_name, target):
    institute_obj, case_obj = institute_and_case(store, institute_id, case_name)
    user_obj = store.user(current_user.email)
    if 'mme_submitter' not in user_obj['roles']:
        flash('unauthorized request', 'warning')
        return redirect(request.referrer)
    mme_base_url = current_app.config.get('MME_URL')
    mme_accepts = current_app.config.get('MME_ACCEPTS')
    mme_token = current_app.config.get('MME_TOKEN')
    nodes = current_app.mme_nodes
    if not mme_base_url or not mme_token or not mme_accepts:
        flash('An error occurred reading matchmaker connection parameters. Please check config file!', 'danger')
        return redirect(request.referrer)
    match_results = controllers.mme_match(case_obj, target, mme_base_url, mme_token, nodes, mme_accepts)
    ok_responses = 0
    for match_results in match_results:
        match_results['status_code'] == 200
        ok_responses +=1
    if ok_responses:
        flash("Match request sent. Look for eventual matches in 'Matches' page.", 'info')
    else:
        flash('An error occurred while sending match request.', 'danger')
    return redirect(request.referrer)