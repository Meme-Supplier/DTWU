import os
import webbrowser
import sys

def clearscreen():
    os.system('cls') #clears the screen

def apptypeselection():

    print('Select category:\n')
    print('[1] Utilities')
    print('[2] Productivity\n')

    answer = input('Select: ')

    if answer == '1': # Productivity selected
        # Add the subfolder to the system path
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps')))

        # Now you can import the module
        import utilities

        # Use the imported function
        print(utilities.utilityselect())

    if answer == '2': # Productivity selected
        # Add the subfolder to the system path
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps')))

        # Now you can import the module
        import productivity

        # Use the imported function
        print(productivity.productivityselect())

apptypeselection()
