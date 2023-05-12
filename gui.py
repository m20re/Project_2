import PySimpleGUI as sg
from user import *

def update_screen() -> None:
    window['-NAMETEXT-'].update(f'Name: {full_name}')
    window['-GENDERTEXT-'].update(f'Gender: {gender}')
    window['-EMAILTEXT-'].update(f'Email: {email}')
    window['-PHONETEXT-'].update(f'Phone: {phone}')
    window['-USERNAMETEXT-'].update(f'Username: {username}')
    window['-PASSWORDTEXT-'].update(f'Password: {password}')
    display_image(img_url)

def display_image(url) -> None:
    window["-IMAGE-"].update(data=get_image_bytes(url))

layout = [
    [sg.Text('Random User Generator', font=("Arial", 24), key = '-HEADERTEXT-')],
    [sg.Image(key='-IMAGE-')],
    [sg.Text('Name: ', font=("Arial", 12), key='-NAMETEXT-'), sg.Push()],
    [sg.Text('Gender: ', font=("Arial", 12), key='-GENDERTEXT-')],
    [sg.Text('Email: ', font=("Arial", 12), key='-EMAILTEXT-')],
    [sg.Text('Phone Number: ', font=("Arial", 12), key = '-PHONETEXT-')],
    [sg.Text('Username: ', font=("Arial", 12), key = '-USERNAMETEXT-')],
    [sg.Text('Password: ', font=("Arial", 12), key = '-PASSWORDTEXT-')],
    [sg.Push(), sg.Button('Generate User', font=("Arial", 12), key='-BUTTON-')]
    ]
window = sg.Window('Converter', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        full_name, gender, email, phone, username, password, img_url = generate_user_info()
        update_screen()
    

window.close()
