from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, ttk

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, ttk

def download_video():
    video_url = entry_url.get()
    resolution = resolution_var.get()
    try:
        yt = YouTube(video_url)
        save_location = filedialog.askdirectory()
        if save_location:
            stream = yt.streams.filter(res=resolution, progressive=True).first()
            if stream:
                stream.download(output_path=save_location)
                status_label.config(text="Видео успешно загружено!")
            else:
                status_label.config(text=f"Не удалось найти поток с разрешением {resolution}p")
        else:
            status_label.config(text="Вы не выбрали директорию для сохранения.")
    except Exception as e:
        status_label.config(text=f"Ошибка: {str(e)}")

def paste_url(event):
    url = root.clipboard_get()
    entry_url.delete(0, tk.END)
    entry_url.insert(0, url)

root = tk.Tk()
root.title("Загрузчик видео с YouTube")

label_url = tk.Label(root, text="Введите URL видео:")
label_url.pack()

entry_url = tk.Entry(root, width=50)
entry_url.pack()
entry_url.bind("<Button-3>", paste_url)  # Связываем вставку URL с правой кнопкой мыши

label_resolution = tk.Label(root, text="Выберите разрешение:")
label_resolution.pack()

resolution_var = tk.StringVar()
resolution_var.set("360p")  # Установка начального значения

resolution_options = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution_dropdown = ttk.Combobox(root, textvariable=resolution_var, values=resolution_options, state="readonly")
resolution_dropdown.pack()

download_button = tk.Button(root, text="Загрузить видео", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
