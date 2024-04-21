# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0  # Chaque joueur commence avec un score de 0

class TennisGame5:
    def __init__(self, player1_name, player2_name, language):
        self.player1 = Player(player1_name)  # Création d'une instance de Player
        self.player2 = Player(player2_name)  # Création d'une autre instance de Player
        self.language = language
        # Init traductions des scores pour les différentes langues
        self.lookup = self.initialize_lookup()

    def initialize_lookup(self):
        # Dictionnaire scores en anglais et en français
        return {
            'en': {
                (0, 0): "Love-All", (0, 1): "Love-Fifteen", (0, 2): "Love-Thirty", (0, 3): "Love-Forty",
                (1, 0): "Fifteen-Love", (1, 1): "Fifteen-All", (1, 2): "Fifteen-Thirty", (1, 3): "Fifteen-Forty",
                (2, 0): "Thirty-Love", (2, 1): "Thirty-Fifteen", (2, 2): "Thirty-All", (2, 3): "Thirty-Forty",
                (3, 0): "Forty-Love", (3, 1): "Forty-Fifteen", (3, 2): "Forty-Thirty", (3, 3): "Deuce",
                (4, 4): "Deuce"
            },
            'fr': {
                (0, 0): "Zéro-Partout", (0, 1): "Zéro-Quinze", (0, 2): "Zéro-Trente", (0, 3): "Zéro-Quarante",
                (1, 0): "Quinze-Zéro", (1, 1): "Quinze-Partout", (1, 2): "Quinze-Trente", (1, 3): "Quinze-Quarante",
                (2, 0): "Trente-Zéro", (2, 1): "Trente-Quinze", (2, 2): "Trente-Partout", (2, 3): "Trente-Quarante",
                (3, 0): "Quarante-Zéro", (3, 1): "Quarante-Quinze", (3, 2): "Quarante-Trente", (3, 3): "Égalité",
                (4, 4): "Égalité"
            }
        }

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        elif player_name == self.player2.name:
            self.player2.score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        score1 = self.player1.score
        score2 = self.player2.score

        if score1 >= 4 or score2 >= 4:
            diff = score1 - score2
            if diff == 0:
                return self.lookup[self.language][(4, 4)]
            elif diff == 1:
                return f"Advantage {self.player1.name}"
            elif diff == -1:
                return f"Advantage {self.player2.name}"
            elif diff >= 2:
                return f"Win for {self.player1.name}"
            else:
                return f"Win for {self.player2.name}"

        return self.lookup[self.language][(score1, score2)]

# Utilisation de la classe
game = TennisGame5("Alice", "Bob", "en")
game.won_point("Alice")
print(game.score())  # Affichera le score après qu'Alice a marqué un point
