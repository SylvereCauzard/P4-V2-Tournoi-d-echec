from data import PLAYERS


class ViewJoueurs:

    def ajout_joueur_family_name(self) -> str:
        family_name = input("Entrez le nom de famille du joueur : ")
        while len(family_name) <= 1:
            print("'family_name' must contains 2 character minimum !")
            family_name = input("Enter the family_name : ")
        return family_name

    def ajout_joueur_name(self) -> str:
        name = input("Entrez le prenom du joueur : ")
        while len(name) <= 1:
            print("'name' must contains 2 character minimum !")
            name = input("Enter the name : ")
        return name

    def ajout_joueur_birthday(self) -> str:
        birthday = input("Entrez la date de naissance du joueur sous le format XX/XX/XXXX : ")
        return birthday

    def ajout_joueur_sexe(self) -> str:
        sexe = input("Enter 'M' for man and 'W' for woman : ")
        check = True
        while check is True:
            if "M" in sexe or "W" in sexe:
                check = False
            else:
                print("Only accept 'M' for man, and 'W' for woman !")
                sexe = input("Enter 'M' for man and 'W' for woman : ")

        return sexe

    def ajout_joueur_classement(self) -> str:
        classement = input("Entrez le classement du joueur : ")
        return classement

    @staticmethod
    def show_players() -> None:
        """Show all players in players.json"""
        for player in PLAYERS:
            print(player)
