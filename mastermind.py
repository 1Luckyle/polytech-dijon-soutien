import os
import random

# PARAMETRES :
# Il suffit d'ajouter une lettre associé à une couleur sous le formant "LETTRE": "Nom_de_la_couleur"
COLORS = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "Y": "Yellow",
    "P": "Purple",
    "W": "White",
}
LENGTH = 4  # nombre d'éléments dans le code secret
NB_TRY = 12  # nombre maximal de tentatives pour la résolution du code secret
# Fichiers de statistiques
FILE_GAME = os.path.dirname(os.path.abspath(__file__))
FILE_PARTY = os.path.join(FILE_GAME, ".mastermind_parties")
FILE_SCORE = os.path.join(FILE_GAME, ".mastermind_score")


def random_code():
    code = []
    # Ici on crée la liste des lettres pour le code secret, liste associé aux couleurs disponibles définies dans COLORS
    lettres = list(COLORS)
    for i in range(LENGTH):
        code.append(random.choice(lettres))
    return code

def verif_essai(essai, code_secret):
    correct = 0
    partiel = 0
    # copies pour ne pas compter deux fois la même couleur
    reste_essai = list(essai)
    reste_secret = list(code_secret)

    # vérifie les bonnes couleurs au bon emplacement
    for i in range(LENGTH):
        if reste_essai[i] == reste_secret[i]:
            correct = correct + 1
            reste_essai[i] = None
            reste_secret[i] = None

    # vérifie les bonnes couleurs au mauvais emplacement
    for couleur in reste_essai:
        if couleur is not None and couleur in reste_secret:
            partiel = partiel + 1
            reste_secret[reste_secret.index(couleur)] = None
    
    return correct, partiel

def read_file_stat(chemin):
    if not os.path.exists(chemin):
        print(f"Fichier de statistiques {chemin} non trouvé.")
        return 0
    with open(chemin) as file:
        contenu = file.read().strip()
    return int(contenu) if contenu else 0

def read_stats():
    nb_parties = read_file_stat(FILE_PARTY)
    score_total = read_file_stat(FILE_SCORE)
    return nb_parties, score_total

def write_stats(nb_parties, score_total):
    with open(FILE_PARTY, "w") as file:
        file.write(str(nb_parties))
    with open(FILE_SCORE, "w") as file:
        file.write(str(score_total))

def save_game(score):
    nb_parties, score_total = read_stats()
    nb_parties = nb_parties + 1
    score_total = score_total + score
    write_stats(nb_parties, score_total)

def display_stats():
    nb_parties, score_total = read_stats()
    print(f"Statistiques : {nb_parties} partie jouée, score total : {score_total}")

def reset_stats():
    write_stats(0, 0)

def input_essai():
    while True:
        saisie = input("Votre code : ").strip().upper()
        if len(saisie) == LENGTH and all(c in COLORS for c in saisie):
            return list(saisie)
        print(f"Saisie invalide, entrez {LENGTH} lettres parmi {', '.join(COLORS)}.")

def game():
    print("Couleurs disponibles :", ", ".join(COLORS))
    code_secret = random_code()
    print(f"{code_secret} (Debug: code secret généré, à supprimer en production)")

    for essai_numero in range(1, NB_TRY + 1):
        essai = input_essai()
        correct, partiel = verif_essai(essai, code_secret)
        print(f"Correct : {correct} | Partiel : {partiel}")
        if correct == LENGTH:
            score = NB_TRY - essai_numero
            print(f"Bravo, code trouvé en {essai_numero} essais ! Score : {score}")
            return score

    print(f"Perdu ! Le code secret était : {''.join(code_secret)}")
    return 0

def menu(options):
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    while True:
        choix = input("Choix : ")
        if choix.isdigit():
            choix = int(choix)
            if choix >= 1 and choix <= len(options):
                return choix
        print("Choix invalide.")

def main():
    display_stats()
    option_jouer = "Jouer"

    while True:
        choix = menu([option_jouer, "Remettre à zéro les statistiques", "Quitter"])
        if choix == 1:
            score = game()
            save_game(score)
            display_stats()
            option_jouer = "Rejouer"
        elif choix == 2:
            reset_stats()
            print("Statistiques remises à zéro.")
            display_stats()
        else:
            print("Fin du jeu.")
            break

if __name__ == "__main__":
    main()