def gradient_plots(self, analytes=None, win=15, samples=None, ranges=False,
                       focus=None, outdir=None,
                       figsize=[10, 4], subset='All_Analyses'):
        if focus is None:
            focus = self.focus_stage
        if outdir is None:
            outdir = self.report_dir + '/' + focus + '_gradient'
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
                f, a = self.data[s].gplot(analytes=analytes, win=win, figsize=figsize,
                                        ranges=ranges, focus_stage=focus)
                f.savefig(outdir + '/' + s + '_gradients.pdf')
                plt.close(f)
                prog.update()
        return