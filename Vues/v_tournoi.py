from data import TOURNOIS


class ViewTournois:

    def creation_tournois(self):
        name = input("Entrez le nom du tournois : ")
        return name

    def afficher_lieu(self):
        lieu = input("Renseignez le lieu du tournois : ")
        return lieu

    def afficher_date(self):
        date = input("Renseignez la date du tournois : ")
        return date

    def afficher_tour(self):
        tour = input("Renseignez le nombre de tours : ")
        return int(tour)

    def afficher_liste_round(self):
        pass

    def afficher_liste_joueurs(self):
        pass

    def afficher_time(self):
        time = 10
        return time

    def afficher_description(self):
        description = input("Veuillez inscrire vos remarques ici : ")
        return description

    def liste_tournois(self) -> None:
        for tournoi in TOURNOIS:
            print(tournoi)
