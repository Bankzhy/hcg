def get_image(self, image, show_history=False):
        itype = self._discover_inputimage_format(image)
        if itype not in ['tag', 'imageid', 'imageDigest']:
            return [False, "cannot use input image string: no discovered imageDigest"]
        params = {}
        params['history'] = str(show_history and itype not in ['imageid', 'imageDigest']).lower()
        if itype == 'tag':
            params['fulltag'] = image
        url = self.url + "/api/scanning/v1/anchore/images"
        url += {
            'imageid': '/by_id/{}'.format(image),
            'imageDigest': '/{}'.format(image)
        }.get(itype, '')
        res = requests.get(url, params=params, headers=self.hdrs, verify=self.ssl_verify)
        if not self._checkResponse(res):
            return [False, self.lasterr]
        return [True, res.json()]