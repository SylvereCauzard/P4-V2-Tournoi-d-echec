# import v_menu
#
#
# class Input:
#
#     # Check len of menu and return selected menu
#     def select_menu_number(self, menu_len):
#         self.menu_len = menu_len
#         self.menu_number = 0
#         while self.menu_number < 1:
#             try:
#                 self.menu_number = int(input('Faire un choix : '))
#
#                 if self.menu_number < 1:
#                     v_menu.ViewMenu().short("err_choise")
#
#                 elif self.menu_number > int(self.menu_len):
#                     v_menu.ViewMenu().short("err_choise")
#                     self.menu_number = 0
#
#             except ValueError:
#                 v_menu.ViewMenu().short("err_choise")
#                 self.menu_number = 0
#         return self.menu_number
