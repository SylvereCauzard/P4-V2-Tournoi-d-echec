from data import PLAYERS, TOURNOIS
from Modèles.m_players import Player
import check_functions as check

import json


class ViewJoueurs:

    def ask_info_player(self) -> str:
        """Get info of a player"""

        print("Enter family name : ")
        while True:
            family_name = input()
            if check.check_input_string_special(family_name) is True:
                if check.check_input_string_len(family_name) is True:
                    if check.check_input_string_integer(family_name) is True:
                        break

        print("Enter last name : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break

        print("Enter date of birth with this format YEAR-MONTH-DAY :  ")
        birthday = check.check_date_input()

        print(
            "Enter a number for choose the gender : \n"
            "1 - Man \n"
            "2 - Women"
        )
        sexe = check.request_selection_with_number("Man", "Women", "none")

        print("Enter the classement of the Player : ")
        classement = check.request_number()

        print("\n The player {} {}, {}, birth on {} with {} elo has been added to the database !".format(
            family_name,
            name,
            sexe,
            birthday,
            classement))

        return family_name, name, sexe, birthday, classement

    def show_players(self):
        """Show all players with id in players.json in alphabetical order or not according to the user choice"""
        liste_player = []
        for player in PLAYERS:
            data_player = (
                    str(player.get("family_name")) + " " +
                    str(player.get("name")) + " | " +
                    str(player.get("birthday")) + " | " +
                    str(player.get("sexe")) + " | " +
                    str(player.get("classement"))
            )
            liste_player.append(data_player)

        print(
            "Do you want the list of players by alphabetical order or by ranking ? \n"
            "1 - Ranking players list \n"
            "2 - Alphabetical players list"
            )
        choice = check.request_selection_with_number("ranking", "alphabetical", "None")
        if choice == "ranking":
            player_id = 0
            players_list = sorted(liste_player, key=lambda player: players_list[4])
            print("******************************************")
            print("List of all Players in ranking order : ")
            print("******************************************")
            for player in players_list:
                player_id += 1
                print(str(player_id) + " : " + player)
        elif choice == "alphabetical":
            player_id = 0
            liste_player.sort()
            print("******************************************")
            print("List of all Players in alphabetical order : ")
            print("******************************************")
            for player in liste_player:
                player_id += 1
                print(str(player_id) + " : " + player)

    def show_players_specific_tournament(self) -> None:
        """Show player of specific tournament"""
        id_choice = check.request_id(TOURNOIS)
        tournament_data = TOURNOIS.get(doc_id=id_choice)
        if tournament_data.get("players") == {}:
            print("\n This tournaments has no players yet")
        else:
            players_list = tournament_data.get("players")
            deserialized_player_list = []
            for player_data in players_list:
                deserialized_player = Player(**json.loads(player_data))
                deserialized_player_list.append(deserialized_player)
            print(
                "Do you want the list of players by alphabetical order or by ranking ? \n"
                "1 - Ranking players list \n"
                "2 - Alphabetical players list"
            )
            choice = check.request_selection_with_number("alphabetical", "ranking", "None")
            if choice == "alphabetical":
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.first_name)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)
            elif choice == "ranking":
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.ranking)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)

    def create_players_id_dict(self) -> dict:
        """Request 8 id of players saved in players.json and return dict like this player_1 = id_selected ect"""
        players_id = {}
        key = 0
        self.show_players()
        print("\n" + "Enter id of wanted players : ")
        while len(players_id) < 8:
            while True:
                id_choice = check.request_id(PLAYERS)
                if check.check_not_same_value(players_id, id_choice) is True:
                    key += 1
                    players_id["player_{0}".format(str(key))] = id_choice
                    break
        return players_id

    def display_empty_players_file(self) -> None:
        """Simply display message if players.json are empty"""
        print("\nNo players has been created yet")
