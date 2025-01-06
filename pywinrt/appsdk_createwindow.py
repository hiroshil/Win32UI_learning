from winrt.microsoft.windows.applicationmodel.dynamicdependency.bootstrap import initialize as MddBootstrapInitialize2
from winrt.microsoft.ui.windowing import AppWindow
from comtypes import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize # pip install comtypes
from comtypes.messageloop import _messageloop
from ctypes import windll, c_int
# for build - manually add modules called from module for exe builder parser
import uuid
import winrt.windows.foundation

PostQuitMessage = windll.user32.PostQuitMessage
PostQuitMessage.argtypes = [c_int]
PostQuitMessage.restype = None

def on_destroying(appwin, obj):
    PostQuitMessage(0)

def main() -> None:
    CoInitializeEx(COINIT_APARTMENTTHREADED)

    hr = MddBootstrapInitialize2()

    appwin = AppWindow.create()
    appwin.title = "Hello World"
    appwin.add_destroying(on_destroying)
    appwin.show()

    # https://github.com/enthought/comtypes/blob/main/CHANGES.txt#L996
    _messageloop.run()

    hr() # call Shutdown()

    CoUninitialize()


if __name__ == "__main__":
    main()
