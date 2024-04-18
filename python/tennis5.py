# -*- coding: utf-8 -*-

class TennisGame5:
    def __init__(self, player1Name, player2Name, language):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0
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
            (4, 0): "Win for " + self.player1Name,
            (4, 1): "Win for " + self.player1Name,
            (4, 2): "Win for " + self.player1Name,
            (4, 3): "Advantage " + self.player1Name,
            (0, 4): "Win for " + self.player2Name,
            (1, 4): "Win for " + self.player2Name,
            (2, 4): "Win for " + self.player2Name,
            (3, 4): "Advantage " + self.player2Name,
            (4, 4): "Deuce",
        }
        self.lookup_french = {
            (0, 0): "Zéro-Partout",
            (0, 1): "Zéro-Quinze",
            (0, 2): "Zéro-Trente",
            (0, 3): "Zéro-Quarante",
            (1, 0): "Quinze-Zéro",
            (1, 1): "Quinze-Partout",
            (1, 2): "Quinze-Trente",
            (1, 3): "Quinze-Quarante",
            (2, 0): "Trente-Zéro",
            (2, 1): "Trente-Quinze",
            (2, 2): "Trente-Partout",
            (2, 3): "Trente-Quarante",
            (3, 0): "Quarante-Zéro",
            (3, 1): "Quarante-Quinze",
            (3, 2): "Quarante-Trente",
            (3, 3): "Égalité",
            (4, 0): "Victoire pour " + self.player1Name,
            (4, 1): "Victoire pour " + self.player1Name,
            (4, 2): "Victoire pour " + self.player1Name,
            (4, 3): "Avantage " + self.player1Name,
            (0, 4): "Victoire pour " + self.player2Name,
            (1, 4): "Victoire pour " + self.player2Name,
            (2, 4): "Victoire pour " + self.player2Name,
            (3, 4): "Avantage " + self.player2Name,
            (4, 4): "Égalité",
        }

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Score += 1
        elif playerName == self.player2Name:
            self.player2Score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        player1Score = self.player1Score
        player2Score = self.player2Score

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
