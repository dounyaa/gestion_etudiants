import sqlite3
from datetime import datetime
from etudiant import Etudiant

#-----------------------------------------------------------------------------------------------------
#                                       VARIABLES
#-----------------------------------------------------------------------------------------------------
chemin_bd = "etudiantbd.db"
format_date = "%Y-%m-%d %H:%M:%S"

#-----------------------------------------------------------------------------------------------------
#                                       FONTIONS
#-----------------------------------------------------------------------------------------------------
def executer_requette(requette, parametres):
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()

  cursor.execute(requette, parametres)

  conn.commit()
  conn.close()


def sauvegarder_etudiant(etudiant):
  etudiant.date_created = str(datetime.now().strftime(format_date))

  parametres = etudiant.getEtudiantAsParams()

  requette_insertion = """INSERT INTO Etudiant(numero , nom, prenom, date_naissance, email, telephone, filiere, option, date_created) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) """ 

  executer_requette(requette_insertion, parametres)


def generer_numero_etudiant():
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()

  select_query = """SELECT COUNT(*) FROM Etudiant"""
  res = cursor.execute(select_query).fetchone()[0]

  numero = int(res) + 1

  conn.close()
  return numero


def in_db(numero):
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()
  select_query = f"""SELECT COUNT(1) FROM Etudiant WHERE numero = :numero"""
  params = {
    "numero": numero
  }
  res = cursor.execute(select_query, params).fetchone()[0]

  return res > 0


def modifier_etudiant_db(colonne, value , numero):
  requette = f"""UPDATE Etudiant SET {colonne} = :value WHERE numero = :numero"""
  parametres = {
    'value' : value,
    'numero' : numero
  }

  executer_requette(requette, parametres)


def supprimer_etudiant_db(numero):
  requette = """DELETE from Etudiant where numero = :numero"""
  parametres = {
    'numero': numero
  }

  executer_requette(requette, parametres)


def trouver_etudiant(numero):
  requette = """SELECT * FROM Etudiant WHERE numero = :numero"""
  parametres = {
    'numero': numero
  }

  list_etudiant = recuperer_etudiants(requette, parametres)
  
  if(len(list_etudiant) == 0):
    return None
  
  return list_etudiant[0]


def afficher_etudiant_par(colonne, valeur):
  requette = f"""SELECT * FROM Etudiant WHERE {colonne} = :valeur"""
  parametres = {
    'valeur': valeur
  }

  list_etudiant = recuperer_etudiants(requette, parametres)

  for etudiant in list_etudiant:
    etudiant.afficher()
    print("---------------------------------")


def afficher_etudiant_par_date(condition, date_creation):
  requette = f"""SELECT *  FROM Etudiant WHERE strftime('%Y-%m-%d', date_created) {condition}  strftime('%Y-%m-%d', :date_creation)"""
  parametres = {
    'date_creation': date_creation
  }
  
  list_etudiant = recuperer_etudiants(requette, parametres)

  if len(list_etudiant) == 0:
    print("aucun etudiant inscrit à cette date ou date invalide")
    return

  for etudiant in list_etudiant:
    etudiant.afficher()
    print("---------------------------------")


def recuperer_etudiants(requette, parametres):
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()

  resultat = cursor.execute(requette, parametres).fetchall()

  conn.close()
  list_etudiant = []

  for r in resultat:
    etudiant = ConvertirEnEtudiant(r)
    list_etudiant.append(etudiant)

  return list_etudiant


def get_filiere():
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()

  select_query = """SELECT DISTINCT filiere FROM Etudiant"""
  resultat = cursor.execute(select_query).fetchall()
  
  liste_filiere = []
  for r in resultat:
    liste_filiere.append(r[0])

  conn.close()

  return liste_filiere


def get_option():
  conn = sqlite3.connect(chemin_bd)
  cursor = conn.cursor()
  select_query = """SELECT DISTINCT option FROM Etudiant"""
  resultat = cursor.execute(select_query).fetchall()
  
  list_option = []
  for r in resultat:
    list_option.append(r[0])
  
  conn.close()

  return list_option


def ConvertirEnEtudiant(resultat):
  etudiant = Etudiant()
  etudiant.numero = resultat[0] 
  etudiant.nom = resultat[1] 
  etudiant.prenom = resultat[2] 
  etudiant.date_naissance = resultat[3] 
  etudiant.email = resultat[4]
  etudiant.telephone = resultat[5]
  etudiant.filiere = resultat[6] 
  etudiant.option = resultat[7] 
  etudiant.date_created = resultat[8]

  return etudiant
