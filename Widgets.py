import wx


class MyFrame(wx.Frame):
    def __init__(self):
        # Initialize the main window (frame) with no parent and a title
        super().__init__(parent=None, title='Hello World')

        # Create a panel inside the frame to hold widgets
        panel = wx.Panel(self)

        # Add a text control (editable text box) at position (5, 5)
        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))

        # Add a button labeled 'Press Me' at position (5, 50)
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 50))

        # Add a static text label at position (5, 100)
        label = wx.StaticText(panel, label="Hello Akim", pos=(5, 100))

        # Create a combo box (drop-down list) with choices at position (5, 150)
        choices = ["Akim", "Jane", "Adam"]
        combo_box = wx.ComboBox(panel, choices=choices, pos=(5, 150))

        # Add a slider with range 0-100 at position (5, 200)
        slider = wx.Slider(panel, minValue=0, maxValue=100, pos=(5, 200))

        # Add a list box with three fruit items at position (5, 250)
        list_box = wx.ListBox(panel, choices=["Banana", "Apple", "Mango"], pos=(5, 250))

        # Create a gauge (progress bar) with range 0-100, size (250, 20), at position (5, 310)
        gauge = wx.Gauge(panel, range=100, size=(250, 20), pos=(5, 310))
        # Set the current value of the gauge to 50
        gauge.SetValue(50)

        # Show the main window
        self.Show()


if __name__ == "__main__":
    # Initialize wxPython app
    app = wx.App()
    # Create an instance of the MyFrame class
    frame = MyFrame()
    # Start the event loop
    app.MainLoop()