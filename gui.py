import PySimpleGUI as sg
from user import *

def update_screen() -> None:
    """
    Updates all of the screen elements to reflect new user data
    :return: None
    """
    window['-NAMETEXT-'].update(f'Name: {full_name}')
    window['-GENDERTEXT-'].update(f'Gender: {gender}')
    window['-EMAILTEXT-'].update(f'Email: {email}')
    window['-PHONETEXT-'].update(f'Phone: {phone}')
    window['-USERNAMETEXT-'].update(f'Username: {username}')
    window['-PASSWORDTEXT-'].update(f'Password: {password}')
    display_image(img_url)

def display_image(url) -> None:
    """
    Displays the image within the gui
    :return: None
    """

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
    [sg.Button('Generate New Password', font=("Arial", 12), key='-BUTTON2-'), sg.Push(), sg.Button('Generate User', font=("Arial", 12), key='-BUTTON-')]
    ]
window = sg.Window('Converter', layout)
ISFIRST = True

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        
        full_name, gender, email, phone, username, password, img_url = generate_user_info()
        update_screen()
        if ISFIRST:
            write_header_csv('output.csv')
            ISFIRST = False

    
    if event == '-BUTTON2-':
        window['-PASSWORDTEXT-'].update(f'Password: {generate_new_password()}')
    

window.close()
