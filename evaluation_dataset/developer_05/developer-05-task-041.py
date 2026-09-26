def _create_msg(self, to, subject, msgHtml, msgPlain, attachments=None):
        sender = self.sender
        if attachments and isinstance(attachments, str):
            attachments = [attachments]
        else:
            attachments = list(attachments or [])
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to
        msg.attach(MIMEText(msgPlain, 'plain'))
        msg.attach(MIMEText(msgHtml, 'html'))
        for path in attachments:
            _attachment = self._prep_attachment(path)
            msg.attach(_attachment)
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        body = {'raw': raw}
        return body