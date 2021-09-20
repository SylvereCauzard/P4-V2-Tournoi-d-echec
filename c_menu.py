from Vues.v_menu import ViewMenu


class RunMenuSelection:

    def main_menu(self):

        menu.ViewMenu().main_menu()
        self.menu_number = input.Input().select_menu_number(3)

        # Call player menu
        if self.menu_number == 1:
            Controller().players_menu()

        # Call tournaments menu
        elif self.menu_number == 2:
            Controller().tournaments_menu()

        # Close app
        elif self.menu_number == 3:
            pass
