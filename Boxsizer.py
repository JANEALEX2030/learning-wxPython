import wx


# Define a class for the main application window, inheriting from wx.Frame
class MyFrame(wx.Frame):
    def __init__(self):
        # Initialize the frame with no parent and set the title
        super().__init__(parent=None, title='Hello World')

        # Create a panel inside the frame to contain other widgets
        panel = wx.Panel(self)

        # Set up a box sizer for vertical layout (arranges widgets vertically)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a text input control (editable text box)
        self.text_ctrl = wx.TextCtrl(panel)
        # Add the text control to the sizer with some border padding
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # Create a button labeled "Press Me"
        my_btn = wx.Button(panel, label='Press Me')
        # Add the button to the sizer, centered horizontally, with padding
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        # Set the sizer for the panel which manages the layout of child widgets
        panel.SetSizer(my_sizer)

        # Show the main window
        self.Show()


# Standard wxPython application startup
if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    # Instantiate the main frame (window)
    frame = MyFrame()
    # Start the application's event loop
    app.MainLoop()