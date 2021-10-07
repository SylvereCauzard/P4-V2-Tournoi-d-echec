from Modèles.m_round import Round
from Modèles.m_players import Player
from Modèles.m_tournoi import Tournoi

from typing import Union
from data import TOURNOIS

import check_functions as check


class RoundController:
    """Round controller"""
    def __init__(self, view) -> None:
        self.view = view

    def get_score_input(self, player_a: Player, player_b: Player):
        """get user entry for a tour between two players"""
        result = self.view.request_specific_number_only(player_a, player_b)
        player_a.faced_players.append(player_b.family_name)
        player_b.faced_players.append(player_a.family_name)
        if result == 1:
            player_a.tournament_score += 1
            player_b.tournament_score += 0
            player_a_result = 1
            player_b_result = 0
        elif result == 0.5:
            player_a.tournament_score += 0.5
            player_b.tournament_score += 0.5
            player_a_result = 0.5
            player_b_result = 0.5
        elif result == 0:
            player_a.tournament_score += 0
            player_b.tournament_score += 1
            player_a_result = 0
            player_b_result = 1

        tuple_result = ((
            str(player_a.family_name) + " " + str(player_a_result) + " " + " | " +
            str(player_b.family_name) + " " + str(player_b_result)
            ))
        return tuple_result

    def run_rounds(self) -> Union[list[list[tuple]], Round]:
        """run rounds 1 to 4 and return result list and the round instance"""
        tournament_id = self.view.request_id(TOURNOIS)
        round = Round(tournament_id)
        tournament = Tournoi.deserialize_tournament(Tournoi, tournament_id)
        if tournament.get_actual_round() == 1:
            tuple_results = []

            start_time = self.view.display_rounds_message("1", "start")
            pairing_players = round.premier_match()
            for pair in pairing_players:
                tuple_result = self.get_score_input(pair[0], pair[1])
                tuple_results.append(tuple_result)
            players_list = [item for sublist in pairing_players for item in sublist]
            tournament.save_players_for_next_round(players_list, tournament_id)
            end_time = self.view.display_rounds_message("1", "end")
            tuple_results.append((start_time, end_time))

            tournament.current_round += 1
            tournament.save_actual_round(tournament_id)
            round.update_rounds_score(tuple_results, "round_1")
            self.view.display_continue_to_next_round()
            response_for_next_round = check.request_selection_with_number("Yes", "No", "None")
            if response_for_next_round == "Yes":
                pass
            else:
                # STOP METHODE
                return
