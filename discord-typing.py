from pyautogui import press, typewrite, hotkey
import pywin32, re, time, keyboard, sys, argparse

parser = argparse.ArgumentParser(description='Type in discord forever, then send a meaningless message.')
parser.add_argument("-t", "--time", help="How long you want to send a typing notification.", default=int(0))
parser.add_argument("-m", "--message", help="The rudimentary message you want to send at the end of your long, drawn out typing notification.", default="Hello guys!")
args = parser.parse_args()  

def setWindowFocus():
    w = WindowMgr()
    w.find_window_wildcard(".*Discord.*")
    w.set_foreground()

def funnyTypingNotificationPrank():
    timeout = int(args.time) # Time in Seconds

    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        typewrite('a')
        if keyboard.is_pressed('esc'):
            break
    hotkey('ctrl','a')
    typewrite(args.message)

## credit for the WindowMgr class goes to luc @ Stackoverflow, because I am lazy and didn't want to spend more than 5 minutes on this joke
#  https://stackoverflow.com/questions/2090464/python-window-activation

class WindowMgr: 
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = pywin32.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(pywin32.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        pywin32.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        pywin32.SetForegroundWindow(self._handle)

def __main__():
    setWindowFocus()
    funnyTypingNotificationPrank()

if __name__ == "__main__":
    __main__()