import wx

class MyFrame(wx.Frame):
    def _init_(self):
        super()._init_(parent=None, title='FlexGridSizer Example')
        panel = wx.Panel(self)

        # Create a FlexGridSizer with 9 rows and 2 columns
        flex_sizer = wx.FlexGridSizer(rows=9, cols=2, hgap=10, vgap=10)

        # Add widgets row by row
        flex_sizer.Add(wx.StaticText(panel, label='Name:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.TextCtrl(panel), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Age:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.TextCtrl(panel), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Email:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.TextCtrl(panel), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Gender:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        gender_choices = ['Male', 'Female', 'Other']
        flex_sizer.Add(wx.Choice(panel, choices=gender_choices), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Subscribe:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.CheckBox(panel), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Country:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        country_choices = ['USA', 'Canada', 'UK', 'Australia', 'Other']
        flex_sizer.Add(wx.ComboBox(panel, choices=country_choices), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Birth Date:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.TextCtrl(panel, value='YYYY-MM-DD'), 1, wx.EXPAND)

        flex_sizer.Add(wx.StaticText(panel, label='Favorite Color:'), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_sizer.Add(wx.ColourPickerCtrl(panel), 1, wx.EXPAND)

        # Create a horizontal sizer for buttons
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        submit_btn = wx.Button(panel, label='Submit')
        reset_btn = wx.Button(panel, label='Reset')
        btn_sizer.Add(submit_btn, 1, wx.RIGHT, 5)
        btn_sizer.Add(reset_btn, 1, wx.LEFT, 5)

        # Spacer + button sizer
        flex_sizer.Add((0, 0))  # Spacer for left column
        flex_sizer.Add(btn_sizer, 1, wx.EXPAND)

        # Make the second column growable
        flex_sizer.AddGrowableCol(1, 1)

        panel.SetSizer(flex_sizer)
        self.SetSize((400, 400))
        self.Centre()
        self.Show()

if __name__ == '_main_':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()