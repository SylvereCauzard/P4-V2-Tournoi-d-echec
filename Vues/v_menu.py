from data import TOURNOIS


class ViewMenu:

    def __init__(self):
        pass

    def main_menu(self) -> str:
        """Main menu of the program"""
        print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                               MENU PRINCIPALE                   ")
        print(
            "\n"
            "                ● 1 -          Créer un tournoi              ●\n"
            "                ● 2 -   Ajouter des joueurs à un tournoi     ●\n"
            "                ● 3 -    Débuté ou continué un tournoi       ●\n"
            "                ● 4 -     Ajouter un nouveau joueur          ●\n"
            "                ● 5 -    Modifier classement d'un joueur     ●\n"
            "                ● 6 -          Menu Secondaire               ●\n"
            "                ● 7 -       Quitter l'application            ●  "

        )
        print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        response = input("Choississez un chiffre pour naviguer dans le menu : ")
        return response

    def menu_secondaire(self) -> str:
        """report menu of the program"""
        print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                           MENU SECONDAIRE                       ")
        print(
            "\n"
            "       ● 1 -          Liste de tous les tournois             ●\n"
            "       ● 2 -           Liste de tous les joueurs             ●\n"
            "       ● 3 -      Les joueurs d'un tournoi particulier       ●\n"
            "       ● 4 -  Résultats des rounds d'un tournoi particulier  ●\n"
            "       ● 5 -             Retour au menu pricnipale           ●  "
        )
        print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        response = input("Choississez un chiffre pour naviguer dans le menu : ")
        return response

    def resultat_rounds(self, tournament_id) -> str:
        """round report menu of the programm"""
        tournament_data = TOURNOIS.get(doc_id=tournament_id)
        tournament_name = tournament_data.get("name")

        print(" ________________________________________________________________")
        print("                          RESULTATS DES ROUNDS                 \n")
        print(
            "               ========================================       \n"
            "                TOURNOI SELECTIONNE : " + tournament_name + " \n"
            "               ========================================       \n"
            "\n              ● 1 -     Résultats de tous les rounds     ●\n"
            "                ● 2 -      Résultat round numéro 1         ●\n"
            "                ● 3 -      Résultat round numéro 2         ●\n"
            "                ● 4 -      Résultat round numéro 3         ●\n"
            "                ● 5 -      Résultat round numéro 4         ●\n"
            "                ● 6 -     Retour au menu secondaire        ●"
        )
        print(" ________________________________________________________________")
        response = input("Choississez un chiffre : ")
        return response
