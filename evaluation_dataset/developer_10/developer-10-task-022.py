def get_data(self, metrics, start_ts, end_ts=0, sampling_s=0,
                 filter='', datasource_type='host', paging=None):
        reqbody = {
            'metrics': metrics,
            'dataSourceType': datasource_type,
        }
        if start_ts < 0:
            reqbody['last'] = -start_ts
        elif start_ts == 0:
            return [False, "start_ts cannot be 0"]
        else:
            reqbody['start'] = start_ts
            reqbody['end'] = end_ts
        if filter != '':
            reqbody['filter'] = filter
        if paging is not None:
            reqbody['paging'] = paging
        if sampling_s != 0:
            reqbody['sampling'] = sampling_s
        res = requests.post(self.url + '/api/data/', headers=self.hdrs, data=json.dumps(reqbody), verify=self.ssl_verify)
        return self._request_result(res)