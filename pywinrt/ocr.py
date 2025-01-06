import asyncio
import tkinter as tk

from winrt.windows.graphics.imaging import BitmapDecoder
from winrt.windows.media.ocr import OcrEngine
from winrt.windows.storage import FileAccessMode
from winrt.windows.storage.pickers import FileOpenPicker
from winrt.windows.ui.popups import MessageDialog
from winrt._winrt import initialize_with_window
# for build - manually add modules called from module for exe builder parser
import winrt.windows.foundation
import winrt.windows.foundation.collections
import winrt.windows.globalization
import winrt.windows.storage.streams

mainhwnd = None


async def show_message(title, msg):
    dialog = MessageDialog(msg, title)
    initialize_with_window(dialog, mainhwnd)
    return await dialog.show_async()


async def open_file(filter):
    picker = FileOpenPicker()
    initialize_with_window(picker, mainhwnd)
    picker.file_type_filter.append(filter)
    return await picker.pick_single_file_async()


async def read_image(storage_file):
    bitmap = await BitmapDecoder.create_async(
        BitmapDecoder.png_decoder_id, await storage_file.open_async(FileAccessMode.READ)
    )
    return await bitmap.get_software_bitmap_async()


def list_ocr_languages():
    print("AvailableRecognizerLanguages:")
    vec = OcrEngine.available_recognizer_languages
    for i in range(vec.size):
        lang = vec.get_at(i)
        print(f"{lang.language_tag}: {lang.display_name}")


async def ocr(software_image):
    engine = OcrEngine.try_create_from_user_profile_languages()
    result = await engine.recognize_async(software_image)
    return result.text


async def run_ocr():
    storage_file = await open_file(".png")
    if not storage_file:
        return
    software_bitmap = await read_image(storage_file)
    text = await ocr(software_bitmap)
    await show_message("Ocr result", text)


async def main():
    global mainhwnd

    is_running = True

    def on_delete():
        nonlocal is_running
        is_running = False

    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_delete)
    root.eval("tk::PlaceWindow . center")

    mainhwnd = root.winfo_id()

    list_ocr_languages()

    button = tk.Button(root, text="Open image for OCR", command=lambda: asyncio.create_task(run_ocr()))
    button.pack(padx=10, pady=10, fill="both", expand=True)

    while is_running:
        root.after(100, root.quit)
        root.mainloop()
        await asyncio.sleep(0)


asyncio.run(main())
