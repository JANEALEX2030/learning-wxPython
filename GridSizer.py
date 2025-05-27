import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='GridSizer Example')
        panel = wx.Panel(self)

        # Create a GridSizer with 2 rows and 2 columns, with gaps of 5 pixels
        grid_sizer = wx.GridSizer(rows=2, cols=2, gap=(5, 5))

        # Add a TextCtrl to cell (0,0)
        self.text_ctrl = wx.TextCtrl(panel)
        grid_sizer.Add(self.text_ctrl, 0, wx.EXPAND)

        # Add a Button to cell (0,1)
        my_btn = wx.Button(panel, label='Press Me')
        grid_sizer.Add(my_btn, 0, wx.EXPAND)

        # Add a StaticText in cell (1,0)
        label = wx.StaticText(panel, label='Hello from GridSizer')
        grid_sizer.Add(label, 0, wx.ALIGN_CENTER)

        # Add a ListBox in cell (1,1)
        list_box = wx.ListBox(panel, choices=["A", "B", "C"])
        grid_sizer.Add(list_box, 0, wx.EXPAND)

        # Apply the sizer to the panel
        panel.SetSizer(grid_sizer)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()