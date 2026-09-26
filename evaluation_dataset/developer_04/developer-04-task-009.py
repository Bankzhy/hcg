def get_conversation_paged_members(
            self, conversation_id, page_size=None, continuation_token=None, custom_headers=None, raw=False, **operation_config):
        url = self.get_conversation_paged_members.metadata['url']
        path_format_arguments = {
            'conversationId': self._serialize.url("conversation_id", conversation_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)
        query_parameters = {}
        if page_size is not None:
            query_parameters['pageSize'] = self._serialize.query("page_size", page_size, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query("continuation_token", continuation_token, 'str')
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)
        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PagedMembersResult', response)
        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response
        return deserialized