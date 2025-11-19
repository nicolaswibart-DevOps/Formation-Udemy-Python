
class Voiture:
    
    def __init__(self, essence = 100):
        self.essence = essence


    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d’essence")
    
    def roule(self, km):
        self.km = km

        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return
        
        conso = (km * 5) / 100
        self.essence -= conso
        
        if self.essence < 10 :
            print("Vous n'avez bientôt plus d'essence !")
            
        else:
            print(f"La voiture contient {self.essence} litres d’essence")

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")
