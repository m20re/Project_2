import PySimpleGUI as sg

layout = [
    [sg.Text('Random User Generator', enable_events=True, font=("Arial", 24), key = '-HEADERTEXT-')],
    [sg.Text('Name: ', font=("Arial", 12), key='-NAMETEXT-'), sg.Image(key='Image')],
    [sg.Text('Gender: ', font=("Arial", 12), key='-GENDERTEXT-')],
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

    if event == '-BUTTON1-':
        window['-TEXT-'].update(visible = False)

    if event == '-BUTTON2-':
        print('This button was pressed')
    
    if event == '-TEXT-':
        print('This text was pressed')

window.close()
