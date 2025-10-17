from pathlib import Path

liste = {".png" : "Images",
       ".jpeg" : "Images",
       ".jpg" : "Images",
       ".gif" : "Images",
       ".mp3" : "Musiques",
       ".wav" : "Musiques",
       ".flac": "Musiques",
       ".mp4" : "Videos",
       ".mov" : "Videos",
       ".avi" : "Videos",
       ".zip" : "Archives",
       ".pdf" : "Documents",
       ".txt" : "Documents",
       ".json" : "Documents",
       ".xls" : "Documents" ,
       ".ppt" : "Documents",
       ".pages" : "Documents",
       ".odp" : "Documents",
       }

liste_tri = Path.home() / "Downloads"
liste_tri.mkdir(exist_ok=True)

files = [f for f in liste_tri.iterdir() if f.is_file()]

for f in files:
       output_dir = liste_tri / liste.get(f.suffix,"Autres")
       output_dir.mkdir(exist_ok = True)
       f.rename(output_dir / f.name)