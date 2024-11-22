import tkinter as tk
from tkinter import filedialog
import os

def list_files(folder_path):
    # Fungsi untuk membuat daftar file dalam folder
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Membuat jendela utama
window = tk.Tk()
window.title("File Viewer")

# ... (komponen GUI lainnya)

# Tombol untuk memilih folder
button = tk.Button(window, text="Pilih Folder", command=lambda: select_folder())
button.pack()

def select_folder():
    # Fungsi yang dipanggil ketika tombol "Pilih Folder" ditekan
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_list = list_files(folder_path)
        # ... (tampilkan daftar file dalam GUI)

window.mainloop()