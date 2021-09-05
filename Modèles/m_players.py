from data import PLAYERS


class Player:

    liste_player = []

    def __init__(self, family_name, name, birthday, sexe, classement):
        self.family_name = family_name
        self.name = name
        self.birthday = birthday
        self.sexe = sexe
        self.classement = classement

        # Player.add_joueur(self)

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
