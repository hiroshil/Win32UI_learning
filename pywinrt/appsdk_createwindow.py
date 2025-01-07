from winrt.microsoft.windows.applicationmodel.dynamicdependency.bootstrap import initialize as MddBootstrapInitialize2
from winrt.microsoft.ui.windowing import AppWindow
from comtypes.messageloop import _messageloop # pip install comtypes
# for build - manually add modules called from module for exe builder parser
import uuid
import winrt.windows.foundation
# based on https://github.com/ynkdir/py-win32more/blob/6650acc3c8010eba3a3c40e07ed62842fb113f74/example/appsdk_createwindow.py

def on_destroying(appwin, obj):
    appwin.destroy()

def main() -> None:

    hr = MddBootstrapInitialize2()

    appwin = AppWindow.create()
    appwin.title = "Hello World"
    #appwin.add_destroying(on_destroying)
    appwin.show()

    # https://github.com/enthought/comtypes/blob/main/CHANGES.txt#L996
    _messageloop.run()

    hr() # call Shutdown()


if __name__ == "__main__":
    main()
