def chart_plot(self, ax=None, cmap='RdBu',
               xlabel='N', ylabel='Z', grid_on=True, colorbar=True):
        from matplotlib.mlab import griddata
        from numpy import linspace, meshgrid
        import matplotlib.pyplot as plt
        x = self.dropna().N
        y = self.dropna().Z
        z = self.dropna().values
        xi = linspace(min(x), max(x), max(x) - min(x) + 1)
        yi = linspace(min(y), max(y), max(y) - min(y) + 1)
        Z = griddata(x, y, z, xi, yi)
        X, Y = meshgrid(xi, yi)
        if ax is None:
            ax = plt.gca()
        chart = ax.pcolormesh(X, Y, Z, cmap=cmap)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid_on)
        ax.set_aspect('equal')
        if colorbar:
            plt.colorbar(chart)
        return ax