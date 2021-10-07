from Modèles.m_players import Player
from datetime import datetime
import check_functions as check

class RoundView:
    """Round view"""

    def request_specific_number_only(self, player_a: Player, player_b: Player) -> float:
        """request user entry for specific number only, player_a and player_b parameter is for print player name"""
        print("**********************")
        print(str(player_a.family_name.upper()) + " versus " + str(player_b.family_name.upper()))
        print("**********************")
        while True:
            result = input(
                "Enter the result of " + str(player_a.family_name.upper()) + " : "
            )
            result = float(result)
            if result == 1:
                print(
                    str(player_a.family_name.upper()) + " : WINNER \n" +
                    str(player_b.family_name.upper()) + " : LOSING \n"
                    )
                return result
            elif result == 0.5:
                print(
                    str(player_a.family_name.upper()) + " : EQUALITY \n" +
                    str(player_b.family_name.upper()) + " : EQUALITY \n"
                    )
                return result
            elif result == 0:
                print(
                    str(player_a.family_name.upper()) + " : LOSING \n" +
                    str(player_b.family_name.upper()) + " : WINNER \n"
                    )
                return result
            else:
                print("You must enter [1], [0.5] or [0] : ")

    def request_id(self, data_file) -> int:
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

    def get_actual_date_and_time(self) -> str:
        """get actual date and time and return them"""
        now = datetime.now()
        date_string = now.strftime("%Y/%m/%d %H:%M:%S")
        return date_string

    def display_rounds_message(self, round_number: str, when: str) -> str:
        """
        display round number when round is launched
        display date and time too with when parameter :
        "start" = round start time
        "end" = round end time
        """
        if when == "start":
            date_and_time = check.get_actual_date_and_time()
            print(
                "**********************\n" +
                "       ROUND " + round_number + "\n" +
                " Start date and time  \n" +
                " " + date_and_time + "\n"
                "======================\n" +
                "| 1   - for winner   |\n" +
                "| 0.5 - for equality |\n" +
                "| 0   - for defeated |\n" +
                "**********************"
                )
        elif when == "end":
            date_and_time = check.get_actual_date_and_time()
            print(
                "**********************\n" +
                "       ROUND " + round_number + "\n" +
                "  End date and time  \n" +
                " " + date_and_time + "\n"
                "**********************"
                )
        return date_and_time

    def button_continue_to_next_round(self) -> None:
        """simply print message for continue tournament or not"""
        print("Do you want to continue to the next Round ?")
        print(
            "1 - Continue to the next Round\n"
            "2 - Exit and save"
            )
