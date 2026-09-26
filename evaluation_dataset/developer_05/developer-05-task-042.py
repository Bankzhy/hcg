def dump(filename, dbname, username=None, password=None, host=None,
    port=None, tempdir='/tmp', pg_dump_path='pg_dump', format='p'):
    filepath = os.path.join(tempdir, filename)
    cmd = pg_dump_path
    cmd += ' --format %s' % format
    cmd += ' --file ' + os.path.join(tempdir, filename)
    if username:
        cmd += ' --username %s' % username
    if host:
        cmd += ' --host %s' % host
    if port:
        cmd += ' --port %s' % port
    cmd += ' ' + dbname
    if password:
        os.environ["PGPASSWORD"] = password
    return sh(cmd)