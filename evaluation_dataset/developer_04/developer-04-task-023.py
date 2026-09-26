def get_arguments(self):
        ApiCli.get_arguments(self)
        if self.args.host_group_name is not None:
            self.host_group_name = self.args.host_group_name
        if self.args.sources is not None:
            self.sources = self.args.sources
        payload = {}
        if self.host_group_name is not None:
            payload['name'] = self.host_group_name
        if self.sources is not None:
            source_list = str.split(self.sources, ',')
            if 'hostnames' not in payload:
                payload['hostnames'] = []
            for s in source_list:
                payload['hostnames'].append(s)
        self.data = json.dumps(payload, sort_keys=True)
        self.headers = {'Content-Type': 'application/json', "Accept": "application/json"}