def get_account(self, headers=None, prefix=None, delimiter=None,
                    marker=None, end_marker=None, limit=None, query=None,
                    cdn=False, decode_json=True):
        query = dict(query or {})
        query['format'] = 'json'
        if prefix:
            query['prefix'] = prefix
        if delimiter:
            query['delimiter'] = delimiter
        if marker:
            query['marker'] = marker
        if end_marker:
            query['end_marker'] = end_marker
        if limit:
            query['limit'] = limit
        return self.request(
            'GET', '', '', headers, decode_json=decode_json, query=query,
            cdn=cdn)