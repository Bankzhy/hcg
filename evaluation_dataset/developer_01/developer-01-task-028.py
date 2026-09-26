def get_data(self, environment_title_or_num=-1, frequency=None):
        if isinstance(environment_title_or_num, int):
            environment_title = tuple(self._raw_environments.keys())[environment_title_or_num]
        else:
            environment_title = environment_title_or_num
        if environment_title not in self._dfs:
            raise ValueError(f"No environment named {environment_title}. Available environments: {tuple(self._dfs)}.")
        environment_dfs = self._dfs[environment_title]
        if frequency is None:
            for frequency in FREQUENCIES:
                if environment_dfs[frequency] is not None:
                    break
        if frequency not in FREQUENCIES:
            raise ValueError(f"Unknown frequency: {frequency}. Available frequencies: {FREQUENCIES}")
        return self._dfs[environment_title][frequency]