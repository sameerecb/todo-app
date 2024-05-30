import PySimpleGUI as sg


def km_to_miles(km):
    return km / 1.6


label1 = sg.Text("Kilometer: ")
input1 = sg.InputText(tooltip="Enter Kilometer", key="kms")
button = sg.Button("Convert")
output = sg.Text(key="output")


window = sg.Window("KM to Miles Converter", layout=[[label1, input1], [button, output]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break


window.close()