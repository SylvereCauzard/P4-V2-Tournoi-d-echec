
class ViewMenu:

    def __init__(self):
        pass

    def main_menu(self) -> str:
        print('\n')
        print('-=[ MENU PRINCIPAL ]=-')
        print("\n\
1 ● Créer un tournoi.\n\
2 ● Tournois enregistrés.\n\
3 ● Ajouter un nouveau joueur.\n\
4 ● Joueurs enregistrés.\n\
5 ● Quitter l'application.\n")
        response = input("Choississez un chiffre pour naviguer dans le menu : ")
        return response
