import PySimpleGUI as sg

# Data kendaraan (contoh)
kendaraan = []

# Layout jendela
layout = [
    [sg.Text('Nomor Polisi'), sg.Input(key='-NOPOL-')],
    [sg.Text('Waktu Masuk'), sg.Input(key='-WAKTU_MASUK-')],
    [sg.Button('Masuk'), sg.Button('Keluar')],
    [sg.Text('Daftar Kendaraan yang Masuk')],
    [sg.Table(headings=['No. Polisi', 'Waktu Masuk', 'Waktu Keluar', 'Biaya'],
              values=[],
              key='-TABLE-',
              auto_size_columns=True,
              num_rows=10)],
    [sg.Button('Urutkan Berdasarkan Waktu'), sg.Button('Urutkan Berdasarkan Biaya')],
    [sg.Button('Keluar')]
]

window = sg.Window('Program Parkir', layout)

# Fungsi untuk menambahkan kendaraan
def tambah_kendaraan(no_polisi, waktu_masuk):
    kendaraan.append({'no_polisi': no_polisi, 'waktu_masuk': waktu_masuk, 'waktu_keluar': None, 'biaya': 0})
    update_table()

# Fungsi untuk menghitung biaya dan mengupdate data kendaraan
def hitung_biaya(index):
    kendaraan[index]['waktu_keluar'] = waktu_sekarang()
    lama_parkir = kendaraan[index]['waktu_keluar'] - kendaraan[index]['waktu_masuk']
    biaya_per_jam = 2000  # Sesuaikan dengan tarif parkir
    kendaraan[index]['biaya'] = lama_parkir * biaya_per_jam
    update_table()

# Fungsi untuk mengupdate tabel
def update_table():
    data = [[kendaraan[i]['no_polisi'], kendaraan[i]['waktu_masuk'], kendaraan[i]['waktu_keluar'], kendaraan[i]['biaya']] for i in range(len(kendaraan))]
    window['-TABLE-'].update(values=data)

# Loop utama
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    elif event == 'Masuk':
        tambah_kendaraan(values['-NOPOL-'], waktu_sekarang())
    elif event == 'Keluar':
        # Implementasi untuk memilih kendaraan yang akan keluar dan menghitung biaya
        pass
    elif event == 'Urutkan Berdasarkan Waktu':
        # Mengurutkan data berdasarkan waktu masuk
        pass
    elif event == 'Urutkan Berdasarkan Biaya':
        # Mengurutkan data berdasarkan biaya
        pass

window.close()
