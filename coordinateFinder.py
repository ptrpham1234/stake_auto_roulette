import time
import pyautogui
import pygame
import os


def find_color_on_screen(target_color):
    pyautogui.moveTo(440, 660)
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to an RGB image
    image = screenshot.convert("RGB")

    # Get the size of the image
    width, height = image.size

    # Iterate through each pixel to find the target color
    for x in range(width):
        for y in range(height):
            pixel_color = image.getpixel((x, y))
            if pixel_color == target_color:
                return x, y  # Return the coordinates of the first occurrence

    return None  # Return None if the color is not found

def play_sound():
    # Initialize pygame
    pygame.init()

    # Get the current working directory
    current_directory = os.getcwd()

    # Your data path (replace 'data' with your actual data path)
    sound_path = 'data/sounds/mixkit-atm-cash-machine-key-press-2841.wav'

    # Join the current directory with the data path
    sound_file = os.path.join(current_directory, sound_path)

    # Load a sound file (replace 'path/to/your/soundfile.mp3' with the actual path to your sound file)
    pygame.mixer.music.load(sound_file)

    # Play the sound
    pygame.mixer.music.play()

    # Add a delay to allow the sound to play
    time.sleep(1)  # Adjust the sleep time as needed

    # Stop the sound
    pygame.mixer.music.stop()

    # Quit pygame
    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example: Find the first occurrence of the color (255, 0, 0) (red)
    print("Starting get ready")
    time.sleep(2)
    target_color = (120, 251, 83)
    result = find_color_on_screen(target_color)

    if result:
        print(f"Found color at coordinates: {result}")
    else:
        print("Color not found on the screen.")

    play_sound()