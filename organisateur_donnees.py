"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""
import re
from pathlib import Path

chemin = Path.home() / "Desktop" / "Formation Python" / "prenoms.txt"

# Lire le fichier texte
with open (chemin , "r" ) as fichier_existant:
    contenu = fichier_existant.read()
    contenu_morceaux = re.split(r"[,.\s]+", contenu)
# Cleaner les données
    contenu_clean = [p.strip().replace(".", "").replace(" ", "") for p in contenu_morceaux if p.strip()]
    contenu_clean = sorted(set(contenu_clean), key=str.casefold)


# Créer un nouveau fichier texte
clean_fichier = Path.home() / "Desktop" / "Formation Python" / "clean_prenoms.txt"


# Rajouter les nouveaux éléments triés dans le nouveau fichier
with open (clean_fichier , "w") as prenom_final:
    for prenom in contenu_clean:
        prenom_final.write(prenom + "\n")
        print(clean_fichier)
