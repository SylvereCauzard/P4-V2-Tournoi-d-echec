from tinydb import TinyDB

TOURNOIS_DATA = TinyDB("tournaments.json")
TOURNOIS = TOURNOIS_DATA.table("Tournaments")
PLAYERS_DATA = TinyDB("players.json")
PLAYERS = PLAYERS_DATA.table("Players")

NOMBRE_JOUEUR = 8
