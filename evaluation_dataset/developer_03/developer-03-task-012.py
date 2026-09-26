def decompress_G2(p: G2Compressed) -> G2Uncompressed:
    z1, z2 = p
    b_flag1 = (z1 % POW_2_383) // POW_2_382
    if b_flag1 == 1:
        return Z2
    x1 = z1 % POW_2_381
    x2 = z2
    x = FQ2([x2, x1])
    y = modular_squareroot_in_FQ2(x**3 + b2)
    if y is None:
        raise ValueError("Failed to find a modular squareroot")
    a_flag1 = (z1 % POW_2_382) // POW_2_381
    y_re, y_im = y.coeffs
    if (y_im > 0 and (y_im * 2) // q != a_flag1) or (y_im == 0 and (y_re * 2) // q != a_flag1):
        y = FQ2((y * -1).coeffs)
    if not is_on_curve((x, y, FQ2([1, 0])), b2):
        raise ValueError(
            "The given point is not on the twisted curve over FQ**2"
        )
    return (x, y, FQ2([1, 0]))