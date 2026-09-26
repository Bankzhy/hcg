def paginate_get(self, url,
                 headers=None,
                 return_json=True,
                 start_page=None):
    geturl = '%s&page=1' %(url)
    if start_page is not None:
        geturl = '%s&page=%s' %(url,start_page)
    results = []
    while geturl is not None:
        result = self._get(url, headers=headers, return_json=return_json)
        if isinstance(result, dict):
            if 'results' in result:
                results = results + result['results']
            geturl = result['next']
        else:
            return result
    return results