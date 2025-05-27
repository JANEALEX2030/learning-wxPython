import wx  # Import the wxPython library for GUI development

app = wx.App()  # Create the application object, initializing wxPython

# Create a new window (frame) with no parent and set its title to 'Hello World'
frame = wx.Frame(parent=None, title='Hello World')

frame.Show()  # Make the window visible

app.MainLoop()  # Start the event loop to respond to user interactions