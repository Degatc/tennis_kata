Utilisation de variables constantes pour l'identification des joueurs :

Les chaînes de caractères "player1" et "player2" ont été remplacées par les attributs de classe self.player1Name et self.player2Name. ça rend le code plus lisible et réduit les risques d'erreurs de frappe.

Suppression de la boucle while inutile :

La boucle while qui ajustait les scores au-dessus de 4 a été supprimée car les scores ne peuvent jamais dépasser 4 dans le jeu de tennis. Cela simplifie le code et le rend plus efficace.

Simplification des conditions pour déterminer les scores :

Les conditions pour savoir les scores ont été simplifiées, car la boucle while a été supprimée. Maintenant, les scores sont simplement ajustés s'ils dépassent 4.

Utilisation de constantes pour les scores :

Les scores associés à des chaînes de caractères ont été remplacés par des constantes. Par exemple, "Love-All" devient "Love-All", etc. Cela rend le code plus modulaire et évite la répétition.
Utilisation de variables pour les conditions de victoire ou d'avantage :

Les conditions de victoire ou d'avantage ont été remplacées par des variables. Par exemple, au lieu de "Win for player1", on a maintenant "Win for " + self.player1Name. Cela rend le code plus générique et adaptable à différents joueurs.

Pour le projet en générale le code brut, le prototype, à été segmenter en classe qui interagissent entre elle afin de facilité les interaction et la maintenabilité.

En résumé, ces modifications améliorent la lisibilité, la modularité et l'efficacité du code, tout en réduisant les risques d'erreurs et en le rendant plus flexible.