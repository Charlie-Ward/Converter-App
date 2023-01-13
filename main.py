import PySimpleGUI as sg

layout = [
    [sg.Text('Converter')],
    [sg.Input(key = 'NumberInput'), sg.Spin(['km to mile', 'kg to pounds', 'sec to min'], key = 'SelectorInput'),
     sg.Button('Convert', key = 'Button1')],
    [sg.Text('Converted Product will appear hear', key = 'OutputText')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Button1':
        input_value = values['NumberInput']
        convert_type = values['SelectorInput']
        if input_value.isnumeric():
            if convert_type == 'km to mile':
                output = round(float(input_value) * 0.6214, 2)
                output_string = f'{input_value} km are {output} miles.'
            elif convert_type == 'kg to pounds':
                output = round(float(input_value) * 2.205, 2)
                output_string = f'{input_value} kg are {output} pounds.'
            elif convert_type == 'sec to min':
                output_mins = round(float(input_value) // 60, 1)
                output_secs = round(float(input_value) % 60, 1)
                output_string = f'{input_value} secs are {output_mins} mins and {output_secs} secs.'
            window['OutputText'].update(output_string)
        else:
            window['OutputText'].update('Please enter a number')

window.close()
