import pyautogui # pyautogui.move() to move the mouse to new position
import pynput # Create Listener object with pynput.keyboard
import PyQt5
import decimal, math

class Settings:
    mouse_dpi = 1000
    in_game_sensitivity = decimal.Decimal('1.0')
    system_sensitivity = decimal.Decimal('1.0')
    resolution = (1920, 1080)
    degrees_to_rotate = 360
    fov = 90.0
    # keybind = kb_F5 

    def __init__(self, mouse_dpi: int = 1000, in_game_sensitivity: float = 1.0, system_sensitivity: float = 1.0, resolution: tuple[int, int] = [1920, 1080], degrees_to_rotate: int = 360, fov: float = 90.0):
        decimal.getcontext().prec = 6
        self.mouse_dpi = mouse_dpi
        self.in_game_sensitivity = decimal.Decimal(in_game_sensitivity)
        self.system_sensitivity = decimal.Decimal(system_sensitivity)
        self.resolution = resolution
        self.degrees_to_rotate = degrees_to_rotate
        self.fov = fov

class Gui():
    pass

class Mouse_movement():
    def pixels_per_degree(self, mouse_dpi: int = 4000, system_sensitivity: float = 1.0, in_game_sensitivity: float = 1.0, resolution: tuple[int, int] = [1920, 1080], fov: float = 90.0) -> float:
        return round(resolution[1] / 2) / math.degrees(math.tan(fov/2))

def run():
    # First we create settings class in order to save all the necessary info
    settings = Settings()
    # Here we ask the user for input on their mouse dpi, in game dpi, degrees to rotate, and read their resolution

    # Calculate how much do we need to move the mouse based on dpi's, resolution and how many degrees to de want to turn
    test = Mouse_movement()
    print(f'for {settings.mouse_dpi} dpi, {settings.in_game_sensitivity} in game sens, {settings.system_sensitivity} system sens, you need {test.pixels_per_degree()} pixels of movement to turn your camera by 1 degree')
    pass

if __name__ == "__main__":
    run()