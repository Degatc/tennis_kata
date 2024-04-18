import os
import unittest

from tennis5 import TennisGame5

class GoldenMasterTest(unittest.TestCase):

    # Ajustez l'emplacement pour votre dossier local
    DIR = "../python/golden-master"

    # Utilisation de TennisGame5
    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name, language):
        game = TennisGame5(p1Name, p2Name, language)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, language, score_player_1, score_player_2):
        return os.path.join(self.DIR, f"{language}_{score_player_1}_{score_player_2}.txt")

    def test_record(self):
        languages = ["fr", "en"]
        for language in languages:
            for score_player_1 in range(5):
                for score_player_2 in range(5):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file_path = self.make_file_name(language, score_player_1, score_player_2)
                        with open(file_path, "w") as file:
                            file.writelines(sortie)

    def test_replay(self):
        languages = ["fr", "en"]
        for language in languages:
            for score_player_1 in range(5):
                for score_player_2 in range(5):
                    with self.subTest(f"{score_player_1}, {score_player_2}"):
                        sortie = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file_path = self.make_file_name(language, score_player_1, score_player_2)
                        with open(file_path, "r") as file:
                            attendu = file.read()
                        self.assertEqual(attendu, sortie)

