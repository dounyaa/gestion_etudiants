from etudiant_gestion import *
import os

def afficher_menu():
  is_closed = False

  while not is_closed:
    os.system('cls')
    print("---------------BIENVENUE AU MENU ELITECH-----------------")
    print()

    choix = int(input(""" 
                      1 : ajouter un nouveau etudiant
                      2 : modifier un etudiant exicte
                      3 : suprimer un etudiant 
                      4 : afficher un etudiant
                      5 : afficher tout les etudiant  
                      6 : Quitter       
                      
                      entrer votre choix ? """))

    if choix == 1 :
      ajouter_etudiant()

    elif choix == 2 :
      modifier_etudiant()

    elif choix == 3 :
      suprimer_etudiant()
    
    elif choix == 4 :
      afficher_etudiant()
    
    elif choix == 5 :
      afficher_liste_etudiants()
    
    elif choix == 6 :
      is_closed = True
    
    else:
      print('choix invalid')
    
    if(choix != 6):
      is_closed = shouldQuit()

  print("----------------- Au Revoir ! ---------------")


def shouldQuit():
  stay = input("voulez vous continuer ? oui/non : ")

  return stay.lower() == "non"


#-------------------------------------------------------------------------------
#                          Programme Principale
#-------------------------------------------------------------------------------

afficher_menu()