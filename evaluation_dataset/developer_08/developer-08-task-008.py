def emit(self, level, message, prefix=None, color=None):
        if color is None:
            color = level
        if prefix is not None:
            prefix = self.addColor(color, "%s " % (prefix))
        else:
            prefix = ""
            message = self.addColor(color, message)
        message = "%s%s" % (prefix, message)
        if not message.endswith('\n'):
            message = "%s\n" % message
        if self.level == QUIET:
            pass
        elif self.isEnabledFor(level):
            if self.emitError(level):
                self.write(self.errorStream, message)
            else:
                self.write(self.outputStream, message)
        self.history.append(message)