from data import TOURNOIS, PLAYERS
import check_functions as check


class ViewTournois:

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        print("Enter name of the tournament : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break

        print("Enter place of the tournament : ")
        while True:
            place = input()
            if check.check_input_string_special(place) is True:
                if check.check_input_string_len(place) is True:
                    if check.check_input_string_integer(place) is True:
                        break

        print("Enter the date with this format YEAR-MONTH-DAY : ")
        date = check.check_date_input()

        print(
            "1: Bullet = 1 minute \n"
            "2: Blitz = 5 minute \n"
            "3: Rapid = 15 minute \n"
            "Choose a number to define the time between tour : "
        )
        time = check.request_selection_with_number(1, 5, 15)
        description = input("Enter description of the tournament : ")

        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments with id saved in tournaments.json"""
        tournament_id = 0
        print("\n")
        for tournament in TOURNOIS:
            tournament_id += 1
            print(
                f"{str(tournament_id)} : {tournament.get('name')} |"
                f" {tournament.get('place')} |"
                f" {tournament.get('date')}  |"
                f" {tournament.get('description')}"
            )

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in for create a tournament"""
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            print("The database of players need 8 saved players minimum !")
            return False
        elif get_players_numbers_saved == 8 or get_players_numbers_saved > 8:
            return True
