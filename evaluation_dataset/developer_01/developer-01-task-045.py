def send_execute_request(self, socket, code, silent=True, subheader=None, ident=None):
        if self._closed:
            raise RuntimeError("Client cannot be used after its sockets have been closed")
        subheader = subheader if subheader is not None else {}
        if not isinstance(code, basestring):
            raise TypeError("code must be text, not %s" % type(code))
        if not isinstance(subheader, dict):
            raise TypeError("subheader must be dict, not %s" % type(subheader))
        content = dict(code=code, silent=bool(silent), user_variables=[], user_expressions={})
        msg = self.session.send(socket, "execute_request", content=content, ident=ident,
                            subheader=subheader)
        msg_id = msg['header']['msg_id']
        self.outstanding.add(msg_id)
        if ident:
            if isinstance(ident, list):
                ident = ident[-1]
            if ident in self._engines.values():
                self._outstanding_dict[ident].add(msg_id)
        self.history.append(msg_id)
        self.metadata[msg_id]['submitted'] = datetime.now()
        return msg