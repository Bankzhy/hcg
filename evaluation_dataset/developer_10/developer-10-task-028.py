def _call_tip(self):
        if not self.enable_calltips:
            return False
        cursor = self._get_cursor()
        cursor.movePosition(QtGui.QTextCursor.Left)
        if cursor.document().characterAt(cursor.position()) != '(':
            return False
        context = self._get_context(cursor)
        if not context:
            return False
        name = '.'.join(context)
        msg_id = self.kernel_manager.shell_channel.object_info(name)
        pos = self._get_cursor().position()
        self._request_info['call_tip'] = self._CallTipRequest(msg_id, pos)
        return True