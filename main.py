import pyautogui # pyautogui.move() to move the mouse to new position
from pynput import keyboard # Create Listener object with pynput.keyboard
import tkinter as tk # GUI
from tkinter import ttk # GUI widgets
import decimal, math # Floating point accuracy
from typing import List

# Class used to change main settings of the program, GUI interacts with it by scrollbars and input fields
class Settings:
    in_game_sensitivity = 1.0
    resolution = [1920, 1080]
    degrees_to_rotate = 360
    duration = 1.0
    fov = 90.0
    keybind = keyboard.Key.f6
    direction_left = False 
    pyautogui.FAILSAFE = False 

    def __init__(self, in_game_sensitivity: float = 1.0, resolution: List[int] = [1920, 1080], degrees_to_rotate: int = 360, fov: float = 90.0, direction_left : bool = True):
        self.in_game_sensitivity = in_game_sensitivity
        self.resolution = resolution
        self.degrees_to_rotate = degrees_to_rotate
        self.fov = fov
        self.direction_left = direction_left

# Class that is used to move the mouse as well as calculate how many pixels we want to turn the mouse for
class Mouse_movement:
    @staticmethod
    def pixels_per_degree(in_game_sensitivity: float = 1.0, resolution: List[int] = [1920, 1080], fov: float = 90.0):
        return float(round(resolution[1] / 2.0) / math.degrees(math.tan(fov/2.0)))

    @staticmethod
    def move_mouse(pos_x: int = 0, pos_y: int = 0):
        pyautogui.moveRel(pos_x, pos_y, Settings.duration)

class Inputs:
    @staticmethod
    def on_press(self, key: keyboard = keyboard.Key.f6, pos_x: int = (Mouse_movement.pixels_per_degree(Settings.in_game_sensitivity, Settings.resolution, Settings.fov)*Settings.degrees_to_rotate), pos_y: int = 0):
        if Settings.direction_left:
            pos_x = -pos_x
        try:
            if key == Settings.keybind:
                print(f'{Settings.keybind.name} key was pressed')
                print(f'Before move {pyautogui.position()}')
                print(f'{pos_x}')
                Mouse_movement.move_mouse(pos_x, pos_y)
                print(f'After move {pyautogui.position()}')
        except AttributeError:
            pass

# Slider for fov
# Slider for in-game sensitivity
# Slider for duration of rotation
# Button for keybind
# Class used to show GUI part of the program, edit fov, sensitivity, duration and change the keybind
class Gui:
    window = tk.Tk()

    def __init__(self, pos_x: int=0, pos_y: int=0):
        self.script_label = ttk.Label(master = self.window, text = 'Rotation Script', font = 'Ubuntu 18')
        self.fov_label = ttk.Label(master = self.window, text = f'Fov: {Settings.fov}')
        self.sensitivity_label = ttk.Label(master = self.window, text = f'Sensitivity: {Settings.in_game_sensitivity}')
        self.duration_label = ttk.Label(master = self.window, text = f'Duration time: {Settings.duration}')
        self.keybind_label = ttk.Label(master = self.window, text = f'Keybind: {Settings.keybind}')
        self.direction_label = ttk.Label(master = self.window, text = f'Direction (left = true, right = false): {Settings.direction_left}')

        self.window.title('xxx')
        #self.window.geometry('200x150')

        self.fov_spinbox = ttk.Spinbox(master = self.window, from_ = decimal.Decimal('10.0'), to = decimal.Decimal('180.0'), increment = 0.1, command = self.update_fov, validatecommand = (self.window.register(self.float_validate)))
        self.sensitivity_spinbox = ttk.Spinbox(master = self.window, from_ = decimal.Decimal('0.01'), to = decimal.Decimal('10.0'), increment = 0.01, command = self.update_sensitivity, validate = 'all', validatecommand = (self.window.register(self.float_validate)))
        self.duration_spinbox = ttk.Spinbox(master = self.window, from_ = decimal.Decimal('0.1'), to = decimal.Decimal('60.0'), increment = 0.1 , command = self.update_duration, validate = 'all', validatecommand = (self.window.register(self.float_validate)))
        self.keybind_button = ttk.Button(master = self.window, text = 'Change keybind', command = self.update_keybind) # TODO: Needs to listen to keybind after that instead of trying to immediately change it
        self.direction_button = ttk.Button(master = self.window, text = 'Change direction', command = self.update_direction)

        self.script_label.grid(row = 0, column = 0, columnspan = 2)

        self.fov_spinbox.grid(row = 1, column = 0)
        self.sensitivity_spinbox.grid(row = 2, column = 0)
        self.duration_spinbox.grid(row = 3, column = 0)
        self.keybind_button.grid(row = 4, column = 0)
        self.direction_button.grid(row = 5, column = 0)

        # Draw labels onto the grid
        self.fov_label.grid(row = 1, column = 1)
        self.sensitivity_label.grid(row = 2, column = 1)
        self.duration_label.grid(row = 3, column = 1)
        self.keybind_label.grid(row = 4, column = 1)
        self.direction_label.grid(row = 5, column = 1)

    def update_fov(self):
        Settings.fov = decimal.Decimal(self.fov_spinbox.get())
        self.fov_label['text'] = f'FOV: {Settings.fov}'

    def update_sensitivity(self):
        Settings.in_game_sensitivity = decimal.Decimal(self.sensitivity_spinbox.get())
        self.sensitivity_label['text'] = f'Sensitivity: {Settings.in_game_sensitivity}'

    def update_duration(self):
        Settings.duration = decimal.Decimal(self.duration_spinbox.get())
        self.duration_label['text'] = f'Duration time: {Settings.duration}s'

    def update_keybind(key):
        Settings.keybind = key

    def update_direction(self):
        Settings.direction_left = not Settings.direction_left

    # If shift, control or alt is pressed, read the next input and add that to the keybind
    def change_keybind(self, key):
        try:
            Settings.keybind = key.char
        except AttributeError:
            Settings.keybind = key.name

    def float_validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False




def run():
    # First we create settings class in order to save all the necessary info
    settings = Settings()
    # Here we ask the user for input on their in game dpi, degrees to rotate, and read their resolution

    # Calculate how much do we need to move the mouse based on dpi's, resolution and how many degrees to de want to turn
    test = Mouse_movement()
    print(f'for {settings.in_game_sensitivity} in game sens, you need {test.pixels_per_degree()} pixels of movement to turn your camera by 1 degree')

    # Create input to make action on pressed key
    input = Inputs()

    # Create listener that will run input.on_press function whenever a key is pressed
    listener = keyboard.Listener(on_press=input.on_press)
    listener.start()
    listener.join()

    gui = Gui()
    #gui.window.mainloop()

    while 1:
        input.on_press(Settings.keybind)
        gui.window.mainloop()

if __name__ == "__main__":
    run()