def check_part_index(state, name, index, part_msg, missing_msg=None, expand_msg=None):
    if missing_msg is None:
        missing_msg = "Are you sure you defined the {{part}}? "
    if expand_msg is None:
        expand_msg = "Did you correctly specify the {{part}}? "
    ordinal = get_ord(index + 1) if isinstance(index, int) else ""
    fmt_kwargs = {"index": index, "ordinal": ordinal}
    fmt_kwargs.update(part=render(part_msg, fmt_kwargs))
    append_message = {"msg": expand_msg, "kwargs": fmt_kwargs}
    has_part(state, name, missing_msg, fmt_kwargs, index)
    stu_part = state.student_parts[name]
    sol_part = state.solution_parts[name]
    if isinstance(index, list):
        for ind in index:
            stu_part = stu_part[ind]
            sol_part = sol_part[ind]
    else:
        stu_part = stu_part[index]
        sol_part = sol_part[index]
    assert_ast(state, sol_part, fmt_kwargs)
    return part_to_child(stu_part, sol_part, append_message, state)