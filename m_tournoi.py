from data import TOURNOIS


class Tournoi:
    NOMBRE_JOUEUR = 8

    def __init__(self, name, place, date, tours, rounded, joueurs, time, description):

        self.name = name
        self.place = place
        self.date = date
        self.tours = tours
        self.rounded = rounded
        self.joueurs = joueurs
        self.time = time
        self.description = description

    def get_name(self):
        return self.name

    def get_place(self):
        return self.place

    def get_date(self):
        return self.date

    def get_tours(self):
        return self.tours

    def get_rounded(self):
        return self.rounded

    def get_joueurs(self):
        return self.joueurs

    def get_time(self):
        return self.time

    def get_description(self):
        return self.description

    def save(self):
        """Save the info in tournaments.json"""
        TOURNOIS.insert({
            "Name": self.name,
            "Place": self.place,
            "Date": self.date,
            "Description": self.description
        })

#
#     """Put the player's index into a list"""
#
#     @classmethod
#     def add_index_in_list(cls, liste_joueurs, liste_index_joueurs):
#         liste_index_joueurs.append(len(liste_joueurs))
#         print(liste_index_joueurs)
#
#     """To get back a player"""
#
#     @classmethod
#     def get_player(cls, liste_joueurs):
#         print(liste_joueurs[2])
#
#     """show the player's list"""
#
#     @classmethod
#     def get_list_player(cls, liste_joueurs):
#         print(liste_joueurs)
#
#     """Check if you have all your players"""
#
#     @classmethod
#     def validate_number_player(cls, liste_joueurs):
#         if len(liste_joueurs) == 8:
#             print("Vous avez tous vos joueurs, le tournoi peut démarrer")
#
#         else:
#             print("Vous n'avez pas ajouté 8 joueurs")
#
# """fait les paires"""


# def faire_match(cls, liste_joueurs):
#
#     print(f"Match 1 : {liste_joueurs[0]} contre {liste_joueurs[7]}")
#     print(f"Match 2 : {liste_joueurs[1]} contre {liste_joueurs[6]}")
#     print(f"Match 3 : {liste_joueurs[2]} contre {liste_joueurs[5]}")
#     print(f"Match 4 : {liste_joueurs[3]} contre {liste_joueurs[4]}")


# class Matchs:
#
#     def __init__(self):
#
#
# def main():
#     vue = Vue()
#     controller = Controller(vue=vue)
# class Round:
#
#     def __init__(self, name_round, date_heure_debut):
#         self.name_round = name_round
#         self.date_heure_debut = date_heure_debut
