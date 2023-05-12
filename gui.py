import PySimpleGUI as sg
from user import *

def update_screen() -> None:
    """
    Updates all of the screen elements to reflect new user data
    :return: None
    """
    if ISERROR:
        hide_password_error()
    window['-NAMETEXT-'].update(f'Name: {user_data[0]}')
    window['-GENDERTEXT-'].update(f'Gender: {user_data[1]}')
    window['-EMAILTEXT-'].update(f'Email: {user_data[2]}')
    window['-PHONETEXT-'].update(f'Phone: {user_data[3]}')
    window['-USERNAMETEXT-'].update(f'Username: {user_data[4]}')
    window['-PASSWORDTEXT-'].update(f'Password: {user_data[5]}')
    display_image(user_data[6])

def display_password_error() -> None:
    window['-ERRORTEXT-'].update(visible=True)

def hide_password_error() -> None:
    window['-ERRORTEXT-'].update(visible=False)

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
    [sg.Button('Generate New Password', font=("Arial", 12), key='-BUTTON2-'), sg.Push(), sg.Button('Generate User', font=("Arial", 12), key='-BUTTON-')],
    [sg.Text('Generate a user first', font=("Arial", 12), visible=False, justification='c', key='-ERRORTEXT-')]
    ]
window = sg.Window('Converter', layout)
ISFIRST = True
ISERROR = False

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        user_data = list(generate_user_info())
        # full_name, gender, email, phone, username, password, img_url = generate_user_info()
        update_screen()
        if ISFIRST:
            write_header_csv('output.csv')
            ISFIRST = False
        write_user_row_csv(user_data, 'output.csv')
            
    if event == '-BUTTON2-':
        try:
            user_data[5] = generate_new_password()
            update_screen()
            write_user_row_csv(user_data, 'output.csv')
        except NameError:
            ISERROR = True
            display_password_error()



window.close()
