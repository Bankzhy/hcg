def _validate_min_max(wave, indep_min, indep_max):
    imin, imax = False, False
    if indep_min is None:
        indep_min = wave._indep_vector[0]
        imin = True
    if indep_max is None:
        indep_max = wave._indep_vector[-1]
        imax = True
    if imin and imax:
        return indep_min, indep_max
    exminmax = pexdoc.exh.addex(
        RuntimeError, "Incongruent `indep_min` and `indep_max` arguments"
    )
    exmin = pexdoc.exh.addai("indep_min")
    exmax = pexdoc.exh.addai("indep_max")
    exminmax(bool(indep_min >= indep_max))
    exmin(
        bool(
            (indep_min < wave._indep_vector[0])
            and (not np.isclose(indep_min, wave._indep_vector[0], FP_RTOL, FP_ATOL))
        )
    )
    exmax(
        bool(
            (indep_max > wave._indep_vector[-1])
            and (not np.isclose(indep_max, wave._indep_vector[-1], FP_RTOL, FP_ATOL))
        )
    )
    return indep_min, indep_max