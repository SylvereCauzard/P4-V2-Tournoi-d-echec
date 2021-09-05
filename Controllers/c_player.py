from m_players import Player
from v_player import ViewJoueurs


class ControllerJoueur:

    @staticmethod
    def add_new_player() -> None:

        vue = ViewJoueurs()
        family_name = vue.ajout_joueur_family_name()
        name = vue.ajout_joueur_name()
        birthday = vue.ajout_joueur_birthday()
        sexe = vue.ajout_joueur_sexe()
        classement = vue.ajout_joueur_classement()
        player = Player(family_name, name, birthday, sexe, classement)
        player.save()


run_player = ControllerJoueur()
run_player.add_new_player()
