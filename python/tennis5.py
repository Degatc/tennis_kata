# -*- coding: utf-8 -*-

class TennisGame5:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    # Utilisation de variables constantes plutôt que des chaînes de caractères
    # pour l'identification des joueurs
    def won_point(self, playerName):
        if (playerName == self.player1Name):
            self.player1Score += 1
        elif (playerName == self.player2Name):
            self.player2Score += 1
        else:
            raise ValueError("Invalid player name.")

    # On élimine la boucle while car elle n'est pas nécessaire
    # les scores ne dépassent jamais 4
    # Conditions plus simples pour déterminer les scores
    def score(self):
        player1Score = self.player1Score
        player2Score = self.player2Score

        if player1Score > 4 or player2Score > 4:
            player1Score = 4
            player2Score = 4

        # Utilisation de constantes pour les scores plutôt que des chaînes de caractères
        lookup = {
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
            # Utilisation de variables pour les conditions de victoire ou d'avantage
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

        entry = (player1Score, player2Score)
        if (entry in lookup):
            return lookup[entry]
        else:
            # Message explicite
            raise ValueError("Invalid score.")
