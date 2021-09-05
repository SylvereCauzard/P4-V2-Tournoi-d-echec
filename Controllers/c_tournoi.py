from m_tournoi import Tournoi
from v_tournoi import ViewTournois


class ControllerTournois:

    @staticmethod
    def toirnoi_creation():

        vue = ViewTournois()
        name = vue.creation_tournois()
        lieu = vue.afficher_lieu()
        date = vue.afficher_date()
        tour = vue.afficher_tour()
        round = vue.afficher_liste_round()
        joueurs = vue.afficher_liste_joueurs()
        time = vue.afficher_time()
        description = vue.afficher_description()
        tournoi = Tournoi(name, lieu, date, tour, round, joueurs, time, description)
        tournoi.save()


run_control = ControllerTournois()
run_control.toirnoi_creation()

