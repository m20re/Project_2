import PySimpleGUI as sg
from user import *

def update_screen() -> None:
    window['-NAMETEXT-'].update(f'Name: {full_name}')
    window['-GENDERTEXT-'].update(f'Gender: {gender}')
    window['-EMAILTEXT-'].update(f'Email: {email}')
    display_image(img_url)

def display_image(url):
    window["-IMAGE-"].update(data=get_image_bytes(url))


layout = [
    [sg.Text('Random User Generator', enable_events=True, font=("Arial", 24), key = '-HEADERTEXT-')],
    [sg.Text('Name: ', font=("Arial", 12), key='-NAMETEXT-'), sg.Push(), sg.Image(key='-IMAGE-')],
    [sg.Text('Gender: ', font=("Arial", 12), key='-GENDERTEXT-')],
    [sg.Text('Email: ', font=("Arial", 12), key='-EMAILTEXT-')],
    [sg.Push(), sg.Button('Generate User', font=("Arial", 12), key='-BUTTON-')]
]
window = sg.Window('Converter', layout)

#
while True:
    # events are things that are triggerd by other elements
    # think buttons, etc.
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        full_name, gender, email, img_url = generate_user_info()
        update_screen()

window.close()
