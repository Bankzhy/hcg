def static(self, root, path, media_type=None, charset='UTF-8'):
        root = os.path.abspath(os.path.join(root, ''))
        path = os.path.abspath(os.path.join(root, path.lstrip('/\\')))
        self.response.state['filename'] = os.path.basename(path)
        if not path.startswith(root):
            return 403
        elif not os.path.isfile(path):
            return 404
        if media_type is not None:
            self.response.media_type = media_type
        else:
            self.response.media_type = mimetypes.guess_type(path)[0]
        self.response.charset = charset
        with open(path, 'rb') as f:
            return f.read()