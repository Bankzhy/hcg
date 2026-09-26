def make_color_wheel(bins=None):
    if bins is None:
        bins = [15, 6, 4, 11, 13, 6]
    assert len(bins) == 6
    RY, YG, GC, CB, BM, MR = tuple(bins)
    ry = [1, np.arange(RY) / RY, 0]
    yg = [1 - np.arange(YG) / YG, 1, 0]
    gc = [0, 1, np.arange(GC) / GC]
    cb = [0, 1 - np.arange(CB) / CB, 1]
    bm = [np.arange(BM) / BM, 0, 1]
    mr = [1, 0, 1 - np.arange(MR) / MR]
    num_bins = RY + YG + GC + CB + BM + MR
    color_wheel = np.zeros((3, num_bins), dtype=np.float32)
    col = 0
    for i, color in enumerate([ry, yg, gc, cb, bm, mr]):
        for j in range(3):
            color_wheel[j, col:col + bins[i]] = color[j]
        col += bins[i]
    return color_wheel.T