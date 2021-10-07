from string import digits, punctuation
import datetime



def check_input_string_len(string_to_check) -> bool:
    """Check input string entry for enter 2 character minimum"""
    if len(string_to_check) < 2:
        print("The minimum number of characters required is 2 : ")
        return False
    return True


def check_input_string_integer(string_to_check) -> bool:
    """check if string have numbers in, return True or False"""
    for number in digits:
        if number in string_to_check:
            print("No numbers allowed : ")
            return False
    return True


def check_input_string_special(string_to_check) -> bool:
    """Check input string entry for not to use special characters"""
    for symbol in punctuation:
        if symbol in string_to_check:
            print("No special character allowed : ")
            return False
    return True


def check_date_input() -> str:
    """Check if input date string is a date format"""
    while True:
        try:
            date = input()
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("The correct date format is YEAR-MONTH-DAY : ")


def check_not_same_value(players_id: dict, id_choice: int) -> bool:
    """check if dict contains two same values and return True or false"""
    for value in players_id.values():
        if value == id_choice:
            print("You already selected this player : ")
            return False
    return True


def request_id(data_file) -> int:
    """request user entry for integer only"""
    while True:
        try:
            id_choice = int(input())
        except ValueError:
            print("Enter only numbers : ")

        object_counter = 0
        for object in data_file:
            object_counter += 1
        if id_choice > object_counter:
            print("Select a valid id : ")
        elif id_choice == 0:
            print("Select a valid id : ")
        else:
            return id_choice


def request_selection_with_number(option_1: str or int, option_2: str or int, option_3: str or int) -> str:
    """
    Take user integer entry only, and assign string variable:
    variable = [1] for option_1 | [2] for option_2 | [3] for option_3
    option_3 is optional enter "none" for delete it.
    """
    while True:
        try:
            result = int(input())
        except TypeError:
            print("Enter a valid number : ")
        if result == 1:
            return str(option_1)
        elif result == 2:
            return str(option_2)
        elif result == 3:
            if option_3 == "none":
                print("Enter a valid number : ")
            else:
                return str(option_3)
        elif len(str(result)) >= 2:
            print("Enter a valid number : ")
        else:
            print("Enter a valid number : ")


def request_number() -> int:
    while True:
        try:
            result = int(input())
        except TypeError:
            print("Enter a valid number : ")

        return result

def get_actual_date_and_time() -> str:
    """get actual date and time and return them"""
    now = datetime.now()
    date_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return date_string
