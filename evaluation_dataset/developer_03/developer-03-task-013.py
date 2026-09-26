def upload_from_url(cls, url, store=None, filename=None):
        if store is None:
            store = 'auto'
        elif store:
            store = '1'
        else:
            store = '0'
        data = {
            'source_url': url,
            'store': store,
        }
        if filename:
            data['filename'] = filename
        result = uploading_request('POST', 'from_url/',
                                   data=data)
        if 'token' not in result:
            raise APIError(
                'could not find token in result: {0}'.format(result)
            )
        file_from_url = cls.FileFromUrl(result['token'])
        return file_from_url