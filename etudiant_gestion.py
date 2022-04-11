from traitementbd import *
from etudiant import Etudiant

#-------------------------------------------------------------------------------
#                                 FONCTIONS
#-------------------------------------------------------------------------------
def ajouter_etudiant():
  nouveauEtudiant = Etudiant()
  nouveauEtudiant.numero = generer_numero_etudiant()

  nouveauEtudiant.nom = input("donnez le nom de l'etudiant : " )
  print()
  nouveauEtudiant.prenom = input("donnez le prenom de l'etudiant : ")
  print()
  nouveauEtudiant.date_naissance = input(" qu'elle est la date de naissance de l'etudiant exemple(AAAA-MM-JJ): ")
  print()
  nouveauEtudiant.email = input("donnez l'email de l'etudiant : ")
  print()
  nouveauEtudiant.telephone = input("donnez le numero de telephone de l'etudiant : ")
  print()
  nouveauEtudiant.filiere = input("a qu'elle filiere appartient l'etudiant : ")
  print()
  nouveauEtudiant.option = input("dans qu'elle option : ")
  print()

  sauvegarder_etudiant(nouveauEtudiant)

  print("l'etudiant est ajouter avec succes et ses cordonnes sont:")
  nouveauEtudiant.afficher()


def modifier_etudiant():
  numero = int(input("donnez le numero de l'etudiant que voulez modifier : "))

  while not in_db(numero):
    numero = int(input("le numero que vous avez saisie n'est pas valide. ressayer : "))

  choix = int(input(""" quelle cordonner voulez modifier ? 
                  1:nom
                  2:prenom
                  3:dete de naissance
                  4:email
                  5:numero de telephone
                  6: filiere
                  7:option """))

  valeur = ''
  colonne = ''
  
  if choix == 1:
    valeur = input("donnez le nouveaux nom : ")
    colonne = 'nom'

  elif choix == 2:
    valeur = input("donnez le nouveaux prenom : ")
    colonne = 'prenom'

  elif choix == 3:
    valeur = input("donnez la nouvelle date de naissance : ")
    colonne = 'date_naissance'
    
  elif choix == 4:
    valeur = input("donnez le nouveaux email : ")
    colonne = 'email'
  
  elif choix == 5:
    valeur = input("donnez le nouveaux numero de telephone : ")
    colonne = 'telephone'
    
  elif choix == 6:
    valeur = input("donnez la nouvelle filiere : ")
    colonne = 'filiere'
    
  elif choix == 7:
    valeur = input("donnez la nouvelle option : ")
    colonne = 'option'

  else:
    print("choix invalide")
    return

  modifier_etudiant_db(colonne, valeur, numero)


def suprimer_etudiant():
  numero = int(input("donnez le numero de l'etudiant que vous voulez suprimer : "))

  while not in_db(numero):
    numero = int(input("le numero que vous avez saisie n'est pas valide. resseyer :"))
    
  supprimer_etudiant_db(numero)

  print('Etudiant est supprimé')


def afficher_etudiant():
  numero = int(input("donnez le numero de l'etudiant que vous voulez afficher : "))

  while not in_db(numero):
    numero = int(input("le numero que vous avez saisie n'est pas valide. resseyer :"))

  etudiant = trouver_etudiant(numero)

  etudiant.afficher()


def afficher_liste_etudiants():
  choix = int(input(""" 
                  1: afficher les etudiant par filiere
                  2: afficher les etudiant par option
                  3: afficher les etudiant par date de creation
                  Entrez votre choix : """))

  if choix == 1:
    print("""par quelle filiere voulez vous afficher les etudiant ?
                     """)

    list_filiere = get_filiere()
    valeur_selectionnee = afficher_menu(list_filiere)

    afficher_etudiant_par('filiere', valeur_selectionnee)
  
  elif choix == 2:
    print("""par quelle option voulez vous afficher les etudiant ?
                     """)

    list_option = get_option()
    valeur_selectionnee = afficher_menu(list_option)

    afficher_etudiant_par('option', valeur_selectionnee)
  
  elif choix == 3 :
    afficher_liste_etudiants_par_date()


def afficher_liste_etudiants_par_date():
  choix = int(input("""
             1 : afficher les etudiant inscrit dans cette date 
             2 : afficher les etudiant inscrit avant cette date 
             3 : afficher les etudiant inscrit apres cette date 
                entrz votre choix :     """))

  msg_date = "entez la date exepmle:(AAAA-MM-JJ) : "
  date = ''
  comparaison = ''
  
  if choix == 1:
    date = input(msg_date)
    comparaison = '='

  elif choix == 2:
    date = input(msg_date)
    comparaison = '<='

  elif choix == 3:
    date = input(msg_date)
    comparaison = '>='
  
  else:
    print("choix invalide")
    return

  afficher_etudiant_par_date(comparaison, date)


def afficher_menu(list_choix):
  for i in range(len(list_choix)):
    print(f"{i + 1} : {list_choix[i]}")
  
  choix = int(input("entrz votre choix :"))

  return list_choix[choix - 1]