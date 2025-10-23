
#chemin = /Users/nicolaswibart/Desktop/Formation Python/readme.txt
fichier = input("Entrer un fichier à ouvrir: ")

try:
    with open (fichier, "r") as fichier_existant:
        contenu = fichier_existant.read()
        print(contenu)

except FileNotFoundError:
    print("Impossible, le fichier n'existe pas")

except UnicodeDecodeError:
    print("Impossible, le fichier est invalide")

finally:
    print("fermeture du fichier")