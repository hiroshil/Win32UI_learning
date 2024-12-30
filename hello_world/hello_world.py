from win32more.Microsoft.UI.Xaml import Window
from win32more.xaml import XamlApplication
# based on https://github.com/MicrosoftDocs/windows-dev-docs/blob/docs/hub/apps/how-tos/hello-world-winui3.md


class App(XamlApplication):
    def OnLaunched(self, args):
        with open("MainWindow.xaml", "r", encoding='utf-8') as file:
            self.window = self.LoadXamlAndSetEventHandler(file.read()).as_(Window)

        self.window.Activate()

XamlApplication.Start(App)
