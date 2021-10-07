from Vues.v_menu import ViewMenu
from Controllers.c_menu import MenuSelection


view = ViewMenu()
app = MenuSelection(view)
app.run_main_menu_selection()
