from data import PLAYERS, TOURNOIS
from Modèles.m_players import Player
import check_functions as check

import json


class ViewJoueurs:

    def ask_info_player(self) -> str:
        """Get info of a player"""

        print("Entrer le nom de famille : ")
        while True:
            family_name = input()
            if check.check_input_string_special(family_name) is True:
                if check.check_input_string_len(family_name) is True:
                    if check.check_input_string_integer(family_name) is True:
                        break

        print("Entrer le prénom : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break

        print("Entrer la date de naissance sous ce format YEAR-MONTH-DAY :  ")
        birthday = check.check_date_input()

        print(
            "Choissez un chiffre pour le sexe : \n"
            "1 - Homme \n"
            "2 - Femme"
        )
        sexe = check.request_selection_with_number("Man", "Women", "none")

        print("Entrer le classement du joueur : ")
        classement = check.request_number()

        print("\n Le joueur {} {}, {}, né le {} avec {} d'elo a été rajouté à la base de donnée !".format(
            family_name,
            name,
            sexe,
            birthday,
            classement))

        return family_name, name, sexe, birthday, classement

    def show_players(self):
        """Show all players with id in players.json in alphabetical order or by ranking according user choice"""
        liste_players = []
        for players in PLAYERS:
            data_player = (
                    f"{players.get('family_name')} |"
                    f"{players.get('name')} |"
                    f"{players.get('birthday')} |"
                    f"{players.get('sexe')} |"
                    f"{players.get('classement')}"
            )
            liste_players.append(data_player)

        print(
            "Voulez vous la liste des joueurs par ordre alphabétique ou de classement ? \n"
            "1 - Liste des joueurs par classement \n"
            "2 - Liste des joueurs par ordre alphabétique"
            )
        choix = check.request_selection_with_number("classement", "alphabétique", "None")
        if choix == "classement":
            player_classement = 0
            liste_players = sorted(liste_players, key=lambda player: player_classement)
            print("*******************************************")
            print("Liste de tous les joueurs par classement : ")
            print("*******************************************")
            for player in liste_players:
                player_classement += 1
                print(str(player_classement) + " : " + str(player))
        elif choix == "alphabétique":
            player_id = 0
            print("***************************************************")
            print("Liste de tous les joueurs par ordre alphabétique : ")
            print("***************************************************")
            for player in liste_players:
                player_id += 1
                print(str(player_id) + " : " + str(player))

    def show_players_specific_tournament(self) -> None:
        """Show player of specific tournament"""
        id_choice = check.request_id(TOURNOIS)
        tournament_data = TOURNOIS.get(doc_id=id_choice)
        if tournament_data.get("players") == {}:
            print("\n Ce tournoi n'a pas encore de joueurs")
        else:
            players_list = tournament_data.get("players")
            deserialized_player_list = []
            for player_data in players_list:
                deserialized_player = Player(**json.loads(player_data))
                deserialized_player_list.append(deserialized_player)
            print(
                "Voulez vous la liste des joueurs par ordre alphabétique ou de classement ? \n"
                "1 - Liste des joueurs par classement \n"
                "2 - Liste des joueurs par ordre alphabétique"
            )
            choix = check.request_selection_with_number("alphabétique", "classement", "None")
            if choix == "alphabétique":
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.family_name)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)
            elif choix == "classement":
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.classement)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)

    def create_players_id_dict(self):
        """Request 8 id of players saved in players.json and return dict like this player_1 = id_selected ect"""
        players_id = []
        self.show_players()
        print("\n" + "Entrer l'id des joueurs voulu : ")
        while len(players_id) < 8:
            while True:
                id_choice = check.request_id(PLAYERS)
                if check.check_not_same_value(players_id, id_choice) is True:
                    players_id.append(id_choice)
                    break
        return players_id

    def display_empty_players_file(self) -> None:
        """Simply display message if players.json are empty"""
        print("\nAucun joueur n'a été encore créé!")
