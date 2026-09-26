def enable_wx(self, app=None):
        import wx
        wx_version = V(wx.__version__).version
        if wx_version < [2, 8]:
            raise ValueError("requires wxPython >= 2.8, but you have %s" % wx.__version__)
        from IPython.lib.inputhookwx import inputhook_wx
        self.set_inputhook(inputhook_wx)
        self._current_gui = GUI_WX
        import wx
        if app is None:
            app = wx.GetApp()
        if app is None:
            app = wx.App(redirect=False, clearSigInt=False)
        app._in_event_loop = True
        self._apps[GUI_WX] = app
        return app