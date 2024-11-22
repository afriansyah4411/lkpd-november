import PySimpleGUI as sg

# Layout jendela
layout = [
    [sg.Text('Nama Lengkap'), sg.Input(key='-NAMA-')],
    [sg.Text('Tanggal Lahir'), sg.Input(key='-TGL_LAHIR-')],
    [sg.Text('Asal Sekolah'), sg.Input(key='-ASAL_SEKOLAH-')],
    [sg.Text('NISN'), sg.Input(key='-NISN-')],
    [sg.Text('Nama Ayah'), sg.Input(key='-NAMA_AYAH-')],
    [sg.Text('Nama Ibu'), sg.Input(key='-NAMA_IBU-')],
    [sg.Text('Nomor Telepon/HP'), sg.Input(key='-NO_TELP-')],
    [sg.Text('Alamat'), sg.Input(key='-ALAMAT-')],
    [sg.Button('Simpan'), sg.Button('Keluar')]
]

# Membuat jendela
window = sg.Window('Data Siswa Baru', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    if event == 'Simpan':
        # Kode untuk menyimpan data ke dalam database atau file
        nama = values['-NAMA-']
        tgl_lahir = values['-TGL_LAHIR-']
        # ... dan seterusnya untuk data lainnya
        print(f"Data siswa baru:\nNama: {nama}\nTanggal Lahir: {tgl_lahir}")  # Contoh output ke console

window.close()