import wx

# Define a new class MyFrame which inherits from wx.Frame (a main window or frame)
class MyFrame(wx.Frame):
    def __init__(self):
        # Call the parent constructor to initialize the frame
        super().__init__(parent=None, title='Hello World')
        # Show the frame window when it's created
        self.Show()

# Entry point of the program
if __name__ == '__main__':
    # Create a wx.App instance, which manages the application's control flow
    app = wx.App()
    # Instantiate the MyFrame class, creating the main window
    frame = MyFrame()
    # Start the wxPython event loop, waiting for user interactions
    app.MainLoop()