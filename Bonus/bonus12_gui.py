import FreeSimpleGUI as sg
from converter import converter

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")

inch_label = sg.Text("Enter Inches")
inch_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inch_label, inch_input],
                           [convert_button, output_label]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = converter(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()
