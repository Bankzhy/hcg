def despike(self, expdecay_despiker=False, exponent=None,
                noise_despiker=True, win=3, nlim=12., exponentplot=False,
                maxiter=4, autorange_kwargs={}, focus_stage='rawdata'):
        if focus_stage != self.focus_stage:
            self.set_focus(focus_stage)
        if expdecay_despiker and exponent is None:
            if not hasattr(self, 'expdecay_coef'):
                self.find_expcoef(plot=exponentplot,
                                  autorange_kwargs=autorange_kwargs)
            exponent = self.expdecay_coef
            time.sleep(0.1)
        with self.pbar.set(total=len(self.data), desc='Despiking') as prog:
            for d in self.data.values():
                d.despike(expdecay_despiker, exponent,
                        noise_despiker, win, nlim, maxiter)
                prog.update()
        self.stages_complete.update(['despiked'])
        self.focus_stage = 'despiked'
        return