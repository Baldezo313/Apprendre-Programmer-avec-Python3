import sqlite3

# ==== Création de la base de données <<musique>>:
"""Création et Alimentation d'une petite base de données SQLite"""

# Etablissement de la connexion -Création du curseur :
connex = sqlite3.connect("musique.sq3")
cur = connex.cursor()
# Création des tables. L'utilisation de try/except permet de réutiliser le script indéfiniment,
# même si la base de données existe déjà.
# try:
#     req = "CREATE TABLE compositeurs(comp TEXT, a_naiss INTEGER, a_mort INTEGER)"
#     cur.execute(req)
#     req = "CREATE TABLE oeuvres(comp TEXT, titre TEXT, duree INTEGER, interpr TEXT)"
#     cur.execute(req)
# except:
#     pass  # Les tables existent certainement déja => on continue.
# print("Entrée des enregistrements, table des compositeurs :")
# while 1:
#     nom = input("Nom du compositeur (<Enter> pour terminer) : ")
#     if nom =='':
#         break
#     aNais = input("Année de naissance : ")
#     aMort = input("Année de mort : ")
#     req = "INSERT INTO compositeurs(comp, a_naiss, a_mort) VALUES (?,?,?)"
#     cur.execute(req, (nom, aNais, aMort))
#
# print("Rappel des infos introduites :")
# cur.execute("SELECT * FROM compositeurs")
# for enreg in cur:
#     print(enreg)
#
# print("Entrée des enregistrement, table des oeuvres musicales :")
# while 1:
#     nom = input("Nom du compositeur (<Enter> pour terminer) : ")
#     if nom == '':
#         break
#     titre = input("Titre de l'oeuvre : ")
#     duree = input("durée (minutes) : ")
#     inter = input("interprète principal : ")
#     req = "INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES (?,?,?,?)"
#     cur.execute(req, (nom, titre, duree, inter))
#
# print("Rappel des infos introduites :")
# cur.execute("SELECT * FROM oeuvres")
# for enreg in cur:
#     print(enreg)
#
# # Transfert effectif des enregistrements dans la BD :
# connex.commit()

# === La requête SELECT ===

# cur.execute("select * from oeuvres where comp = 'Mozart'")
# print(cur.fetchall())

# cur.execute("SELECT comp, titre, duree FROM oeuvres ORDER BY comp")
# print(cur.fetchall())

# cur.execute("SELECT titre, comp FROM oeuvres WHERE comp='Beethoven' OR comp='Mozart' ORDER BY comp")
# print(cur.fetchall())

# cur.execute("SELECT COUNT(*) FROM oeuvres")
# print(cur.fetchall())

# cur.execute("SELECT SUM(duree) FROM oeuvres")
# print(cur.fetchall())

# cur.execute("SELECT AVG(duree) FROM oeuvres")
# print(cur.fetchall())

# cur.execute("SELECT SUM(duree) FROM oeuvres WHERE comp='Beethoven'")
# print(cur.fetchall())

# cur.execute("SELECT * FROM oeuvres WHERE duree > 35 ORDER BY duree DESC")
# print(cur.fetchall())

# cur.execute("SELECT * FROM compositeurs WHERE a_mort < 1800")
# print(cur.fetchall())

# cur.execute("SELECT * FROM compositeurs WHERE a_mort < 1800 LIMIT 3")
# print(cur.fetchall())

# =================================================
# cur.execute("SELECT o.titre, c.comp, a_naiss FROM oeuvres AS o, compositeurs AS c WHERE o.comp=c.comp")
# print(cur.fetchall())

# cur.execute("SELECT comp, titre, a_naiss FROM oeuvres JOIN compositeurs USING(comp)")
# print(cur.fetchall())

# cur.execute("SELECT * FROM oeuvres JOIN compositeurs USING(comp) ORDER BY a_mort")
# print(cur.fetchall())

# cur.execute("SELECT comp FROM oeuvres INTERSECT SELECT comp FROM compositeurs")
# print(cur.fetchall())

# cur.execute("SELECT comp from oeuvres except SELECT comp FROM compositeurs")
# print(cur.fetchall())

# cur.execute("SELECT comp FROM compositeurs except SELECT comp FROM oeuvres")
# print(cur.fetchall())

# cur.execute("SELECT DISTINCT comp FROM oeuvres UNION SELECT comp FROM compositeurs")
# print(cur.fetchall())