
#-------------------------------------------------------------------------------
#                                  CLASS
#-------------------------------------------------------------------------------
class Etudiant():
    def __init__(self):
        self.numero = '' 
        self.nom = '' 
        self.prenom = '' 
        self.date_naissance = '' 
        self.email = '' 
        self.telephone = '' 
        self.filiere = '' 
        self.option = ''  
        date_created = ''

    def afficher(self):
        print(
            "numero :", self.numero,
                        "nom :", self.nom,"prenom :", self.prenom,"date de naissance :", self.date_naissance,"email :", self.email,
                        "numero de telephone :", self.telephone,"filiere :", self.filiere,"option :", self.option
        )

    def getEtudiantAsParams(self): 
        return (self.numero, 
            self.nom,
            self.prenom, 
            self.date_naissance, 
            self.email, 
            self.telephone, 
            self.filiere, 
            self.option,
            self.date_created)