from data import PLAYERS


class Player:

    liste_player = []

    def __init__(self, family_name, name, birthday, sexe, classement, faced_players=[], tournament_score=0):
        self.family_name = family_name
        self.name = name
        self.birthday = birthday
        self.sexe = sexe
        self.classement = classement
        self.faced_players = faced_players
        self.tournament_score = tournament_score

    @classmethod
    def add_joueur(cls, joueur):
        cls.liste_player.append(joueur)

    def save(self):
        """Save the info of a player"""
        PLAYERS.insert({
            "Name": self.name,
            "family.name": self.family_name,
            "Birthday": self.birthday,
            "Sexe": self.sexe,
            "Classement": self.classement
           })

    def add_faced_player(self, player) -> None:
        """Save a faced player in a list"""
        self.faced_players.append(player)

    def __repr__(self):
        """redifining repr method for print cleaned data"""
        return f"{self.family_name} {self.name} | {self.birthday} | {self.sexe} | {self.classement}"
