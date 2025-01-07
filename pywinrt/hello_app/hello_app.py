from winrt.microsoft.ui.xaml import (
    Application,
    ApplicationInitializationCallbackParams,
    LaunchActivatedEventArgs,
    Window,
)
from winrt.microsoft.ui.xaml.markup import XamlReader
from winrt.microsoft.windows.applicationmodel.dynamicdependency.bootstrap import (
    InitializeOptions,
    initialize,
)
from winrt.system import box_string
# for build - manually add modules called from module for exe builder parser
import winrt.microsoft.ui.xaml.controls.primitives
import winrt.windows.foundation
import sys
from os.path import join as path_join
# based on https://github.com/pywinrt/pywinrt/blob/397195cbfccdeb1802a6ef6a279e905829a21b71/samples/win_app_sdk/hello_app.py

####################### REQUIREMENT: pywinrt >= 397195c ################################################


# for build with pyinstaller https://stackoverflow.com/questions/53587322/how-do-i-include-files-with-pyinstaller/53605128#53605128
def get_path(fpath):
    if getattr(sys, 'frozen', False):
        return path_join(sys._MEIPASS, fpath)
    return fpath

class App(Application):
    def _on_launched(self, args: LaunchActivatedEventArgs) -> None:

        window = Window()
        with open(get_path("hello_app.xaml"), "r", encoding='utf-8') as file:
            window.content = XamlReader.load(file.read())

        # Show it!
        window.activate()


def init(_: ApplicationInitializationCallbackParams) -> None:
    # This implicitly sets Application.current to this object so we don't need
    # to keep a reference to it.
    App()


# This is the main entry point for the application. To use the Windows App SDK
# outside of a packaged app, you have to bootstrap it using the initialize
# function. The ON_NO_MATCH_SHOW_UI option will show a dialog if the required
# version of the Windows App runtime is not installed.
with initialize(options=InitializeOptions.ON_NO_MATCH_SHOW_UI):
    Application.start(init)
