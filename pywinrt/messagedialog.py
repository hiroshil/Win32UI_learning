import asyncio
import tkinter as tk
from winrt.windows.ui.popups import MessageDialog
from winrt._winrt import initialize_with_window
# based on https://github.com/ynkdir/py-win32more/blob/6650acc3c8010eba3a3c40e07ed62842fb113f74/example/winrt_messagedialog.py


async def winrt_dialog(hwnd):
    dialog = MessageDialog("This is WinRT MessageDialog", "WinRT MessageDialog")

    initialize_with_window(dialog, hwnd)

    uicommand = await dialog.show_async()

    print(uicommand, uicommand.label)


async def main() -> None:
    is_running = True

    def on_delete():
        nonlocal is_running
        is_running = False

    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_delete)
    root.eval("tk::PlaceWindow . center")

    hwnd = root.winfo_id()

    button = tk.Button(root, text="Popup WinRT dialog", command=lambda: asyncio.create_task(winrt_dialog(hwnd)))
    button.pack(padx=10, pady=10, fill="both", expand=True)

    while is_running:
        root.after(100, root.quit)
        root.mainloop()
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
