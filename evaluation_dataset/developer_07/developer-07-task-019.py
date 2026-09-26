def migrate(uri: str, archive_uri: str, case_id: str, dry: bool, force: bool):
    scout_client = MongoClient(uri)
    scout_database = scout_client[uri.rsplit('/', 1)[-1]]
    scout_adapter = MongoAdapter(database=scout_database)
    scout_case = scout_adapter.case(case_id)
    if not force and scout_case.get('is_migrated'):
        print("case already migrated")
        return
    archive_client = MongoClient(archive_uri)
    archive_database = archive_client[archive_uri.rsplit('/', 1)[-1]]
    archive_case = archive_database.case.find_one({
        'owner': scout_case['owner'],
        'display_name': scout_case['display_name']
    })
    archive_data = archive_info(archive_database, archive_case)
    if dry:
        print(ruamel.yaml.safe_dump(archive_data))
    else:
        pass