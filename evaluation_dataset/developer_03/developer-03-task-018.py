def distros_for_location(location, basename, metadata=None):
    if basename.endswith('.egg.zip'):
        basename = basename[:-4]
    if basename.endswith('.egg') and '-' in basename:
        return [Distribution.from_location(location, basename, metadata)]
    if basename.endswith('.exe'):
        win_base, py_ver, platform = parse_bdist_wininst(basename)
        if win_base is not None:
            return interpret_distro_name(
                location, win_base, metadata, py_ver, BINARY_DIST, platform
            )
    for ext in EXTENSIONS:
        if basename.endswith(ext):
            basename = basename[:-len(ext)]
            return interpret_distro_name(location, basename, metadata)
    return []