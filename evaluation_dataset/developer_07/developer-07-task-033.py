def configure(self, options, conf):
        super(NoseExclude, self).configure(options, conf)
        self.exclude_dirs = {}
        if options.exclude_dir_file:
            if not options.exclude_dirs:
                options.exclude_dirs = []
            new_dirs = self._load_from_file(options.exclude_dir_file)
            options.exclude_dirs.extend(new_dirs)
        if not options.exclude_dirs:
            self.enabled = False
            return
        self.enabled = True
        root = os.getcwd()
        log.debug('cwd: %s' % root)
        for exclude_param in options.exclude_dirs:
            for d in exclude_param.split('\n'):
                d = d.strip()
                abs_d = self._force_to_abspath(d)
                if abs_d:
                    self.exclude_dirs[abs_d] = True
        exclude_str = "excluding dirs: %s" % ",".join(self.exclude_dirs.keys())
        log.debug(exclude_str)