import win32gui


class Window:
    def __init__(self, window_name, position, sizes):
        """
        ------------------------------------------------------------------------------------------
        Search for the necessary window and work with it

        type(window_name) >> str()
        type(position) >> tuple() | len(position) >> 2 | type(position[::]) >> int()
        type(sizes) >> tuple() | len(sizes) >> 2 | type(sizes[::]) >> int()
        ------------------------------------------------------------------------------------------
        """

        self.hwnd =  win32gui.FindWindow(None, window_name)

        self.position = position
        self.sizes = sizes

    def update_window(self):
        """
        ------------------------------------------------------------------------------------------
        Moving + Scaling + Focusing necessary window
        ------------------------------------------------------------------------------------------
        """
        
        win32gui.MoveWindow(self.hwnd, *self.position, *self.sizes, True)
        win32gui.SetForegroundWindow(self.hwnd)