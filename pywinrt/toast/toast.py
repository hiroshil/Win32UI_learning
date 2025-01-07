from winrt.windows.ui.notifications import ToastNotification, ToastNotificationManager
from winrt.windows.data.xml.dom import XmlDocument
# for build - manually add modules called from module for exe builder parser
import sys
import uuid
from os.path import join as path_join
# based on https://github.com/ynkdir/py-win32more/blob/6650acc3c8010eba3a3c40e07ed62842fb113f74/example/winrt_notification.py


# for build with pyinstaller https://stackoverflow.com/questions/53587322/how-do-i-include-files-with-pyinstaller/53605128#53605128
def get_path(fpath):
    if getattr(sys, 'frozen', False):
        return path_join(sys._MEIPASS, fpath)
    return fpath

doc = XmlDocument()
with open(get_path("toast.xaml"), "r", encoding='utf-8') as file:
    doc.load_xml(file.read())
toast = ToastNotification(doc)
toast_notifier = ToastNotificationManager.create_toast_notifier_with_id(r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe")
toast_notifier.show(toast)