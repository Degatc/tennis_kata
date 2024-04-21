import os
import unittest

from tennis5 import TennisGame5

class GoldenMasterTest(unittest.TestCase):

    # Répertoire pour stocker les résultats des tests
    DIR = "../python/golden-master"
    os.makedirs(DIR, exist_ok=True)  # Assurez-vous que le répertoire existe

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
        """Enregistre les résultats des scores dans des fichiers pour chaque combinaison de scores."""
        languages = ["fr", "en"]
        for language in languages:
            for score_player_1 in range(5):
                for score_player_2 in range(5):
                    with self.subTest(f"{language}: {score_player_1}, {score_player_2}"):
                        score = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file_path = self.make_file_name(language, score_player_1, score_player_2)
                        with open(file_path, "w") as file:
                            file.write(score)

    def test_replay(self):
        """Vérifie les résultats des scores contre les fichiers enregistrés."""
        languages = ["fr", "en"]
        for language in languages:
            for score_player_1 in range(5):
                for score_player_2 in range(5):
                    with self.subTest(f"{language}: {score_player_1}, {score_player_2}"):
                        expected_score = self.play_game(score_player_1, score_player_2, "player1", "player2", language)
                        file_path = self.make_file_name(language, score_player_1, score_player_2)
                        with open(file_path, "r") as file:
                            recorded_score = file.read().strip()
                        self.assertEqual(recorded_score, expected_score)

if __name__ == "__main__":
    unittest.main()

