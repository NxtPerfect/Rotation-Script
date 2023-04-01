import pyautogui # pyautogui.move() to move the mouse to new position
from pynput import keyboard # Create Listener object with pynput.keyboard
import PyQt5
import decimal, math

class Settings:
    mouse_dpi = 1000
    in_game_sensitivity = decimal.Decimal('1.0')
    system_sensitivity = decimal.Decimal('1.0')
    resolution = (1920, 1080)
    degrees_to_rotate = 360
    fov = 90.0
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

class Gui:
    pass

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
    listener = keyboard.Listener(on_press=input.on_press)
    listener.start()
    listener.join()

    while 1:
        input.on_press(keyboard.Key.f6)

if __name__ == "__main__":
    run()