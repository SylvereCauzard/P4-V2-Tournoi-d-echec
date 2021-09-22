import v_menu
from Controllers.c_tournoi import ControllerTournois
from Controllers.c_player import ControllerJoueur
from Vues.v_tournoi import ViewTournois
from Vues.v_player import ViewJoueurs


class MenuSelection:

    def __init__(self, view) -> None:
        self.view = view
        self.tournament_view = ViewTournois()
        self.player_view = ViewJoueurs()
        self.tournament_controller = ControllerTournois()
        self.player_controller = ControllerJoueur()

        self.run_main_menu = "Yes"
        self.run_report_menu = "Yes"

    def main_menu(self):

        v_menu.ViewMenu().main_menu()
        self.run_report_menu = "No"

        while self.run_main_menu == "Yes":
            # self.menu_number = input.Input().select_menu_number(5)
            choix = self.view.main_menu()
            # Call tournament's creation
            if choix == 1:
                self.tournament_controller.tournoi_creation()
            # Call list of all tournaments
            elif choix == 2:
                pass
            # Call Player's creation
            elif choix == 3:
                self.player_controller.add_new_player()
            # Call list of all Players
            elif choix == 4:
                pass
            # Quit the Apps
            elif choix == 5:
                self.run_report_menu = "No"
            elif choix == "":
                print("You must enter a number ! ")
