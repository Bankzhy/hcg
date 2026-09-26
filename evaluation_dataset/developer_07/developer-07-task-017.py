def fetch_json(self, uri_path, http_method='GET', query_params=None,
                   body=None, headers=None):
        query_params = query_params or {}
        headers = headers or {}
        query_params = self.add_authorisation(query_params)
        uri = self.build_uri(uri_path, query_params)
        allowed_methods = ("POST", "PUT", "DELETE")
        if http_method in allowed_methods and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        response, content = self.client.request(
            uri=uri,
            method=http_method,
            body=body,
            headers=headers
        )
        self.check_errors(uri, response)
        return json.loads(content.decode('utf-8'))