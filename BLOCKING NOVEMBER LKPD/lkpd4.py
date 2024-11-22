import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Membuat jendela utama
window = tk.Tk()
window.configure(bg="white")  # Mengatur warna latar belakang jendela
window.geometry("300x200")  # Mengatur ukuran jendela
window.resizable(False, False)  # Mencegah jendela diubah ukurannya
window.title("Sapa")  # Mengatur judul jendela

# Membuat variabel untuk menyimpan nama
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi untuk menampilkan pesan sapaan
def tombol_click():
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have a nice day!"
    showinfo(title="Halo!", message=pesan)

# Membuat frame untuk input
input_frame = ttk.Frame(window)
input_frame.pack(padx=18, pady=10, fill="x", expand=True)

# Membuat label dan entry untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# Membuat label dan entry untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# Membuat tombol untuk menampilkan pesan
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()