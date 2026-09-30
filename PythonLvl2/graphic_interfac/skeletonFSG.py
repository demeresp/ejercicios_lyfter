import FreeSimpleGUI as fsg

layout = [
    [fsg.Text("Greetings")], 
        ]

window = fsg.Window("Program 1", layout)

#evento loop
while True:
    event, values = window.read()
    #proces event

    if event == fsg.WIN_CLOSED:
        break

