import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube
import os
import pyperclip


class YoutubeAudioDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Киберпанк Аудио Скачиватель")

        # Стили
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Orbitron", 18), background="#1E1E1E", foreground="#00FF00")
        self.style.configure("TEntry", font=("Orbitron", 18), background="#1E1E1E", foreground="#00FF00",
                             insertcolor="#00FF00", relief="flat")
        self.style.configure("TButton", font=("Orbitron", 18), background="#00FF00", foreground="#1E1E1E",
                             relief="flat")
        self.style.configure("TCombobox", font=("Orbitron", 18), background="#1E1E1E", foreground="#00FF00")

        # Монотонный фон
        self.master.configure(background="#1E1E1E")

        # Создаем виджеты
        self.label = ttk.Label(master, text="Введите ссылку на видео YouTube:")
        self.label.pack(pady=20)

        self.url_entry = ttk.Entry(master, width=50)
        self.url_entry.pack(pady=10)

        # Связываем правую кнопку мыши с методом paste_from_clipboard
        self.url_entry.bind("<Button-3>", self.paste_from_clipboard)

        self.format_label = ttk.Label(master, text="Выберите формат аудио:")
        self.format_label.pack(pady=10)

        self.format_combobox = ttk.Combobox(master, values=["mp3", "wav", "ogg"], state="readonly")
        self.format_combobox.current(0)  # Выбираем mp3 по умолчанию
        self.format_combobox.pack(pady=10)

        self.directory_label = ttk.Label(master, text="Выберите директорию для сохранения:")
        self.directory_label.pack(pady=10)

        self.directory_entry = ttk.Entry(master, width=50)
        self.directory_entry.pack(pady=10)

        self.browse_button = ttk.Button(master, text="Обзор", command=self.select_directory)
        self.browse_button.pack(pady=10)

        self.download_button = ttk.Button(master, text="Скачать Аудио", command=self.download_audio)
        self.download_button.pack(pady=20)

        self.status_label = ttk.Label(master, text="")
        self.status_label.pack(pady=10)

    def paste_from_clipboard(self, event):
        clipboard_content = pyperclip.paste()
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, clipboard_content)

    def select_directory(self):
        self.download_directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, self.download_directory)

    def download_audio(self):
        url = self.url_entry.get()
        download_directory = self.directory_entry.get()
        audio_format = self.format_combobox.get()
        try:
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()

            # Сохранение аудио в формате mp3
            out_file = audio.download(output_path=download_directory, filename_prefix=f"audio")

            # Переименование файла с правильным расширением
            new_file_path = os.path.join(download_directory, f"audio.{audio_format}")
            os.rename(out_file, new_file_path)

            self.status_label.config(text=f"Аудио сохранено как: {new_file_path}")
        except Exception as e:
            self.status_label.config(text=f"Ошибка: {str(e)}")


root = tk.Tk()
root.geometry("600x550")
app = YoutubeAudioDownloader(root)
root.mainloop()
