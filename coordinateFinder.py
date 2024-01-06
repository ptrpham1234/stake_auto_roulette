import pyautogui
from PIL import Image


def find_color_on_screen(target_color):
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example: Find the first occurrence of the color (255, 0, 0) (red)
    target_color = (31, 255, 32)
    result = find_color_on_screen(target_color)

    if result:
        print(f"Found color at coordinates: {result}")
    else:
        print("Color not found on the screen.")