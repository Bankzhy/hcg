def tonnetz(y=None, sr=22050, chroma=None):
    if y is None and chroma is None:
        raise ParameterError('Either the audio samples or the chromagram must be '
                             'passed as an argument.')
    if chroma is None:
        chroma = chroma_cqt(y=y, sr=sr)
    dim_map = np.linspace(0, 12, num=chroma.shape[0], endpoint=False)
    scale = np.asarray([7. / 6, 7. / 6,
                        3. / 2, 3. / 2,
                        2. / 3, 2. / 3])
    V = np.multiply.outer(scale, dim_map)
    V[::2] -= 0.5
    R = np.array([1, 1,
                  1, 1,
                  0.5, 0.5])
    phi = R[:, np.newaxis] * np.cos(np.pi * V)
    return phi.dot(util.normalize(chroma, norm=1, axis=0))