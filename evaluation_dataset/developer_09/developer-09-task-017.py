def configure(self):
        handler = logging.FileHandler(self.path, delay=True)
        if self._format:
            handler.setFormatter(logging.Formatter(self._format))
        if type(self._formatter) == str:
            if self._env and self._env.config.logging.dict_config.formatters[self._formatter]:
                d = self._env.config.logging.dict_config.formatters[self._formatter].to_dict()
                handler.setFormatter(logging.Formatter(**d))
        elif type(self._formatter) == dict:
            handler.setFormatter(logging.Formatter(**self._formatter))
        if len(self._loggers):
            for name in self._loggers:
                logging.getLogger(name).addHandler(handler)
        else:
            logging.getLogger().addHandler(handler)