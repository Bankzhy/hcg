def down(auth_token, force, app_name):
    if not app_name:
        click.echo(
            'WARNING: Inferring the app name when deleting is deprecated. '
            'Starting with happy 2.0, the app_name parameter will be required.'
        )
    app_name = app_name or _read_app_name()
    if not app_name:
        click.echo('No app name given.')
        sys.exit(1)
    if not force:
        click.confirm(
            'Are you sure you want to delete %s?' % app_name,
            abort=True,
        )
    happy = Happy(auth_token=auth_token)
    click.echo('Destroying app %s... ' % app_name, nl=False)
    happy.delete(app_name=app_name)
    _delete_app_name_file()
    click.echo('done')
    click.echo("It's down. :(")