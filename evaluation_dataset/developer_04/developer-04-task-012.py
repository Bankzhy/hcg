def set(self, token, request, *args, **kwargs):
        if hasattr(request, 'user') and request.user:
            user = request.user
        elif self.current_user:
            user = self.current_user()
        client = request.client
        tokens = self.query.filter_by(
            client_id=client.client_id,
            user_id=user.id).all()
        if tokens:
            for tk in tokens:
                self.session.delete(tk)
            self.session.commit()
        expires_in = token.get('expires_in')
        expires = datetime.utcnow() + timedelta(seconds=expires_in)
        tok = self.model(**token)
        tok.expires = expires
        tok.client_id = client.client_id
        tok.user_id = user.id
        self.session.add(tok)
        self.session.commit()
        return tok