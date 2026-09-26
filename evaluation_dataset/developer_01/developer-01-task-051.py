def calc_correlation(self, x_analyte, y_analyte, window=15, filt=True, recalc=True):
        label = '{:}_{:}_{:.0f}'.format(x_analyte, y_analyte, window)
        if label in self.correlations and not recalc:
            return
        if window % 2 != 1:
            window += 1
        ind = self.filt.grab_filt(filt, [x_analyte, y_analyte])
        x = nominal_values(self.focus[x_analyte])
        x[~ind] = np.nan
        xr = rolling_window(x, window, pad=np.nan)
        y = nominal_values(self.focus[y_analyte])
        y[~ind] = np.nan
        yr = rolling_window(y, window, pad=np.nan)
        r, p = zip(*map(nan_pearsonr, xr, yr))
        r = np.array(r)
        p = np.array(p)
        self.correlations[label] = r, p
        return