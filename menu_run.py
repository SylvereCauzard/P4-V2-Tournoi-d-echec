from v_menu import ViewMenu


def run_menu_selection(self):
    selection = ViewMenu()
    if selection == "1":
        self.creation_tournois()
    if selection == "2":
        self.liste_tournois()
    if selection == "3":
        self.add_new_player()
    if selection == "4":
        self.show_players()
    if selection == "5":
        quit()

    return run_menu_selection(ViewMenu)
