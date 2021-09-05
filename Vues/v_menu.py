
class ViewMenu:

    def menu_principal(self):

        print(
            "Pour Créer un tournoi - tapper 1 \n"
            "Pour voir tous les tournois enregistrés - tapper 2 \n"
            "Pour ajouter un nouveau joueur - tapper 3 \n"
            "Pour voir tous les joueurs enregistrés - tapper 4 \n"
            "Pour quitter le menu - tapper 5")

        response = input("Quel numéro voulez-vous choisir?")
        return response


