import pyautogui # pyautogui.move() to move the mouse to new position
from pynput import keyboard # Create Listener object with pynput.keyboard
import tkinter as tk # GUI
from tkinter import ttk # GUI widgets
import decimal, math # Floating point accuracy

# Class used to change main settings of the program, GUI interacts with it by scrollbars and input fields
class Settings:
    mouse_dpi = 1000
    in_game_sensitivity = decimal.Decimal('1.0')
    system_sensitivity = decimal.Decimal('1.0')
    resolution = (1920, 1080)
    degrees_to_rotate = 360
    fov = 90.0
    duration = decimal.Decimal('1.0')
    keybind = keyboard.Key.f6 

    def __init__(self, mouse_dpi: int = 1000, in_game_sensitivity: float = 1.0, system_sensitivity: float = 1.0, resolution: tuple[int, int] = [1920, 1080], degrees_to_rotate: int = 360, fov: float = 90.0):
        decimal.getcontext().prec = 6
        self.mouse_dpi = mouse_dpi
        self.in_game_sensitivity = decimal.Decimal(in_game_sensitivity)
        self.system_sensitivity = decimal.Decimal(system_sensitivity)
        self.resolution = resolution
        self.degrees_to_rotate = degrees_to_rotate
        self.fov = fov

class Inputs:
    def on_press(self, key = keyboard.Key.f6, pos_x: int = pyautogui.size()[0]/10, pos_y: int = pyautogui.size()[1]/10):
        try:
            if key == keyboard.Key.f6:
                print('F6 key was pressed')
                print(f'Before move {pyautogui.position()}')
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
    script_label = ttk.Label(master = window, text = 'Rotation Script', font = 'Ubuntu 18')

    fov_label = ttk.Label(master = window, text = f'FOV: {Settings.fov}')
    sensitivity_label = ttk.Label(master = window, text = f'Sensitivtiy: {Settings.in_game_sensitivity}')
    duration_label = ttk.Label(master = window, text = f'Duration time: {Settings.duration}')
    keybind_label = ttk.Label(master = window, text = f'Keybind: {Settings.keybind}')

    fov_scale = ttk.Scale(master = window, orient = 'horizontal', from_ = 10.0, to = 180.0, value = Settings.fov) 
    sensitivity_scrollbar = ttk.Scrollbar()
    duration_scrollbar = ttk.Scrollbar()
    keybind_button = ttk.Button()


    def __init__(self, pos_x: int=0, pos_y: int=0):
        self.window.title('xxx')
        self.window.geometry('200x150')

        self.fov_scale.grid(row = 1, column = 0)

        # Draw labels onto the grid
        self.fov_label.grid(row = 1, column = 1)
        self.sensitivity_label.grid(row = 2, column = 1)
        self.duration_label.grid(row = 3, column = 1)
        self.keybind_label.grid(row = 4, column = 1)
        # label
        #self.script_label.pack()

# Class that is used to move the mouse as well as calculate how many pixels we want to turn the mouse for
class Mouse_movement:
    def pixels_per_degree(self, mouse_dpi: int = 4000, system_sensitivity: float = 1.0, in_game_sensitivity: float = 1.0, resolution: tuple[int, int] = [1920, 1080], fov: float = 90.0) -> float:
        return round(resolution[1] / 2) / math.degrees(math.tan(fov/2))

    def move_mouse(pos_x: int = 0, pos_y: int = 0):
        pyautogui.moveRel(pos_x, pos_y, 2)

def run():
    # First we create settings class in order to save all the necessary info
    settings = Settings()
    # Here we ask the user for input on their in game dpi, degrees to rotate, and read their resolution

    # Calculate how much do we need to move the mouse based on dpi's, resolution and how many degrees to de want to turn
    test = Mouse_movement()
    print(f'for {settings.mouse_dpi} dpi, {settings.in_game_sensitivity} in game sens, {settings.system_sensitivity} system sens, you need {test.pixels_per_degree()} pixels of movement to turn your camera by 1 degree')

    # Create input to make action on pressed key
    input = Inputs()

    # Create listener that will run input.on_press function whenever a key is pressed
    #listener = keyboard.Listener(on_press=input.on_press)
    #listener.start()
    #listener.join()

    gui = Gui()
    gui.window.mainloop()

    #while 1:
    #    input.on_press(keyboard.Key.f6)

if __name__ == "__main__":
    run()