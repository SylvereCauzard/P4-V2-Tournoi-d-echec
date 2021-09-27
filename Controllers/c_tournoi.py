from Modèles.m_tournoi import Tournoi
from Controllers.c_player import ControllerJoueur
from Vues.v_player import ViewJoueurs

from data import TOURNOIS
from typing import Union
import json
from tinydb import where


class ControllerTournois:

    def __init__(self, view) -> None:
        self.view = view
        self.player_controller = ControllerJoueur(ViewJoueurs)

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.view.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournoi(name, place, date, time, description)
        tournament.save()
        print("\n The tournament named '{}' has been saved !".format(name))

    def instantiate_tournament(self) -> Union[Tournoi, int]:
        """instantiate tournament saved in tournaments.json"""
        self.view.show_tournaments()
        tournament_id = self.view.request_id(TOURNOIS)
        tournament_data = TOURNOIS.get(doc_id=tournament_id)
        tournament = Tournoi(
            name=tournament_data.get("name"),
            place=tournament_data.get("place"),
            date=tournament_data.get("date"),
            time=tournament_data.get("time"),
            description=tournament_data.get("description")
        )
        return tournament, tournament_id

    def add_tournament_players(self):
        """Add 8 players to a selected tournament"""
        tournament, tournament_id = self.instantiate_tournament()
        # player
        tournament.players = self.player_controller.instantiates_players()
        tournament_data = TOURNOIS.get(doc_id=tournament_id)
        serialized_players_list = []

        for player in tournament.players.values():
            serialized_player = json.dumps(player.__dict__)
            serialized_players_list.append(serialized_player)

        TOURNOIS.update({"players": serialized_players_list}, where("name") == tournament_data.get("name"))
        print("Selected players have been added to the tournament")

