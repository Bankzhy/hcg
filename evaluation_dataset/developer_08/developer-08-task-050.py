def stats(self, filter, limit, start=None):
        if filter == 'random':
            filter = 'rand'
        valid_filters = ('top', 'bottom', 'rand', 'last')
        if filter not in valid_filters:
            msg = 'filter must be one of {}'.format(', '.join(valid_filters))
            raise ValueError(msg)
        data = dict(action='stats', filter=filter, limit=limit, start=start)
        jsondata = self._api_request(params=data)
        stats = DBStats(total_clicks=int(jsondata['stats']['total_clicks']),
                        total_links=int(jsondata['stats']['total_links']))
        links = []
        if 'links' in jsondata:
            for i in range(1, limit + 1):
                key = 'link_{}'.format(i)
                links.append(_json_to_shortened_url(jsondata['links'][key]))
        return links, stats