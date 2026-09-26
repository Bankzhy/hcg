def __tile_background(self, dc):
        sz = self.wx_obj.GetClientSize()
        bmp = self._bitmap.get_bits()
        w = bmp.GetWidth()
        h = bmp.GetHeight()
        if isinstance(self, wx.ScrolledWindow):
            spx, spy = self.wx_obj.GetScrollPixelsPerUnit()
            vsx, vsy = self.wx_obj.GetViewStart()
            dx,  dy  = (spx * vsx) % w, (spy * vsy) % h
        else:
            dx, dy = (w, h)
        x = -dx
        while x < sz.width:
            y = -dy
            while y < sz.height:
                dc.DrawBitmap(bmp, x, y)
                y = y + h
            x = x + w