def plot1d(self, grid=None, size=64, limits=None, weight=None, figsize=None, f="identity", axes=None, xlabel=None, ylabel=None, **kwargs):
        import pylab
        f = _parse_f(f)
        limits = self.limits(limits)
        assert self.dimension == 1, "can only plot 1d, not %s" % self.dimension
        if limits is None:
            limits = self.limits_sigma()
        if grid is None:
            grid = self.histogram(limits=limits, size=size, weight=weight)
        if figsize is not None:
            pylab.figure(num=None, figsize=figsize, dpi=80, facecolor='w', edgecolor='k')
        if axes is None:
            axes = pylab.gca()
        pylab.xlabel(xlabel or self.expressions[0])
        pylab.ylabel("counts" or ylabel)
        N = len(grid)
        xmin, xmax = limits[0]
        return pylab.plot(np.arange(N) / (N - 1.0) * (xmax - xmin) + xmin, f(grid,), drawstyle="steps", **kwargs)