import PySimpleGUI as sg

OptionValues = ['WEIGHT' ,'kg to pounds','pounds to kg' ,'DISTANCE' , 'km to mile','mile to km' ,"TIME" ,'min to sec' , "sec to min", 'TEMPERATURE', '°C to °F', '°F to °C']

NotAllowedOptions = ["SELECT UNITS", "WEIGHT", "DISTANCE", "TIME", "TEMPERATURE"]

layout = [
	[sg.Text("Converting App")],
	[sg.Input(key = "numberInput"), sg.OptionMenu(values = OptionValues, key = "selectionInput", default_value = "SELECT UNITS"), sg.Button('Convert', key = 'Button1')],
	[sg.Text('Converted Product will appear hear', key = 'OutputText')]
]

window = sg.Window("Converter", layout)

while True:
	event, values = window.read()
	
	if event == sg.WIN_CLOSED:
		break
	if event == "Button1":
		inputValue = values['numberInput']
		inputType = values['selectionInput']
		for i in range(len(NotAllowedOptions)):
			if inputType == NotAllowedOptions[i]:
				window['OutputText'].update("Please select a correct unit type")
				break
		if inputValue == "":
			window['OutputText'].update('Please enter a number')
		else:
			if inputType == 'kg to pounds':
				Converted = round(float(inputValue) * 2.205, 1)
				ConvertText = f'{inputValue}kg = {Converted} pound'
				window['OutputText'].update(ConvertText)
			elif inputType == 'pounds to kg':
				Converted = round(float(inputValue)/ 2.205, 1)
				ConvertText = f'{inputValue} pound = {Converted}kg'
				window['OutputText'].update(ConvertText)
			elif inputType == "km to mile":
				Converted = round(float(inputValue)/ 1.609, 1)
				ConvertText = f'{inputValue}km = {Converted} mile'
				window['OutputText'].update(ConvertText)
			elif inputType == "mile to km":
				Converted = round(float(inputValue)* 1.609, 1)
				ConvertText = f'{inputValue} mile = {Converted}km'
				window['OutputText'].update(ConvertText)
			elif inputType == "min to sec":
				Converted = round(float(inputValue) * 60, 1)
				ConvertedText = f'{inputValue} minutes = {Converted} seconds'
				window['OutputText'].update(ConvertedText)
			elif inputType == "sec to min":
				ConvertedMins = round(float(inputValue) // 60, 1)
				ConvertedSecs = round(float(inputValue) % 60, 1)
				Converted = f'{inputValue} seconds = {ConvertedMins} minutes and {ConvertedSecs} seconds'
				window['OutputText'].update(Converted)
			elif inputType == "°C to °F":
				Converted = round(float(inputValue)) /* need to finish */