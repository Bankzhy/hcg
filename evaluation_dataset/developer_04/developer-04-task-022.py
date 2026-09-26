def _put_information(self):
        self.session._add_object()
        self.session._out('<<')
        self.session._out('/Producer ' + self._text_to_string(
            'PDFLite, https://github.com/katerina7479'))
        if self.title:
            self.session._out('/Title ' + self._text_to_string(self.title))
        if self.subject:
            self.session._out('/Subject ' + self._text_to_string(self.subject))
        if self.author:
            self.session._out('/Author ' + self._text_to_string(self.author))
        if self.keywords:
            self.session._out('/Keywords ' +
                              self._text_to_string(self.keywords))
        if self.creator:
            self.session._out('/Creator ' + self._text_to_string(self.creator))
        self.session._out('/CreationDate ' + self._text_to_string(
            'D:' + datetime.now().strftime('%Y%m%d%H%M%S')))
        self.session._out('>>')
        self.session._out('endobj')