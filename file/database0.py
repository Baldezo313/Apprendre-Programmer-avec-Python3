import sqlite3

# ===== Creation d'une base de donnée====
# fichierDonnees = "C:/Users/balde/Desktop/Oreilli/cours/file/bd_test.sq3"
# conn = sqlite3.connect(fichierDonnees)
# cur = conn.cursor()
# cur.execute("CREATE TABLE members (age INTEGER, nom TEXT, taille REAL)")
# cur.execute("INSERT INTO members(age, nom, taille) VALUES(28, 'Baldezo', 1.83)")
# cur.execute("INSERT INTO members(age, nom, taille) VALUES(26, 'Chaimae', 1.85)")
# cur.execute("INSERT INTO members(age, nom, taille) VALUES(15, 'Rouguiata', 1.60)")
# conn.commit()
# cur.close()
# conn.close()

# ===== Connection à la base de donnée=====
conn = sqlite3.connect("C:/Users/balde/Desktop/Oreilli/cours/file/bd_test.sq3")
cur = conn.cursor()
# cur.execute("SELECT * FROM members")

# for l in cur:
#     print(l)

# print(list(cur))

# print(cur.fetchall())

# cur.execute("INSERT INTO members(age, nom, taille) VALUES(45, 'Ricard', 1.75)")

# data = [(27, 'Aliou', 1.87), (26, 'Alpha', 1.62), (30, 'Cheikh', 1.69)]
# for tu in data:
#     cur.execute("INSERT INTO members(age,nom,taille) VALUES(?,?,?)", tu)
# conn.commit()

# Updated (modifier ou remplacer) la réquette
cur.execute("UPDATE members SET nom = 'Lapha' WHERE nom='Alpha'")
# Supprimer un enregistrement
# cur.execute("DELETE FROM members WHERE nom='Lapha'")
# conn.commit()          # Enregistrer les modification
# conn.close()           # fermer la connection 




