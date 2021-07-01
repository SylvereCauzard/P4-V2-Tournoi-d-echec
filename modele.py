class Tournoi:

    def __init__(self, **tournoi_attribute):
        tournoi_attribute = []
        self.nom = tournoi_attribute[nom]
        self.lieu = tournoi_attribute[lieu]
        self.date = tournoi_attribute[date]
        self.nb_tours = tournoi_attribute[nb_tours]
        self.tournees = tournoi_attribute[tournees]
        self.joueurs = tournoi_attribute[joueurs]
        self.time = tournoi_attribute[time]
        self.description = tournoi_attribute[description]





class Player:

    list_player = []

    def __init__(self, family_name, name, birth_date, sexe, classement):
        self.family_name = family_name
        self.name = name
        self.birth_date = birth_date
        self.sexe = sexe
        self.classement = classement
        Player.add_joueur(self)


    @classmethod
    def add_joueur(cls, joueur):
        cls.list_player.append(joueur)

    def data_base(self):



class Matchs:

    def __init__(self):


def main():
    vue = Vue()
    controller = Controller(vue=vue)
