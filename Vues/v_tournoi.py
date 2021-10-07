from data import TOURNOIS, PLAYERS
import check_functions as check


class ViewTournois:

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        print("Entrer le nom du tournoi : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break

        print("Entrer le lieu du tournoi : ")
        while True:
            place = input()
            if check.check_input_string_special(place) is True:
                if check.check_input_string_len(place) is True:
                    if check.check_input_string_integer(place) is True:
                        break

        print("Entrer la date de départ du tournoi sous ce format YEAR-MONTH-DAY : ")
        start_date = check.check_date_input()
        print("Entrer la date de fin du tournoi sous ce format YEAR-MONTH-DAY : ")
        end_date = check.check_date_input()
        date = f"{start_date} to {end_date}"

        print(
            "1: Bullet = 1 minute \n"
            "2: Blitz = 5 minute \n"
            "3: Rapid = 15 minute \n"
            "Choissisez un numéro pour définir le temps des matchs : "
        )
        time = check.request_selection_with_number(1, 5, 15)
        description = input("Description du tournoi : ")

        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments with id saved in tournaments.json"""
        tournament_id = 0
        print("Liste de tous les tournois : ")

        for tournament in TOURNOIS:
            tournament_id += 1
            print(
                f"{str(tournament_id)} : {tournament.get('name')} |"
                f" {tournament.get('place')} |"
                f" {tournament.get('date')}  |"
                f" Time : {tournament.get('time')} |"
                f" {tournament.get('description')}"
            )

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in for create a tournament"""
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            print("Il vous faut un minimum de 8 joueurs enregistrés dans la base de donnée !")
            return False
        elif get_players_numbers_saved == 8 or get_players_numbers_saved > 8:
            return True

    def show_rounds_results(self, tournament_id, selected_round: str) -> None:
        """
        Show the results of selected round, "score_round_1", "score_round_2" ect...
        Use "all" for all rounds.
        """
        tournament_data = TOURNOIS.get(doc_id=tournament_id)

        if selected_round == "all":
            round_1 = tournament_data.get("score_round_1")
            round_2 = tournament_data.get("score_round_2")
            round_3 = tournament_data.get("score_round_3")
            round_4 = tournament_data.get("score_round_4")
            print("===================")
            print("|RESULTAT ROUND 1|")
            print("===================")
            print("START TIME :")
            print(round_1[4][0])
            print("END TIME :")
            print(round_1[4][1])
            print("___________________________")
            for tuple_round_1 in round_1[0:4]:
                print(tuple_round_1)
            print("___________________________")
            print("===================")
            print("|RESULTAT ROUND 2|")
            print("===================")
            print("START TIME :")
            print(round_2[4][0])
            print("END TIME :")
            print(round_2[4][1])
            print("___________________________")
            for tuple_round_2 in round_2[0:4]:
                print(tuple_round_2)
            print("___________________________")
            print("===================")
            print("|RESULTAT ROUND 3|")
            print("===================")
            print("START TIME :")
            print(round_3[4][0])
            print("END TIME :")
            print(round_3[4][1])
            print("___________________________")
            for tuple_round_3 in round_3[0:4]:
                print(tuple_round_3)
            print("___________________________")
            print("===================")
            print("|RESULTAT ROUND 4|")
            print("===================")
            print("START TIME :")
            print(round_4[4][0])
            print("END TIME :")
            print(round_4[4][1])
            print("___________________________")
            for tuple_round_4 in round_4[0:4]:
                print(tuple_round_4)
            print("___________________________")
        else:
            round = tournament_data.get(selected_round)
            print("===================")
            print(f"|RESULTAT DE {selected_round.replace('score_', '').replace('_', ' ').upper()}|")
            print("===================")

            print("START TIME :")
            print(round[4][0])
            print("END TIME :")
            print(round[4][1])

            print("___________________________")
            for tuple_round in round[0:4]:
                print(tuple_round)
            print("___________________________")

    def display_selected_players(self, deserialized_players_list) -> None:
        """Display a message for print selected players of a tournament"""
        print("Les joueurs sélectionés ont été ajouté au tournoi :\n")
        for player in deserialized_players_list:
            print(player)
        print("\n")

    def display_choose_a_tournament(self) -> None:
        """simply print a message"""
        print("\nChoissisez un tournoi pour y ajouter des joueurs : ")

    def display_empty_tournaments_file(self) -> None:
        """Simply display message if tournaments.json are empty"""
        print("\nAncun tournoi n'a été encore créé")
