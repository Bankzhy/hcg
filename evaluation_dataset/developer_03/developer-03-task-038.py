def correlation_plots(self, x_analyte, y_analyte, window=15, filt=True, recalc=False, samples=None, subset=None, outdir=None):
        if outdir is None:
            outdir = self.report_dir + '/correlations/'
        if not os.path.isdir(outdir):
            os.mkdir(outdir)
        if subset is not None:
            samples = self._get_samples(subset)
        elif samples is None:
            samples = self.subsets['All_Analyses']
        elif isinstance(samples, str):
            samples = [samples]
        with self.pbar.set(total=len(samples), desc='Drawing Plots') as prog:
            for s in samples:
                f, a = self.data[s].correlation_plot(x_analyte=x_analyte, y_analyte=y_analyte,
                                                     window=window, filt=filt, recalc=recalc)
                f.savefig('{}/{}_{}-{}.pdf'.format(outdir, s, x_analyte, y_analyte))
                plt.close(f)
                prog.update()
        return