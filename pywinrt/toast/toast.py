from winrt.windows.ui.notifications import ToastNotification, ToastNotificationManager
from winrt.windows.data.xml.dom import XmlDocument

doc = XmlDocument()
doc.load_xml("""<toast>
    <visual>
      <binding template="ToastImageAndText01" description="An image and a single string wrapped across a maximum of three lines of text.">
        <image id="1" src="" name="Image" />
        <text id="1" name="Text"></text>
      </binding>
    </visual>
  </toast>""")
toast = ToastNotification(doc)
toast_notifier = ToastNotificationManager.create_toast_notifier(r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe")
toast_notifier.show(toast)