from Modèles.m_players import Player

from data import PLAYERS


class ControllerJoueur:

    def __init__(self, view) -> None:
        self.view = view

    def get_info_player(self) -> None:
        """Get the user entry info and create a player"""

        family_name, name, birthday, sexe, classement = self.view.ask_info_player()
        player = Player(family_name, name, birthday, sexe, classement)
        player.save()

    def instantiates_players(self) -> dict:
        """instantiates 8 players selected by the user in a dict"""

        players_list = self.view.create_players_id_dict()
        for key in players_list:
            player_data = PLAYERS.get(doc_id=players_list.get(key))
            players_list[key] = Player(
                family_name=player_data.get("family_name"),
                name=player_data.get("name"),
                birthday=player_data.get("birthday"),
                sexe=player_data.get("sexe"),
                classement=player_data.get("classement"),
            )
        return players_list
