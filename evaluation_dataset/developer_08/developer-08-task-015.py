def recurse(self, k, wait=False, wait_index=None, timeout='5m'):
        k = k.lstrip('/')
        url = '{}/{}'.format(self.endpoint, k)
        params = {}
        params['recurse'] = 'true'
        if wait:
            params['wait'] = timeout
            if not wait_index:
                params['index'] = self.index(k, recursive=True)
            else:
                params['index'] = wait_index
        r = requests.get(url, params=params)
        if r.status_code == 404:
            raise KeyDoesNotExist("Key " + k + " does not exist")
        if r.status_code != 200:
            raise KVStoreError('GET returned {}'.format(r.status_code))
        entries = {}
        for e in r.json():
            if e['Value']:
                entries[e['Key']] = base64.b64decode(e['Value'])
            else:
                entries[e['Key']] = ''
        return entries