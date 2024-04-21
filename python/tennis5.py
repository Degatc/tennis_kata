import json

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0  # Chaque joueur commence avec un score de 0

class TennisGame5:
    def __init__(self, player1_name, player2_name, language):
        self.player1 = Player(player1_name)  # Création d'une instance de Player
        self.player2 = Player(player2_name)  # Création d'une autre instance de Player
        self.language = language
        self.load_translations()

    def load_translations(self):
        with open('translations.json', 'r') as file:
            self.translations = json.load(file)

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
        score_tuple = f"({player1Score}, {player2Score})"

        if self.language == 'en':
            lookup = self.translations['english']
        elif self.language == 'fr':
            lookup = self.translations['french']
        else:
            raise ValueError("Language not supported.")

        # Ajout du nom du joueur dynamiquement pour ne pas le stocker dans le fichier JSON de traduction
        if score_tuple in lookup:
            result = lookup[score_tuple]
            if "Win for" in result or "Victoire pour" in result:
                if player1Score > player2Score:
                    result += " " + self.player1.name
                else:
                    result += " " + self.player2.name
            elif "Advantage" in result or "Avantage" in result:
                if player1Score > player2Score:
                    result += " " + self.player1.name
                else:
                    result += " " + self.player2.name
            return result
        else:
            raise ValueError("Invalid score.")

