def body(self, msgid_article=None, decode=False):
        args = None
        if msgid_article is not None:
            args = utils.unparse_msgid_article(msgid_article)
        code, message = self.command("BODY", args)
        if code != 222:
            raise NNTPReplyError(code, message)
        escape = 0
        crc32 = 0
        body = []
        for line in self.info_gen(code, message):
            if decode:
                if line.startswith("=y"):
                    continue
                line, escape, crc32 = yenc.decode(line, escape, crc32)
            body.append(line)
        return "".join(body)