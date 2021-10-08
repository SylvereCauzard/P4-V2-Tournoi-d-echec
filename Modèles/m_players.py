from data import PLAYERS
import json

import check_functions as check


class Player:

    def __init__(self, family_name, name, birthday, sexe, classement, faced_players, tournament_score=0):
        self.family_name = family_name
        self.name = name
        self.birthday = birthday
        self.sexe = sexe
        self.classement = classement
        self.faced_players = faced_players
        self.tournament_score = tournament_score

    def save(self):
        """Save the info of a player"""
        PLAYERS.insert({
            "Name": self.name,
            "family.name": self.family_name,
            "Birthday": self.birthday,
            "Sexe": self.sexe,
            "Classement": self.classement,
            "faced_players": self.faced_players
           })

    def serialize(self):
        """serialize a player"""
        serialized_player = json.dumps(self.__dict__)
        return serialized_player

    def update_general_ranking(self):
        """Update general ranking of a player after a tournament in players database"""
        pass

    @staticmethod
    def modify_player_ranking():
        """To modify manually the player ranking"""
        player_id = check.request_id(PLAYERS)
        print(str(player_id))
        player = Player.deserialize_player(Player, player_id)
        print(f"Le classement d'élo de {player.family_name} est {str(player.classement)}")
        print(f"Entre son nouvelle élo {player.family_name} : ")
        new_player_score = check.request_number()
        PLAYERS.update({"Classement": new_player_score}, doc_ids=[player_id])
        print(f"Le classement d'élo de {player.family_name} est maintenant de {str(new_player_score)}")

    @staticmethod
    def deserialize_player(cls, key: int) -> "Player":
        """deserialize one player and instantiate it"""
        player_data = PLAYERS.get(doc_id=key)
        player = cls(
            family_name=player_data.get("family_name"),
            name=player_data.get("name"),
            birthday=player_data.get("birthday"),
            sexe=player_data.get("sexe"),
            classement=player_data.get("classement"),
            faced_players=player_data.get("faced_players")
        )
        return player

    @staticmethod
    def deserialize_player_for_next_round(cls, player_dict) -> "Player":
        """deserialize one player and instantiate it"""
        player = cls(
            family_name=player_dict.get("first_name"),
            name=player_dict.get("last_name"),
            birthday=player_dict.get("birthday"),
            sexe=player_dict.get("genre"),
            classement=player_dict.get("ranking"),
        )
        player.faced_players = player_dict.get("faced_players")
        return player

    def __repr__(self):
        """redifining repr method for print cleaned data"""
        return f"{self.family_name} {self.name} | {self.birthday} | {self.sexe} | {self.classement}"
