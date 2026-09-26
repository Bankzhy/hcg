def noise_despike(sig, win=3, nlim=24., maxiter=4):
    if win % 2 != 1:
        win += 1
    kernel = np.ones(win) / win
    over = np.ones(len(sig), dtype=bool)
    npad = int((win - 1) / 2)
    over[:npad] = False
    over[-npad:] = False
    nloops = 0
    while any(over) and (nloops < maxiter):
        rmean = np.convolve(sig, kernel, 'valid')
        rstd = rmean**0.5
        over[npad:-npad] = (sig[npad:-npad] > rmean + nlim * rstd)
        if any(over):
            sig[npad:-npad][over[npad:-npad]] = rmean[over[npad:-npad]]
            nloops += 1
    return sig