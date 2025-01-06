from winrt.microsoft.windows.applicationmodel.dynamicdependency.bootstrap import initialize as MddBootstrapInitialize
from winrt.microsoft.windows.appnotifications import AppNotificationManager
from winrt.microsoft.windows.appnotifications.builder import AppNotificationBuilder
from comtypes import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize # pip install comtypes
# for build - manually add modules called from module for exe builder parser
import uuid
# based on https://github.com/ynkdir/py-win32more/blob/6650acc3c8010eba3a3c40e07ed62842fb113f74/example/appsdk_notification.py


def main() -> None:

    CoInitializeEx(COINIT_APARTMENTTHREADED)
    
    hr = MddBootstrapInitialize()
    
    notification_manager = AppNotificationManager.default

    notification_manager.register()

    # How to set title?
    notification = AppNotificationBuilder().add_text("title").add_text("message").build_notification()

    notification_manager.show(notification)

    # Documentation says:
    # "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    notification_manager.unregister()
    
    hr() # call Shutdown()
    
    CoUninitialize()


if __name__ == "__main__":
    main()
