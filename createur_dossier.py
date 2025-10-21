from pathlib import Path

# 📁 Chemin de base : Bureau / Formation Python
chemin = Path.home() / "Desktop" / "Formation Python"

# 🗂️ Dictionnaire avec les dossiers et sous-dossiers à créer
structure = {
    "Films": [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forrest Gump",
    ],
    "Employes": [
        "Paul",
        "Pierre",
        "Marie",
    ],
    "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles",
    ],
}

# 🏗️ Création du dossier racine (Formation Python) s'il n'existe pas
chemin.mkdir(parents=True, exist_ok=True)

# 🔁 Boucle sur chaque dossier et sous-dossier
for dossier_principal, sous_dossiers in structure.items():
    dossier_path = chemin / dossier_principal
    dossier_path.mkdir(parents=True, exist_ok=True)  # Crée le dossier principal

    for sous_dossier in sous_dossiers:
        sous_path = dossier_path / sous_dossier
        sous_path.mkdir(parents=True, exist_ok=True)  # Crée le sous-dossier

        print(f"✅ Créé : {sous_path}")


