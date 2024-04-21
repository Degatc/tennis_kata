# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0  # Chaque joueur commence avec un score de 0

class TennisGame5:
    def __init__(self, player1_name, player2_name, language):
        self.player1 = Player(player1_name)  # Création d'une instance de Player
        self.player2 = Player(player2_name)  # Création d'une autre instance de Player
        # Dictionnaire scores en anglais et en français
        self.language = language
        self.lookup_english = {
            (0, 0): "Love-All",
            (0, 1): "Love-Fifteen",
            (0, 2): "Love-Thirty",
            (0, 3): "Love-Forty",
            (1, 0): "Fifteen-Love",
            (1, 1): "Fifteen-All",
            (1, 2): "Fifteen-Thirty",
            (1, 3): "Fifteen-Forty",
            (2, 0): "Thirty-Love",
            (2, 1): "Thirty-Fifteen",
            (2, 2): "Thirty-All",
            (2, 3): "Thirty-Forty",
            (3, 0): "Forty-Love",
            (3, 1): "Forty-Fifteen",
            (3, 2): "Forty-Thirty",
            (3, 3): "Deuce",
            (4, 0): "Win for " + self.player1.name,
            (4, 1): "Win for " + self.player1.name,
            (4, 2): "Win for " + self.player1.name,
            (4, 3): "Advantage " + self.player1.name,
            (0, 4): "Win for " + self.player2.name,
            (1, 4): "Win for " + self.player2.name,
            (2, 4): "Win for " + self.player2.name,
            (3, 4): "Advantage " + self.player2.name,
            (4, 4): "Deuce",
        }
        self.lookup_french = {
            (0, 0): "Zero-Partout",
            (0, 1): "Zero-Quinze",
            (0, 2): "Zero-Trente",
            (0, 3): "Zero-Quarante",
            (1, 0): "Quinze-Zero",
            (1, 1): "Quinze-Partout",
            (1, 2): "Quinze-Trente",
            (1, 3): "Quinze-Quarante",
            (2, 0): "Trente-Zero",
            (2, 1): "Trente-Quinze",
            (2, 2): "Trente-Partout",
            (2, 3): "Trente-Quarante",
            (3, 0): "Quarante-Zero",
            (3, 1): "Quarante-Quinze",
            (3, 2): "Quarante-Trente",
            (3, 3): "Egalite",
            (4, 0): "Victoire pour " + self.player1.name,
            (4, 1): "Victoire pour " + self.player1.name,
            (4, 2): "Victoire pour " + self.player1.name,
            (4, 3): "Avantage " + self.player1.name,
            (0, 4): "Victoire pour " + self.player2.name,
            (1, 4): "Victoire pour " + self.player2.name,
            (2, 4): "Victoire pour " + self.player2.name,
            (3, 4): "Avantage " + self.player2.name,
            (4, 4): "Egalite",
        }

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        elif player_name == self.player2.name:
            self.player2.score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        player1Score = self.player1.score
        player2Score = self.player2.score

        if player1Score > 4 or player2Score > 4:
            player1Score = 4
            player2Score = 4

        if self.language == 'en':
            lookup = self.lookup_english
        elif self.language == 'fr':
            lookup = self.lookup_french
        else:
            raise ValueError("Language not supported.")

        entry = (player1Score, player2Score)
        if entry in lookup:
            return lookup[entry]
        else:
            raise ValueError("Invalid score.")

