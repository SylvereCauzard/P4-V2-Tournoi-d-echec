from Modèles.m_tournoi import Tournoi
from Controllers.c_player import ControllerJoueur
from Vues.v_player import ViewJoueurs

import check_functions as check

from data import TOURNOIS

from tinydb import where


class ControllerTournois:

    def __init__(self, view) -> None:
        self.view = view
        self.player_view = ViewJoueurs
        self.player_controller = ControllerJoueur(self.player_view)

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.view.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournoi(name, place, date, time, description)
        tournament.save()
        print("\n The tournament named '{}' has been saved !".format(name))

    def add_tournament_players(self):
        """Add 8 serialized players to a selected tournament"""
        if self.check_data_tournaments_numbers():
            self.view.display_empty_tournaments_file()
        else:
            self.view.show_tournaments()
            self.view.display_choose_a_tournament()
            tournament_id = check.request_id(TOURNOIS)
            tournament = Tournoi.deserialize_tournament(Tournoi, tournament_id)
            tournament.players = self.player_controller.instantiates_players()
            tournament_data = TOURNOIS.get(doc_id=tournament_id)
            serialized_players_list = []

            for player in tournament.players:
                serialized_player = player.serialize()
                serialized_players_list.append(serialized_player)

            TOURNOIS.update({"players": serialized_players_list}, where("name") == tournament_data.get("name"))
            TOURNOIS.update(
                {"players_round_id": tournament.players_round_id},
                where("players_round_id") == tournament_data.get("players_round_id"))

            self.view.display_selected_players(tournament.players)

    def check_data_tournaments_numbers(self) -> bool:
        """check if json are empty or not"""
        tournaments_number = 0
        for tournament in TOURNOIS:
            tournaments_number += 1

        if tournaments_number != 0:
            return False
        else:
            return True
