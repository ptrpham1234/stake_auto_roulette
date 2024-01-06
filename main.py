import pyautogui
import time
import keyboard
import random

number_coordinates = ["(855, 533)", "(909, 640)", "(909, 586)", "(909, 533)", "(963, 640)", "(963, 586)", "(963, 533)",
                      "(1016, 640)", "(1016, 586)", "(1016, 533)", "(1070, 640)", "(1070, 586)", "(1070, 533)",
                      "(1124, 640)", "(1124, 586)", "(1124, 533)", "(1178, 640)", "(1178, 586)", "(1178, 533)",
                      "(1232, 640)", "(1232, 586)", "(1232, 533)", "(1285, 640)", "(1285, 586)", "(1285, 533)",
                      "(1339, 640)", "(1339, 586)", "(1339, 533)", "(1393, 640)", "(1393, 586)", "(1393, 533)",
                      "(1447, 640)", "(1447, 586)", "(1447, 533)", "(1501, 640)", "(1501, 586)", "(1501, 533)"]


def main():
    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
                         10946,
                         17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
    fibonacci_tracker = 0
    fail_count = 0

    current_dozen_bet = 1

    number_history = []
    win_history = []

    click_clear()
    click_bet(current_dozen_bet, 1)
    click_play()
    rounds_without_hit = [0, 0, 0, 0]

    try:
        while True:

            # wait for the wheel to stop spinning then find the color on the screen
            time.sleep(3.1)
            winning_number = get_number()

            # If there is a number that the program doesn't know which should be a bug
            if winning_number is None:
                print("uhh oh unknown number. double check it!")
                if fail_count > 1:
                    break
                else:
                    print("Retrying")
                    fail_count += 1
                    continue

            number_history.append(winning_number)

            winning_dozen = (winning_number - 1) // 12 + 1

            if winning_dozen == 1:
                rounds_without_hit[1] = 0
                rounds_without_hit[2] += 1
                rounds_without_hit[3] += 1

            elif winning_dozen == 2:
                rounds_without_hit[1] += 1
                rounds_without_hit[2] = 0
                rounds_without_hit[3] += 1

            elif winning_dozen == 3:
                rounds_without_hit[1] += 1
                rounds_without_hit[2] += 1
                rounds_without_hit[3] = 0

            else:  # if it hits a 0
                rounds_without_hit[1] += 1
                rounds_without_hit[2] += 1
                rounds_without_hit[3] += 1

            print(f"Winning number: {winning_number}")
            print(f"Rounds without hits: {rounds_without_hit}")



            # If the winning dozen is not the current dozen bet meaning you lost
            if winning_dozen != current_dozen_bet:
                print("You lost :(")
                time.sleep(.5)
                win_history.append(False)
                click_bet(current_dozen_bet, fibonacci_numbers[fibonacci_tracker])
                time.sleep(1)
                click_play()

                fibonacci_tracker += 1

            else:
                print("You win!\n\n")
                time.sleep(.5)
                win_history.append(True)
                click_clear()

                time.sleep(.5)
                dozenPick = pickDozen(rounds_without_hit)

                click_bet(dozenPick, 1)
                click_play()
                time.sleep(.5)
                print("\n\n")

                current_dozen_bet = dozenPick
                fibonacci_tracker = 0


    except KeyboardInterrupt:
        print("interrupt")
        print()
        print(f"Number History: {number_history}")
        print(f"Win History: {win_history}")

        # count the max number of consecutive loses
        max_consecutive_false = 0
        current_consecutive_false = 0
        for value in win_history:
            if value is False:
                current_consecutive_false += 1
                if current_consecutive_false > max_consecutive_false:
                    max_consecutive_false = current_consecutive_false
            else:
                current_consecutive_false = 0

        print(f"Max Consecutive Loses: {max_consecutive_false}")



#############################################################################################################
# Function:            click_bet
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def click_bet(dozen, amount):

    if dozen == 1:
        x, y = (1013, 708)
    elif dozen == 2:
        x, y = (1228, 716)
    else:
        x, y = (1440, 715)

    while amount:
        pyautogui.click(x, y)
        time.sleep(0.1)
        amount -= 1

    time.sleep(.3)

#############################################################################################################
# Function:            click_play
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def click_play():
    pyautogui.click(625, 469)
    time.sleep(.3)

#############################################################################################################
# Function:            click_clear
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def click_clear():
    pyautogui.click(1629, 818)
    time.sleep(.3)

#############################################################################################################
# Function:            get_number
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def get_number():
    # Example: Find the first occurrence of the color (31, 255, 32) (green)
    target_color = (31, 255, 32)
    result = str(find_color_on_screen(target_color))
    print(f"Coordinates Found: {result}")

    if result in number_coordinates:
        return number_coordinates.index(result)
    else:
        return None

#############################################################################################################
# Function:            find_color_on_screen
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
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

#############################################################################################################
# Function:            dozenPick
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def pickDozen(lst: list):
    choice = max(lst)
    choice_index = pickFromList(lst, choice)

    print(f"Number to pick {choice}")
    print(f"Selected index {choice_index}")
    print(f"List: {lst}")
    return choice_index


#############################################################################################################
# Function:            find_indexes_of_number
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def pickFromList(lst: list, choice: int) -> int:
    if lst.count(choice) > 1:
        duplicate_indexes = find_indexes_of_number(lst, choice)
        print(f"Indexes of duplicate values: {duplicate_indexes}")
        choice_index = random.choice(duplicate_indexes)
    else:
        print(f"Index of choice: {lst.index(choice)}")
        choice_index = lst.index(choice)

    return choice_index

#############################################################################################################
# Function:            find_indexes_of_number
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
def find_indexes_of_number(lst, number):
    return [index for index, value in enumerate(lst) if value == number]

#############################################################################################################
# Function:            establishConnection
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
# Receive the file id to stream from the user and then close the connection
#############################################################################################################
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
