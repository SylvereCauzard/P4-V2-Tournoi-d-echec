from Modèles.m_players import Player
from Controllers.c_tournoi import ControllerTournois
from Controllers.c_player import ControllerJoueur
from Controllers.c_round import RoundController
from Vues.v_tournoi import ViewTournois
from Vues.v_player import ViewJoueurs
from Vues.v_round import RoundView

from data import TOURNOIS

import check_functions as check


class MenuSelection:

    def __init__(self, view) -> None:
        self.view = view
        self.tournament_view = ViewTournois()
        self.player_view = ViewJoueurs()
        self.round_view = RoundView()
        self.tournament_controller = ControllerTournois(self.tournament_view)
        self.player_controller = ControllerJoueur(self.player_view)
        self.round_controller = RoundController(self.round_view)

        self.run_main_menu = "Yes"
        self.run_menu_secondaire = "Yes"
        self.run_resultat_rounds = "Yes"

    def run_main_menu_selection(self):

        self.run_menu_secondaire = "No"
        self.run_resultat_rounds = "No"

        while self.run_main_menu == "Yes":
            choix = self.view.main_menu()
            if choix == "1":
                self.tournament_controller.get_info_tournament()
            elif choix == "2":
                self.tournament_controller.add_tournament_players()
            elif choix == "3":
                if self.tournament_controller.check_data_tournaments_numbers():
                    self.tournament_view.display_empty_tournaments_file()
                else:
                    self.round_controller.run_rounds()
            elif choix == "4":
                self.player_controller.get_info_player()
            elif choix == "5":
                if self.player_controller.check_data_players_numbers():
                    self.player_view.display_empty_players_file()
                else:
                    self.player_controller.view.show_players()
                    Player.modify_player_ranking(Player)
            elif choix == "6":
                self.run_menu_secondaire = "Yes"
                self.run_menu_secondaire_selection()
            elif choix == "7":
                self.run_main_menu = "No"
                quit()
            elif choix == "":
                print("Vous devez entrer un chiffre ! ")

    def run_menu_secondaire_selection(self) -> None:
        while self.run_menu_secondaire == "Yes":
            choix = self.view.menu_secondaire()
            if choix == "1":
                if self.tournament_controller.check_data_tournaments_numbers():
                    self.tournament_view.display_empty_tournaments_file()
                else:
                    self.tournament_controller.view.show_tournaments()
            if choix == "2":
                if self.player_controller.check_data_players_numbers():
                    self.player_view.display_empty_players_file()
                else:
                    self.player_controller.view.show_players()
            if choix == "3":
                self.tournament_controller.view.show_tournaments()
                self.player_controller.view.show_players_specific_tournament()
            if choix == "4":
                self.run_resultat_rounds = "Yes"
                self.run_resultat_rounds_selection()
            if choix == "5":
                self.run_main_menu_selection()
            if choix == "":
                print("Vous devez entrer un chiffre ! ")

    def run_resultat_rounds_selection(self) -> None:
        self.tournament_controller.view.show_tournaments()
        print("Choissisez un tournoi pour voir les résultats : ")
        tournament_id = check.request_id(TOURNOIS)
        while self.run_resultat_rounds == "Yes":
            choix = self.view.resultat_rounds(tournament_id)
            if choix == "1":
                self.tournament_view.show_rounds_results(tournament_id, "all")
            if choix == "2":
                self.tournament_view.show_rounds_results(tournament_id, "score_round_1")
            if choix == "3":
                self.tournament_view.show_rounds_results(tournament_id, "score_round_2")
            if choix == "4":
                self.tournament_view.show_rounds_results(tournament_id, "score_round_3")
            if choix == "5":
                self.tournament_view.show_rounds_results(tournament_id, "score_round_4")
            if choix == "6":
                self.run_menu_secondaire_selection()


