def queue_status(self, targets='all', verbose=False):
        if targets == 'all':
            engine_ids = None
        else:
            engine_ids = self._build_targets(targets)[1]
        content = dict(targets=engine_ids, verbose=verbose)
        self.session.send(self._query_socket, "queue_request", content=content)
        idents,msg = self.session.recv(self._query_socket, 0)
        if self.debug:
            pprint(msg)
        content = msg['content']
        status = content.pop('status')
        if status != 'ok':
            raise self._unwrap_exception(content)
        content = rekey(content)
        if isinstance(targets, int):
            return content[targets]
        else:
            return content