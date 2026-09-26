def filter_unused_import(line, unused_module, remove_all_unused_imports,
                         imports, previous_line=''):
    if multiline_import(line, previous_line):
        return line
    is_from_import = line.lstrip().startswith('from')
    if ',' in line and not is_from_import:
        return break_up_import(line)
    package = extract_package_name(line)
    if not remove_all_unused_imports and package not in imports:
        return line
    if ',' in line:
        assert is_from_import
        return filter_from_import(line, unused_module)
    else:
        return (get_indentation(line) +
                'pass' +
                get_line_ending(line))