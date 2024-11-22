import PySimpleGUI as sg

layout = [
    [sg.Text('Nama Barang'), sg.Input(key='-BARANG-')],
    [sg.Text('Harga'), sg.Input(key='-HARGA-')],
    [sg.Text('Kuantitas'), sg.Input(key='-KUANTITAS-')],
    [sg.Button('Hitung Total'), sg.Button('Keluar')],
    [sg.Text('Total:', key='-TOTAL-')]
]

window = sg.Window('Program Kasir', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    if event == 'Hitung Total':
        try:
            harga = float(values['-HARGA-'])
            kuantitas = int(values['-KUANTITAS-'])
            total = harga * kuantitas
            window['-TOTAL-'].update(f'Rp. {total:.2f}')
        except ValueError:
            sg.popup_error('Masukkan 1  harga dan kuantitas yang valid!')

window.close()