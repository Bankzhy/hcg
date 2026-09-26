def subwave(wave, dep_name=None, indep_min=None, indep_max=None, indep_step=None):
    ret = copy.copy(wave)
    if dep_name is not None:
        ret.dep_name = dep_name
    _bound_waveform(ret, indep_min, indep_max)
    pexdoc.addai("indep_step", bool((indep_step is not None) and (indep_step <= 0)))
    exmsg = "Argument `indep_step` is greater than independent vector range"
    cond = bool(
        (indep_step is not None)
        and (indep_step > ret._indep_vector[-1] - ret._indep_vector[0])
    )
    pexdoc.addex(RuntimeError, exmsg, cond)
    if indep_step:
        indep_vector = _barange(indep_min, indep_max, indep_step)
        dep_vector = _interp_dep_vector(ret, indep_vector)
        ret._set_indep_vector(indep_vector, check=False)
        ret._set_dep_vector(dep_vector, check=False)
    return ret