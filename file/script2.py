import os
from tkinter import *
from random import randrange
from math import *
import pickle
from random import *

# obFichier = open('Monfichier', 'a')
# obFichier.write('Bonjour, fichier !')
# obFichier.write("Quel beau temps, aujourd'hui")
# obFichier.close()

# ofi = open('Monfichier', 'r')
# t = ofi.read()
# print(t)
# ofi.close()
# t = ofi.read(7)
# print(t)
# t = ofi.read(1000)
# print(t)

# def copieFichier(source, destination):
#     "copie intégrale d'un fichier"
#     fs = open(source, 'r')
#     fd = open(destination, 'w')
#     while 1:
#         txt = fs.read(50)
#         if txt =="":
#             break
#         fd.write(txt)
#     fs.close()
#     fd.close()
#     return


# copieFichier('Monfichier', 'Tonfichier')

# f = open("Fichiertexte", "w")
# f.write("Ceci est la ligne un\nVoice la ligne deux\n")
# f.write("Voici la ligne trois\nVoici la ligne quatre\n")
# f.close()

# f = open('Fichiertexte', 'r')
# t = f.readline()
# print(t)
# print(f.readline())

# t = f.readlines()
# print(t)
# f.close()


# def filtre(source, destination):
#     "recopier un fichier en éliminant les lignes de remarques"
#     fs = open(source, 'r')
#     fd = open(destination, 'w')
#     while 1:
#         txt = fs.readline()
#         if txt == '':
#             break
#         if txt[0] != '#':
#             fd.write(txt)
#     fs.close()
#     fd.close()
#     return

# a, b, c = 5, 2.83, 67
# f = open('Monfichier', 'w')
# f.write(str(a))
# f.write(str(b))
# f.write(str(c))
# f.close()
# f = open('Monfichier', 'r')
# print(f.read())
# f.close()

# a, b, c = 27, 12.96, [5, 4.83, "René"]
# f = open('donnees_test', 'wb')
# pickle.dump(a, f)
# pickle.dump(b, f)
# pickle.dump(c, f)
# f.close()
# f = open('donnees_test', 'rb')
# j = pickle.load(f)
# k = pickle.load(f)
# l = pickle.load(f)
# print(j, type(j))
# print(k, type(k))
# print(l, type(l))
# f.close()

# filename = input("Veuillez entrez un nom de fichier : ")
# try:
#     f = open(filename, "r")
# except:
#     print("Le fichier", filename, "est introuvable")

# def existe(fname):
#     try:
#         f = open(fname, 'r')
#         f.close()
#         return 1
#     except:
#         return 0
#
#
# filename = input("Veuillez entrer le nom du fichier : ")
# if existe(filename):
#     print("Ce fichier existe bel et bien.")
# else:
#     print("Le fichier", filename, "est introuvable.")

# =============================================================
"""Èditeur simple, pour lire et écrire dans un fichier 'text'"""
# =============================================================


# def sansDC(ch):
#     "Cette fonction renvoie la chîane ch amputée de son dernier caractère"
#     nouv = ""
#     i, j = 0, len(ch) -1
#     while i < j:
#         nouv = nouv + ch[i]
#         i = i+1
#     return nouv
#
#
# def ecrireDansFichier():
#     of = open(nomF, 'a')
#     while 1:
#         ligne = input("Entrez une ligne de texte (ou <Entrer>) : ")
#         if ligne == '':
#             break
#         else:
#             of.write(ligne + '\n')
#     of.close()
#
#
# def lireDansFichier():
#     of = open(nomF, 'r')
#     while 1:
#         ligne = of.readline()
#         if ligne == "":
#             break
#         # afficher en omettant le dernier caractère (= fin de ligne) :
#         print(sansDC(ligne))
#     of.close()
#
#
# nomF = input('Nom du fichier à traiter : ')
# choix = input('Entrez "e" pour écrire, "c" pour consulter les données : ')
#
# if choix =='e':
#     ecrireDansFichier()
# else:
#     lireDansFichier()

# ========================================================
"""Génération des tables de multiplication de 2 à 30"""
# ========================================================


# def tableMulti(n):
#     # Fonction générant la table de multiplication par n (20 termes)
#     # La table sera renvoyée sous forme d'une chaîne de caractères :
#     i, ch = 0, ""
#     while i < 20:
#         i += 1
#         ch = ch + str(i * n) + " "
#     return ch
#
#
# NomF = input("Nom du fichier à créer : ")
# fichier = open(NomF, "w")
#
# # Génération des tables de 2 à 30 :
# table = 2
# while table < 31:
#     fichier.write(tableMulti(table) + '\n')
#     table = table + 1
# fichier.close()


# ========================================================
"""FCT qui triple les espaces entre mots dans une chaîne de caractères"""
# ========================================================
"""Triplement des espaces dans un fichier texte.
Ce script montre également comment modifier le contenu d'un fichier en le 
transférant d'abord tout entier dans une liste, puis en ré-enregistrant
celle-ci après modifications """

# def triplerEspaces(ch):
#     "fct qui triple les espaces entre mots dans la chaîne ch"
#     i, nouv = 0, " "
#     while i < len(ch):
#         if ch[i] == " ":
#             nouv = nouv + "  "
#         else:
#             nouv = nouv + ch[i]
#         i = i + 1
#     return nouv
#
#
# nomF = input("Nom du fichier : ")
# fichier = open(nomF, 'r+')          # 'r+' = mode read/write
# lignes = fichier.readlines()        # lire toutes les lignes
#
# n = 0
# while n < len(lignes):
#     lignes[n] = triplerEspaces(lignes[n])
#     n += 1
#
# fichier.seek(0)                     # retour au debut du fichier
# fichier.writelines(lignes)          # réenregistrement
# fichier.close()

# ===============================================================
"""Fct qui arrondie un Nombre présenté dans la chaîne de caractère"""
# ===============================================================
""" Mise en forme de données numériques.
Le fichier traité est un fichier texte dont chaque ligne contient un nombre
réel (sans exposants et encodé sous la forme d'une chaîne de caractères)"""

# def valArrondie(ch):
#     "représentation arrondie du nombre présenté dans la chaîne ch"
#     f = float(ch)  # conversion de la chaîne en un nombre réel
#     e = int(f + .5)  # conversion en entier (On ajoute d'abord 0.5
#     # au réel pour l'arrondir correctement)
#     return str(e)  # reconverion en chaîne de caractères
#
#
# fiSource = input("Nom du fichier à traiter : ")
# fiDest = input("Nom du fichier destinataire : ")
# fs = open(fiSource, 'r')
# fd = open(fiDest, 'w')
#
# while 1:
#     ligne = fs.readline()  # lecture d'une ligne du fichier
#     if ligne == "" or ligne == "\n":
#         break
#     ligne = valArrondie(ligne)
#     fd.write(ligne + "\n")
#
# fd.close()
# fs.close()

# ============================================================
""" Comparaison de deux fichiers, caractère par caractère"""
# ============================================================

# fich1 = input("Nom du premier fichier : ")
# fich2 = input("Nom du second fichier : ")
# fi1 = open(fich1, 'r')
# fi2 = open(fich2, 'r')
#
# c, f = 0, 0  # compteur de caractères et "drapeau"
# while 1:
#     c += 1
#     car1 = fi1.read(1)  # lecture d'une caractère dans chacun
#     car2 = fi2.read(1)  # des deux fichiers
#     if car1 == "" or car2 == "":
#         break
#     if car1 != car2:
#         f = 1
#         break  # différence trouvée
# fi1.close()
# fi2.close()
#
# print("Ces 2 fichiers", end=' ')
# if f == 1:
#     print("diffèrence à partir du caractère n°", c)
# else:
#     print("sont identiques.")


# ==============================================================
"""Combinaison de deux fichiers texte pour en faire un nouveau"""

# fichA = input("Nom du premier fichier : ")
# fichB = input("Nom du second fichier : ")
# fichC = input("Nom du fichier destinataire : ")
# fiA = open(fichA, 'r')
# fiB = open(fichB, 'r')
# fiC = open(fichC, 'w')
#
# while 1:
#     ligneA = fiA.readline()
#     ligneB = fiB.readline()
#     if ligneA == "" and ligneB == "":
#         break                       # on est arrivé à la fin des 2 fichiers
#     if ligneA != "":
#         fiC.write(ligneA)
#     if ligneB != "":
#         fiC.write(ligneB)
#
# fiA.close()
# fiB.close()
# fiC.close()

# ================================================================
""" Enregistrer les coordonnées des membres d'un club """
# ================================================================


# Enregistrer les coordonnées des membres d'un club
# def encodage():
#     "renvoie la liste des valeurs entrées, ou une liste vide"
#     print("*** Veuillez entrer les données (ou <Enter> pour terminer) :")
#     while 1:
#         nom = input("Nom : ")
#         if nom == "":
#             return []
#         prenom = input("Prénom : ")
#         rueNum = input("Adresse (N° et rue) : ")
#         cPost = input("Code postal : ")
#         local = input("Localité : ")
#         tel = input("N° de téléphone : ")
#         print(nom, prenom, rueNum, cPost, local, tel)
#         ver = input("Entrez <Enter> si c'est correct, sinon <n> ")
#         if ver == "":
#             break
#     return [nom, prenom, rueNum, cPost, local, tel]
#
#
# def enregistrer(liste):
#     "enregistre les données de la liste en les séparant par des <#>"
#     i = 0
#     while i < len(liste):
#         of.write(liste[i] + "#")
#         i = i + 1
#     of.write("\n") # caractère de fin de ligne
#
#
# nomF = input('Nom du fichier destinataire : ')
# of = open(nomF, 'a')
# while 1:
#     tt = encodage()
#     if tt == []:
#         break
#     enregistrer(tt)
# of.close()
#
# """ Ajouter des informations dans le fichier du Club"""
#
#
# def traduire(ch):
#     "convertir une ligne du fichier source en liste de données"
#     dn = "" # chaîne temporaire pour extraire les données
#     tt = [] # la liste à produire
#     i = 0
#     while i < len(ch):
#         if ch[i] == "#":
#             tt.append(dn)  # on ajoute la donnée à la liste, et
#             dn = ""  # on réinitialise la chaine temporaire
#         else:
#             dn = dn + ch[i]
#         i = i + 1
#     return tt
#
#
# def encodage(tt):
#     "renvoyer la liste tt, complétée avec la date de naissance et le sexe"
#     print("*** Veuillez entrer les données (ou <Enter> pour terminer) :")
#     # Affichage des données déjà présentes dans la liste :
#     i = 0
#     while i < len(tt):
#         print(tt[i], end =' ')
#         i = i +1
#     print()
#     while 1:
#         daNai = input("Date de naissance : ")
#         sexe = input("Sexe (m ou f) : ")
#         print(daNai, sexe)
#         ver = input("Entrez <Enter> si c'est correct, sinon <n> ")
#         if ver == "":
#             break
#     tt.append(daNai)
#     tt.append(sexe)
#     return tt
#
#
# def enregistrer(tt):
#     "enregistrer les données de la liste tt en les séparant par des <#>"
#     i = 0
#     while i < len(tt):
#         fd.write(tt[i] + "#")
#         i = i + 1
#     fd.write("\n") # caractère de fin de ligne
#
#
# fSource = input('Nom du fichier source : ')
# fDest = input('Nom du fichier destinataire : ')
# fs = open(fSource, 'r')
# fd = open(fDest, 'w')
# while 1:
#     ligne = fs.readline() # lire une ligne du fichier source
#     if ligne =="" or ligne =="\n":
#         break
#     liste = traduire(ligne) # la convertir en une liste
#     liste = encodage(liste) # y ajouter les données supplémentaires
#     enregistrer(liste) # sauvegarder dans fichier dest.
# fd.close()
# fs.close()

# =============================================================
""" Rechercher de lignes particulières dans un fichier texte :"""

# def chercheCP(ch):
#     "recherche dans ch la portion de chaîne contenant le code postal"
#     i, f, ns = 0, 0, 0      # ns est un compteur de codes #
#     cc = ""                 # chaîne à construire
#     while i < len(ch):
#         if ch[i] == "#":
#             ns = ns + 1
#             if ns == 3:     # le CP se trouve après le 3e code #
#                 f = 1       # variable "drapeau" (flag)
#             elif ns == 4:    # inutile de lire après le 4e code #
#                 break
#         elif f == 1:        # le caractère lu fait partie du
#             cc = cc + ch[i]     # CP recherché -> on mémorise
#             i = i + 1
#     return cc
#
#
# nomF = input("Nom du fichier à traiter : ")
# codeP = input("Code postal à rechercher : ")
# fi = open(nomF, 'r')
# while 1:
#     ligne = fi.readline()
#     if ligne =="":
#         break
#     if chercheCP(ligne) == codeP:
#         print(ligne)
# fi.close()

# nom = 'Cédric'
# print(nom[1], nom[3], nom[5])
# print(nom[-1], nom[-2], nom[-4], nom[-6])
# print(len(nom))

# ch = "Juliette"
# print(ch[0:3])
# print(ch[:3])           # les 3 premiers caractères
# print(ch[3:])           # Tous ce qui suit les 3 premiers caractères

# ch = 'Adélaïde'
# print(ch[:3], ch[4:8])

# n = 'abc' + 'def'               # concaténation
# m = 'zut ! ' * 4                # répétition
# print(n, m)

# =============================================================
"""Découpage d'une chaîne en fragments"""
# =============================================================


# def decoupe(ch, n):
#     "découpage de la chaîne ch en une liste de fragments de n caractères"
#     d, f = 0, n             # indices de début et de fin de fragment
#     tt = []                 # liste à construire
#     while d < len(ch):
#         if f > len(ch):         # On ne peut pas découper au-delà de la fin
#             f = len(ch)
#         fr = ch[d:f]            # découpage d'un fragment
#         tt.append(fr)           # ajout du fragment à la liste
#         d, f = f, f + n         # indices suivants
#     return tt
#
#
# def inverse(tt):
#     "rassemble les éléments de la liste tt dans l'ordre inverse"
#     ch = ""             # chaîne à construire
#     i = len(tt)         # on commence par la fin de la liste
#     while i > 0:
#         i = i - 1       # le dernier élément possède l'indice n-1
#         ch = ch + tt[i]
#     return ch
#
#
# # Test :
# if __name__ == '__main__':
#     ch = "abcdefghijklmnopqrstuvwxyz123456789âêîôûàèìòùáéíóú"
#     liste = decoupe(ch, 5)
#     print("chaîne initiale :")
#     print(ch)
#     print("liste de fragments de 5 caractères :")
#     print(liste)
#     print("fragments rassemblés après inversion de la liste :")
#     print(inverse(liste))

# ================================================================
""" Rechercher l'indice d'un caractère donné dans une chaîne """
# ===============================================================


# def trouve(ch, car, deb=0):
#     "trouver l'indice du caractère car dans la chaîne ch"
#     i = deb
#     while i < len(ch):
#         if ch[i] == car:
#             return i        # le caractère est trouvé -> on termine
#         i = i+1
#     return -1               # toute la chaîne a été scannée sans succés
#
#
# # Test :
# if __name__ == '__main__':
#     print(trouve("Coucou c'est moi", "z"))
#     print(trouve("Juliette & Roméo", "&"))
#     print(trouve("César & Cléopâtre", "r", 5))


# =================================================================
"""Comptage des occurrences d'un caractère donné dans une chaîne"""
# =================================================================

# def compteCar(ch, car):
#     "trouve l'indice du caractère car dans la chaîne ch"
#     i, nc = 0, 0                # initialisations
#     while i < len(ch):
#         if ch[i] == car:
#             nc = nc + 1         # caractère est trouvé -> on incrémente le compteur
#         i = i+1
#     return nc
#
#
# # Test :
# if __name__ == '__main__':
#     print(compteCar("ananas au jus", "a"))
#     print(compteCar("Gédon est déjà là", "é"))
#     print(compteCar("Gédon est déjà là", "à"))


# =============================================================
# nom = "Joséphine"
# index = 0
# while index < len(nom):
#     print(nom[index] + ' *', end=' ')
#     index = index + 1

# nom = "Cléopâtre"
# for car in nom:
#     print(car + ' *', end=' ')

# liste = ['chien', 'chat', 'crocodile', 'éléphant']
# for animal in liste:
#     print('longueur de la chaîne', animal, '=', len(animal))

# divers = ['lézard', 3, 17.25, [5, 'Jean'], (5, "car"), {"a": 4}]
# for e in divers:
#     print(e, type(e))

# =================================================================
"""Concaténer deux chaîne de caractère"""
# =================================================================

# prefixes, suffixe = "JKLMNOP", "ack"
#
# for p in prefixes:
#     print(p + suffixe)

# ================================================================
"""FCT qui recherche le nbr de mots dans une chaine de caractère"""
# ===============================================================


# def compteMots(ch):
#     "compter du nombre de mots dans la chaîne ch"
#     if len(ch) == 0:
#         return 0
#     nm = 1                  # la chaîne comporte au moins un mot
#     for c in ch:
#         if c == " ":        # il suffit de compter les espaces
#             nm = nm + 1
#     return nm
#
# # Test :
# if __name__ == '__main__':
#     print(compteMots("Les petits ruisseaux font les grandes rivières"))

# =======================================
"""FCT qui recherche le nbr de caractère listé dans une phrase donnée"""
# ==================================================================


# def compteCar(ch, car):
#     "comptage du nbr de caractères <car> la chaîne <ch>"
#     if len(ch) == 0:
#         return 0
#     n = 0
#     for c in ch:
#         if c == car:
#             n = n+1
#     return n
#
#
# # Programme principal :
# def compteCarDeListe(chaine, serie):
#     "dans la chaine <ch>, comptage du nbr de caractères listés dans <serie>"
#     for cLi in serie:
#         nc = compteCar(chaine, cLi)
#         print("Caractère", cLi, ":", nc)
#
#
# # Test :
# if __name__ == '__main__':
#     txt = "René et Célimène étaient eux-même nés à Noël de l'année dernière"
#     print(txt)
#     compteCarDeListe(txt, "eéèêë")

# ===============================================================
# car = "e"
# voyelles = "aeiouyAEIOUàâéèâëùîï"
# if car in voyelles:
#     print(car, "est une voyelle")

# n = 5
# premiers = [1, 2, 3, 5, 7, 11, 13, 17]
# if n in premiers:
#     print(n, "fait partie de notre liste de nbr de premiers")

# ==================================================================
"""FCT qui vérifie si un caractère est un chiffre"""
# ===================================================================


# def estUnChiffre(car):
#     "renvoie <vrai> si le caractère 'car' est un chiffre"
#     if car in "0123456789":
#         return "vrai"
#     else:
#         return "faux"
#
#
# # Test :
# if __name__ == '__main__':
#     caracteres = "d75è8b0â1"
#     print("Caractères à tester :", caracteres)
#     for car in caracteres:
#         print(car, estUnChiffre(car))

# =================================================================
"""FCT qui rechercher un Majuscule"""


# =================================================================


def estUneMaj(car):
    "renvoie <vrai> si le caractère 'car' est une majuscule"
    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÇÎÏÙÜÛÔÖ":
        return True
    else:
        return False


#
# # Test :
# if __name__ == '__main__':
#     caracteres = "eÀçMöSÖÛmÇéùT"
#     print("Caractères à tester :", caracteres)
#     for car in caracteres:
#         print(car, estUneMaj(car))

# =================================================================
"""FCT qui convertie une chaine de caractère en une liste de mots"""


# =================================================================


def chaineListe(ch):
    "convertit la chaîne ch en une liste de mots"
    liste, ct = [], ""  # ct est une chaîne temporaire
    for c in ch:  # examiner tous les caractères de ch
        if c == " ":  # lorsqu'on rencontre un espace,
            liste.append(ct)  # on ajoute la chaîne temporaire à la liste
            ct = ""  # ... et on ré-initialise la chaîne temporaire
        else:
            # Les autres caractères examnés sont ajoutés à la chaîne temp
            ct = ct + c
    # Ne pas oublier le mot restant après le dernier espace ! :
    if ct:  # vérifier si ct n'est pas une chaîne vide
        liste.append(ct)
    return liste  # renvoie la liste ainsi construite


# Tests :
# if __name__ == '__main__':
#     li = chaineListe("René est un garçon au caractère héroïque")
#     print(li)
#     for mot in li:
#         print(mot, "-", end=' ')
#     print(chaineListe(""))          # doit renvoyer une liste vide

# ==================================================================
"""FCT qui verifie si un caractère est un MAJ et l'extraire"""
# ==================================================================

# txt = "Le prénom de cette Monsieur est Baldezo"
# print("Phrase à tester :", txt)
#
# lst = chaineListe(txt)              # convertir la phrase en une liste de mots

# for mot in lst:                 # analyser chacun des mots de la liste
#     prem = mot[0]               # extraction du premier caractère
#     if estUneMaj(prem):
#         print(mot)

# Variante plus compacte, utilisant la composition :
# print("Variante :")
# for mot in lst:
#     if estUneMaj(mot[0]):
#         print(mot)

# =================================================================
"""FCT qui renvoie le Nbr de caractère MAJ dans une chaîne de caractère"""


# =================================================================


def compteMaj(ch):
    "comptage des mots débutant par une majuscule dans la chaîne ch"
    c = 0
    lst = chaineListe(ch)  # convertir la phrase en une liste de mots
    for mot in lst:  # analyser chacun des mots de la liste
        if estUneMaj(mot[0]):
            c = c + 1
    return c


#
# # TEST :
# if __name__ == '__main__':
#     phrase = "Les filles Tidgoutt se nomment Joséphine, Justine et Corinne"
#     print("Phrase à tester : ", phrase)
#     print("Cette phrase contient", compteMaj(phrase), "majuscule.")

# =================================================================

# salut = 'bonjour à tous'
# salut = 'B' + salut[1:]
# print(salut)

# while True:
#     mot = input("Entrez un mot quelconque : (<entrer> pour terminer)")
#     if mot =="":
#         break
#     if mot < "limonade":
#         place = "précède"
#     elif mot > "limonade":
#         place = "suit"
#     else:
#         place = "se confond avec"
#     print("Le mot", mot, place, "le mot 'limonade' dans l'ordre alphabétique")

# ==================================================================
# chaine = "Amélie et Eugène\n"
# of = open("test1.txt", "w")
# of.write(chaine)
#
# of.close()

# of = open("test1.txt", "rb")            # "rb" => mode lecture (r) binaire (b)
# octets = of.read()
# of.close()
# print(type(octets))
# print(octets)

# for oct in octets:
#     print(oct, end=' ')

# print(len(chaine))
# print(len(octets))

"""Conversion d'une chaîne bytes en chaîne string"""
# ch_car = octets.decode("latin-1")           # "utf8" ne pase passe pas !!!
# print(ch_car)
# print(type(ch_car))

"""Conversion d'une chaine string en chaîne bytes"""
# chaine = "Bonne fête de Noël"
# octets_u = chaine.encode("utf-8")
# octets_l = chaine.encode("Latin-1")
# print(octets_u)
# print(octets_l)

"""Conversions automatiques lors du traitement des fichiers"""

chaine = "Amélie et Eugène\n"
of = open("test1.txt", "w", encoding="Latin-1")
of.write(chaine)
of.close()
#
# of = open("test1.txt", "rb")
# octets = of.read()
# of.close()
# print(octets)

# of = open("test1.txt", "r")
# ch_lue = of.read()

# of = open("test1.txt", "r", encoding ="Latin-1")
# ch_lue = of.read()
# of.close()
# print(ch_lue)

# =================================================================
"""Alphabet grec (minuscule)"""
# =================================================================
# s = ""                  # chaîne vide
# i = 945                 # premier code
# while i <= 969:         # dernier code
#     s += chr(i)
#     i = i + 1
# print("Alphabet grec (minuscule) : ", s)

# =================================================================
"""Script qui affiche une table des codes ASCII"""
# =================================================================

# c = 32                  # premier code ASCII <imprimable>

# while c < 128:          # dernier code strictement ASCII = 127
#     print("Code", c, ":", chr(c), end=" - ")
#     c = c+1

# =================================================================
"""FCT qui convertir les Majuscules en minuscule et vice versa """


# =================================================================


def convMajMin(ch):
    "échange les majuscules et les minuscules dans la chaîne ch"
    nouvC = ""  # chaîne à construire
    for car in ch:
        code = ord(car)
        # Les codes numériques des caractères majuscules et minuscules
        # correspondant sont séparés de 32 unités :
        if 65 <= code <= 91:  # majuscule ordinaires
            code = code + 32
        elif 192 <= code <= 222:  # majuscule accentuées
            code = code + 32
        elif 97 <= code <= 122:  # minuscule ordinaires
            code = code - 32
        elif 224 <= code <= 254:  # minuscules accentuées
            code = code - 32
        nouvC = nouvC + chr(code)
    # renvoi de la chaîne construite :
    return nouvC


# # Test :
# if __name__ == '__main__':
#     txt = "Émile Noël épouse Irène Müller"
#     print(txt)
#     print(convMajMin(txt))

# =================================================================
"""Traitement et Conversion d'un fichier Latin-1 en Utf-8"""


# ================================================================


def traiteLigne(ligne):
    "remplacement des espaces de la ligne de text par '-*-' "
    newline = ""  # nouvelle chaîne à construire
    c, m = 0, 0  # initialisations
    while c < len(ligne):  # lire tous les caractères de la ligne
        if ligne[c] == " ":
            # Le caractère lu est un espace.
            # On ajoute une 'tranche' à la chaîne en cours de construction :
            newline = newline + ligne[m:c] + "_*_"
            # On mémorise dans m la position atteinte dans la ligne lue :
            m = c + 1  # ajouter 1 pour "oublier" l'espace
        c = c + 1
    # Ne pas oublier d'ajouter la 'tranche' suivant le dernier espace :
    newline = newline + ligne[m:]

    # Renvoyer la chaîne construite :
    return newline


# # --- Programme Principal : ----
# nomFS = input("Nom du fichier source (Latin-1) : ")
# nomFD = input("Nom du fichier destinataire (Utf-8) : ")
# fs = open(nomFS, 'r', encoding="Latin1")                # ouverture des 2 fihiers
# fd = open(nomFD, 'w', encoding="Utf8")                  # dans les ecodages spécifiés
# while 1:                            # boucle de traitement
#     li = fs.readline()              # lecture d'une ligne
#     if li == "":                    # détection de la fin du fichier :
#         break                       # readline() renvoie une chaîne vide
#     fd.write(traiteLigne(li))       # traitement + écriture
# fd.close()
# fs.close()

# =================================================================
"""FCT qui Teste si un caractère donné est une voyelle"""


# =================================================================


def voyelle(car):
    "tester si le caractère <car> est une voyelle"
    if car in "AEIOUYÀÉÈÊËÎÏÔÛÙaeiouyàéèêëîïôûù":
        return True
    else:
        return True


# # Test :
# if __name__ == '__main__':
#     ch = "gOàÉsùïÇ"         # lettre à tester
#     for c in ch:
#         print(c, ":", voyelle(c))

# ================================================================
"""FCT qui compte le les voyelles et renvoie le nombre de voyelles"""


# ================================================================


def compteVoyelles(phrase):
    "compte les voyelles présentes dans la chaîne de caractères <phrase>"
    n = 0
    for c in phrase:
        if voyelle(c):
            n = n + 1
        return n


# # Test :
# if __name__ == '__main__':
#     texte = "Maître corbeau sur un arbre perché"
#     nv = compteVoyelles(texte)
#     print("La phrase <", texte, "> compte ", nv, " voyelles.", sep="")


# =================================================================
# c = 1040                    # code du premier caractère (majuscule)
# maju = ""                   # chaîne destinée aux majuscules
# minu = ""                   # chaîne destinée aux minuscules
# while c < 1072:             # on se limitera à cette gamme
#     maju = maju + chr(c)
#     minu = minu + chr(c + 32)
#     c = c+1
# print(maju)
# print(minu)


# =================================================================

# c2 = "Votez pour moi"
# a = c2.split()
# # print(a)
#
# c4 = "Cet exemple, parmi d'autres, peut encore servir"
# a1 = c4.split(",")
# print(a1)

# b = ["Bête", "a", "manger", "du", "foin"]
# print(" ".join(b))
# print("---".join(b))

# ch1 = "Cette leçon vaut bien un fromage, sans doute ?"
# ch2 = "fromage"
# print(ch1.find(ch2))

# ch1 = "Le héron au long bec emmanché d'un long cou"
# ch2 = 'long'
# print(ch1.count(ch2))

# ch = "CÉLIMÈNE est un prénom ancien"
# print(ch.lower())

# ch = "Maître Jean-Noël Hébèrt"
# print(ch.upper())

# ch = "albert rené élise véronique"
# print(ch.title())

# ch = "quel beau temps, aujourd'hui !"
# print(ch.capitalize())

# ch = "Le Lièvre Et La Tortue"
# print(ch.swapcase())

# ch = "  Monty Python  "
# print(ch.strip())

# ch = "Si ce n'est toi c'est donc ton frère"
# print(ch.replace(" ", "*"))

# ch = "Portez ce vieux whisky au juge blond qui fume"
# print(ch.index("w"))

# print(ch.index("e"))            # cherche à partir du début de la chaîne et trouve le 1er 'e'
# print(ch.index("e", 5))         # cherche seulement à partir de l'indice 5 et trouve le 2nd 'e'
# print(ch.index("e", 15))        # cherche à partir du caractère n°15 et trouve le 4em 'e'

# a = float("12.36")
# print(a + 5)

# n = 789
# txt = "Le nombre {0:d} (décimal) vaut {0:x} en hexadécimal et {0:b} en binaire."
# print(txt.format(n))
#
# coul = "verte"
# temp = 1.347 + 15.9
# print("La couleur est %s et la température vaut %s °C" % (coul, temp))

# =================================================================
"""Conversion en majuscule du premier caractère de chaque mot dans un texte."""
# =================================================================

# fiSource = input("Nom du fichier à traiter (Latin-1) : ")
# fiDest = input("Nom du fichier destinataire (Utf-8) : ")
# fs = open(fiSource, 'r', encoding="Latin1")
# fd = open(fiDest, 'w', encoding="Utf8")
#
# while 1:
#     ch = fs.readline()          # lecture d'une ligne
#     if ch == "":
#         break                   # fin du fichier
#     ch = ch.title()             # conversion des initiales en maj.
#     fd.write(ch)
#
# fd.close()
# fs.close()

# ================================================================
"""Conversion Latin-1 => Utf (variante utilisant une variable <bytes>)"""
# ================================================================
#
# fiSource = input("Nom du fichier à traiter (Latin-1) : ")
# fiDest = input("Nom du fichier destinataire (Utf-8) : ")
# fs = open(fiSource, 'rb')           # mode de lecture <binaire>
# fd = open(fiDest, 'wb')             # mode d'écriture <binaire>
#
# while 1:
#     so = fs.readline()          # la ligne lue une séquence d'octets
#     # Remarque : la variable so étant du type <bytes>, on doit la comparer
#     # avec une chaîne littérale (vide) du même type dans les tests :
#     if so == b"":
#         break               # fin du fichier
#     ch = so.decode("Latin-1")       # conversion en chaîne de caractères
#     ch = ch.replace(" ", "_*_")     # remplacement des espaces par _*_
#     so = ch.encode("Utf-8")         # Ré-encodage en une séquence d'octets
#     fd.write(so)                    # transcription
#
# fd.close()
# fs.close()

# ===============================================================
"""FCT qui compte le Nbre de mots dans un texte"""
# ===============================================================

# FiSource = input("Nom du fichier à traiter : ")
# fs = open(FiSource, 'r')
#
# n = 0               # variable compteur
# while 1:
#     ch = fs.readline()
#     if ch == "":            # fin du fichier
#         break
#     # conversion de la chaîne lue en une liste de mots :
#     li = ch.split()
#     # Totalisation des mots :
#     n = n+len(li)
# fs.close()
# print("Ce fichier texte contient un total de %s mots" % (n))

# ================================================================
"""FCT qui recopie un fichier texte en fusionnant les lignes pour former des phrases"""
# ================================================================

# fiSource = input("Nom du fichier à traiter (Latin-1) : ")
# fiDest = input("Nom du fichier destinataire (Utf-8) : ")
# fs = open(fiSource, 'r', encoding="Latin1")
# fd = open(fiDest, 'w', encoding="Utf8")
#
# # On lit d'abord la première ligne :
# ch1 = fs.readline()
# # On lit ensuite les suivantes, en les fusionnant si nécessaire :
# while 1:
#     ch2 = fs.readline()
#     if not ch2:                 # Rappel : une chaîne vide est considérée
#         break                   # comme "fausse" dans les tests
#     # Si la chaîne lue commence par une majuscule on transcrit
#     # la précédente dans le fichier destinataire, et on la
#     # remplace par celle que l'on vient de lire :
#     if ch2[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÎÏÔÙÛÇ":
#         fd.write(ch1)
#         ch1 = ch2
#     # Sinon, on la fusionne avec la précédente, en veillant à en
#     # enlever au préalable le ou les caractère(s) de fin de ligne.
#     else:
#         ch1 = ch1[:-1] + " " + ch2
#
# # Attention : ne pas oublier de transcrire la dernière ligne :
# fd.write(ch1)
# fd.close()
# fs.close()

# ================================================================
"""Caractèristiques de Sphères"""


# ================================================================


def caractSphere(d):
    "renvoie les caractèristiques d'une sphère de diamètre d"
    d = float(d)  # conversion de l'argument (ch=chaîne) en réel
    r = d / 2  # rayon
    ss = pi * r ** 2  # Surface de section
    se = 4 * pi * r ** 2  # surface exterieur
    v = 4 / 3 * pi * r ** 2  # volume
    # La balise {:8.2f} utilisé ci-dessous formate le nombre
    # affiché de manière à occuper 8 caractères au total, en arrondissant de
    # manière à conserver deux chiffres après la virgule :
    ch = "Diam. {:6.2f} cm Section = {:8.2f} cm^2 ".format(d, ss)
    ch = ch + "Surf. = {:8.2f} cm^2. Vol. = {:9.2f} cm^3".format(se, v)
    return ch


# fiSource = input("Nom du fichier à traiter : ")
# fiDest = input("Nom du fichier destinataire : ")
# fs = open(fiSource, 'r')
# fd = open(fiDest, 'w')
# while 1:
#     diam = fs.readline()
#     if diam == "" or diam == "\n":
#         break
#     fd.write(caractSphere(diam) + "\n")             # enregistrement
#     fd.close()
#     fs.close()

# =================================================================
"""Mise en forme de données numériques
Le fichier traité est un fichier <texte> dont chaque ligne contient un nombre
réel (sans exposant et encodé sous la forme d'une chaîne de caractères"""


# =================================================================


def arrondir(reel):
    "représentation arrondie à .0 ou .5 d'un nombre réel"
    ent = int(reel)  # partie entière du nombre
    fra = reel - ent  # partie fractionnaire
    if fra < .25:
        fra = 0
    elif fra < .75:
        fra = .5
    else:
        fra = 1
    return ent + fra


# fiSource = input("Nom du fichier à traiter : ")
# fiDest = input("Nom du fichier destinataire : ")
# fs = open(fiSource, 'r')
# fd = open(fiDest, 'w')
# while 1:
#     ligne = fs.readline()
#     if ligne == "" or ligne == "\n":
#         break
#     n = arrondir(float(ligne))          # conversion en <float>, puis arrondi
#     fd.write(str(n) + "\n")             # enregistrement
#
# fd.close()
# fs.close()

# =================================================================
"""Les listes sont des objets"""
# =================================================================

# nombres = [17, 38, 10, 25, 72]
# nombres.sort()                  # trier la liste
# print(nombres)
# nombres.append(12)              # ajouter un élément à la fin
# print(nombres)
# nombres.reverse()               # inverser l'ordre des éléments
# print(nombres)
# print(nombres.index(17))        # retrouver l'index d'un élément
# nombres.remove(38)              # enlever (effacer) un élément
# print(nombres)
# del nombres[2]
# print(nombres)
# del nombres[1:3]
# print(nombres)

# ================================================================
"""Affichage de tables de multiplication"""
# ================================================================

# nt = [2, 3, 5, 7, 9, 11, 13, 17, 19]
#
#
# def tableMulti(m, n):
#     "renvoie n termes de la table de multiplication par m"
#     ch = ""
#     for i in range(n):
#         v = m * (i+1)           # calcul d'un des termes
#         ch = ch + "%4d" % (v)   # formatage à 4 caractères
#     return ch
#
#
# for a in nt:
#     print(tableMulti(a, 15))            # 15 premiers termes seulement

# =================================================================
"""Script qui affiche chacun des noms d'un liste avec le nbr de caractères"""
# =================================================================

# # _*_ coding:Utf-8 _*_
#
# lst = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
# for e in lst:
#     print("%s : %s caractères" % (e, len(e)))

# =================================================================
"""Script qui élimine des doublons"""
# =================================================================
# lst = [9, 12, 40, 5, 12, 3, 27, 5, 9, 3, 8, 22, 40, 3, 2, 4, 6, 25]
# lst2 = []
#
# for el in lst:
#     if el not in lst2:
#         lst2.append(el)
# lst2.sort()
#
# print("liste initiale :", lst)
# print("Liste traitée :", lst2)

# =================================================================
"""Script qui affiche tous les jours d'une année"""
# =================================================================
"""Cette variante utilise une liste de listes (que l'on pourrait aisément
remplacer par deux listes distinctes)

La liste ci-dessous contient deux éléments qui sont eux-même des listes.
L'élément 0 contient les Nbre de jours de chaque mois, tandis que l'élément 1
contient les noms des douzes mois: """

# mois = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
#         'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']]
# jour = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'vendredi', 'Samedi']
# ja, jm, js, m = 0, 0, 0, 0
#
# while ja < 365:
#     ja, jm = ja +1, jm +1           # ja = jour dans l'année, jm = jour dans le mois
#     js = (ja + 3) % 7          # js = jour de la semaine. Le décalage ajouté permet de choisir le jour de départ
#
#     if jm > mois[0][m]:         # émlément m de élément 0 de la liste
#         jm, m = 1, m+1
#
#     print(jour[js], jm, mois[1][m])         # élément m de l'élément 1 de la liste
# =================================================================

# print(list(range(10)))
# print(list(range(5, 13)))
# print(list(range(3, 16, 3)))
# print(list(range(10, -10, -3)))

# prov = ['La', 'raison', 'du', 'plus', 'fort', 'est', 'toujours', 'la', 'meilleur']
# for mot in prov:
#     print(mot, end=' ')

# for n in range(10, 18, 3):
#     print(n, n**2, n**3)

# fable = ['Maître', 'Corbeau', 'sur', 'un', 'arbre', 'perché']
# for index in range(len(fable)):
#     print(index, fable[index], len(fable[index]))
#
# fruits = ['orange', 'citron']
# legumes = ['poireau', 'oignon', 'tomate']
# print(fruits+legumes)
# print(fruits*3)

# sept_zeros = [0]*7
# print(sept_zeros)

# ===================================================================
"""Insertion de nouveaux éléments dans une liste existante"""
# ===================================================================

# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
#       'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# c, d = 1, 0
# while d < 12:
#     t2[c:c] = [t1[d]]       # ! l'élément inséré doit être une liste
#     c, d = c+2, d+1
#
# print(t2)

# =================================================================
"""Crible d'eratosthène pour rechercher les nombres premiers de 1 à 999"""
# =================================================================

# Créer une liste de 1000 éléments de 1 (leurs indices vont de 0 à 999):
# lst = [1]*1000
# # Parcourir la liste à partir de l'élément d'indice 2:
# for i in range(2, 1000):
#     # Mettre à zero les éléments suivants dans la liste,
#     # dont les indices sont des multiples de i :
#     for j in range(i*2, 1000, i):
#         lst[j] = 0
#
# # Afficher les indices des éléments restés à 1 (on ignore l'élément 0) :
# for i in range(1, 1000):
#     if lst[i]:
#         print(i, end=' ')

# =================================================================


# def list_alea(n):
#     s = [0]*n
#     for i in range(n):
#         s[i] = random()
#     return s
#
#
# print(list_alea(3))
# =================================================================
"""Test du générateur de nombres aléatoires"""
# =================================================================

# n = input("Nombre de valeurs à tirer au hasard (defaut =1000 :")
# if n == "":
#     nVal = 1000
# else:
#     nVal = int(n)
# n = input("Nombre de fractions dans l'intervalle 0-1 (entre 2 et {0}, "\
#           "défaut=5) : ".format(nVal//10))
# if n == "":
#     nFra = 5
# else:
#     nFra = int(n)
# if nFra < 2:
#     nFra = 2
# elif nFra > nVal/10:
#     nFra = nVal/10
#
# print("Tirage au sort des", nVal, "valeurs ...")
# listVal = [0]*nVal                  # Créer une liste de zéros
# for i in range(nVal):               # puis modifier chaque élément
#     listVal[i] = random()
# print("Comptage des valeurs dans chacune des", nFra, "fractions ...")
# listCompt = [0]*nFra                # créer une liste de compteurs
#
# # parcourir la liste des valeurs :
# for valeur in listVal:
#     # trouver l'index de la fraction qui contient la valeur :
#     index = int(valeur*nFra)
#     # incrémenter le compteur correspondant :
#     listCompt[index] = listCompt[index] + 1
#
# # afficher l'état des compteurs :
# for compt in listCompt:
#     print(compt, end=' ')
# print()

# ================================================================

# for i in range(15):
#     print(randrange(3, 13, 3), end=' ')
#
# ================================================================
"""Script qui tire au hasard des cartes à jouer."""
# ================================================================

# couleurs = ['Pique', 'Trèfle', 'Carreau', 'Coeur']
# valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 'valet', 'dame', 'roi', 'as']
#
# # construction de la liste des 52 cartes :
# carte = []
# for coul in couleurs:
#     for val in valeurs:
#         carte.append("{0} de {1}".format(val, coul))
#
# # Tirage au hasard :
# while 1:
#     k = input("Frappez <c> pour tirer une carte, <Enter> pour terminer ")
#     if k == "":
#         break
#     r = randrange(52)       # tirage au hasard d'un entier entre 0 et 51
#     print(carte[r])
#

# =================================================================

# tup = 'a', 'b', 'c', 'd', 'e'
# # print(tup)
# tup = ('André',) + tup[1:]
# print(tup)

# tu1, tu2 = ("a", "b"), ("c", "d", "e")
# tu3 = tu1*4 + tu2
# # print(tu3)
# for e in tu3:
#     print(e, end=":")

# ===================================================================
dico = {}
dico['computer'] = 'ordinateur'
dico['mouse'] = 'souris'
dico['keyboard'] = 'clavier'
# print(dico)

invent = {'pommes': 430, 'bananes': 312, 'orange': 274, 'poires': 137}
# print(invent)
# del invent['pommes']
# print(invent)
# print(len(invent))
#
# if "pommes" in invent:
#     print("Nous avons des pommes")
# else:
#     print("Pas de pommes. Sorry")

# print(dico.keys())
# for k in dico.keys():
#     print("clé :", k, " --- Valeur :", dico[k])
# print(invent.values())
# print(invent.items())
# print(tuple(invent.items()))

# stock = invent
# # print(stock)
# del invent['bananes']
# del invent['orange']
# # print(stock)
#
# magasin = stock.copy()
# magasin['prunes'] = 561
# print(magasin)
# print(stock)
# print(invent)

# for clef in magasin:
#     print(clef, magasin[clef])

# for cle, valeur in magasin.items():
#     print(cle, valeur)

# arb = {}
# arb[(1,2)] = 'Peuplier'
# arb[(3,4)] = 'Platane'
# arb[6,7] = 'Palmier'
# arb[5,1] = 'Cycas'
# arb[7,3] = 'Sapin'
# # print(arb)
# print(arb.get((1,2), 'néant'))
# print(arb.get((2,1), 'néant'))

# ==================================================================
"""Création et consultation d'un dictionnaire"""
# ==================================================================

"""Mini système de bases de données"""

# def consultation():
#     while 1:
#         nom = input("Entrez le nom (ou <enter> pour terminer) :")
#         if nom == "":
#             break
#         if nom in dico:  # le nom est-il répertoire ?
#             item = dico[nom]  # consultation proprement dite
#             age, taille = item[0], item[1]
#             print("Nom : {0} - âge : {1} ans - taille : {2} m.". \
#                   format(nom, age, taille))
#         else:
#             print("*** nom inconnu ! ***")
#
#
# def remplissage():
#     while 1:
#         nom = input("Entrez le nom (ou <entrer> pour terminer) : ")
#         if nom == "":
#             break
#         age = int(input("Entrez l'âge (nombre entier !) : "))
#         taille = float(input("Entrez la taille (en mètres) :"))
#         dico[nom] = (age, taille)
#
#
# dico = {}
# while 1:
#     choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
#     if choix.upper() == 'T':
#         break
#     elif choix.upper() == 'R':
#         remplissage()
#     elif choix.upper() == 'C':
#         consultation()

# ===================================================================
"""Echange des clés et des valeurs dans un dictionnaire"""
# ===================================================================


# def inverse(dico):
#     "Construction d'un nouveau dico, pas à pas"
#     dic_inv = {}
#     for cle in dico:
#         item = dico[cle]
#         dic_inv[item] = cle
#     return dic_inv
#
# # Programme test :
#
#
# dico = {'Computer': 'Ordinateur',
#         'Mouse': 'Souris',
#         'Keyboard': 'Clavier',
#         'Hard disk': 'Disque dur',
#         'Screen': 'Ecran'}
#
# print(dico)
# print(inverse(dico))

# ==================================================================
# texte = "les saucisses et saucissons secs sont dans le saloir"
# lettre = {}
# for c in texte:
#     lettre[c] = lettre.get(c, 0) + 1
# # print(lettre)
#
# lettres_triees = list(lettre.items())
# lettres_triees.sort()
# # print(lettres_triees)

# =====================================================================
"""Histogramme des fréquences de chaque lettre dans un texte"""
# ===================================================================

# nFich = input('Nom du fichier (Latin-1) : ')
# fi = open(nFich, 'r', encoding="Latin1")
# texte = fi.read()
# fi.close()
#
# print(texte)
# dico = {}
# for c in texte:             # afin de les regrouper, on convertit
#     c = c.upper()           # toutes les lettres en majuscules
#     dico[c] = dico.get(c, 0) + 1
#
# liste = list(dico.items())
# liste.sort()
# for car, freq in liste:
#     print("Caractère {0} : {1} occurrence(s).".format(car, freq))
#
# ==================================================================
"""Histogramme des fréquences de chaque mot dans un texte Suivan l'encodage
du fichier source, activer l'une ou l'autre-ligne : """
# encodage = "Latin-1"
# # encodage = "Utf-8
#
# nFich = input('Nom du fichier à traiter ({0}) : '.format(encodage))
# # Conversition du fichier en une chaîne de caractères :
# fi = open(nFich, 'r', encoding=encodage)
# texte = fi.read()
# fi.close()
#
# # afin de pouvoir aisément séparer les mots du texte, on commence par
# # convertir tous les caractères non-alphabétiques en espaces :
# alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"
# lettres = ""            # nouvelle chaîne à construire
# for c in texte:
#     c = c.lower()       # conversion de chaque caractère en minuscule
#     if c in alpha:
#         lettres = lettres + c
#     else:
#         lettres = lettres + ' '
#
# # conversion de la chaîne résultante en une liste de mots :
# mots = lettres.split()
#
# # construction de l'histogramme :
# dico = {}
# for m in mots:
#     dico[m] = dico.get(m, 0) + 1
# liste = list(dico.items())
#
# # tri de la liste résultante :
# liste.sort()
# # affichage en clair :
# for item in liste:
#     print("{0} : {1}".format(item[0], item[1]))
# =================================================================
"""Encodage d'un texte dans un dictionnaire suivant l'encodage du fichier
source, activer l'une ou l'autre ligne : """
# encodage ="Latin-1"
# # encodage ="Utf-8"
#
# nFich = input('Nom du fichier à traiter ({0}) : '.format(encodage))
# # Conversion du fichier en une chaîne de caractères :
# fi = open(nFich, 'r', encoding =encodage)
# texte = fi.read()
# fi.close()
#
# # On considère que les mots sont des suites de caractères faisant partie
# # de la chaîne ci-dessous. Tous les autres sont des séparateurs :
# alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"
#
#
# # construction du dictionnaire :
# dico = {}
# # Parcours de tous les caractères du texte :
# i = 0               # indice du caractères en cours de lecture
# im = -1             # indice du premier caractère du mot
# mot = ""            # variable de travail : mot en cours de lecture
# for c in texte:
#     c = c.lower()   # conversion de chaque caractère en minuscule
#
#     if c in alpha:  # car. alphabétique => on est à l'intérieur d'un mot
#         mot = mot + c
#         if im < 0:  # mémoriser l'indice du premier caractère du mot
#             im = i
#     else:       # car. non-alphabetique => fin de mot
#         if mot != "":   # afin d'ignorer les car. non-alphab successifs
#             # pour chaque mot, on construit une liste d'indices :
#             if mot in dico:         # mot dèjà répertorié
#                 dico[mot].append(im)    # ajout d'un indice à la liste
#             else:                       # mot rencontré pour la 1er fois:
#                 dico[mot] = [im]        # création de la liste d'indices
#             mot = ""        # préparer la lecture du mot suivant
#             im = -1
#     i += 1                  # indice du caractère suivant
#
#
# # Affichage du dictionnaire, en claire :
# listeMots = list(dico.items())          # conversion du dico en une liste de tuples
# listeMots.sort()                        # tri alphabétique de la liste
# for clef, valeur in listeMots:
#     print(clef, ":", valeur)

# ===================================================================
"""Mini-système de base de données"""
# ===================================================================


# def consultation():
#     while 1:
#         nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#         if nom == "":
#             break
#         if nom in dico:  # le nom est-il répertorié ?
#             item = dico[nom]  # consultation proprement dite
#             age, taille = item[0], item[1]
#             print("Nom : {0} - âge : {1} ans - taille : {2} m.".\
#                   format(nom, age, taille))
#         else:
#             print("*** nom inconnu ! ***")
#
#
# def remplissage():
#     while 1:
#         nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#         if nom == "":
#             break
#         age = int(input("Entrez l'âge (nombre entier !) : "))
#         taille = float(input("Entrez la taille (en mètres) : "))
#         dico[nom] = (age, taille)
#
#
# def enregistrement():
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     ofi = open(fich, "w")
#     # écriture d'une ligne-repère pour identifier le type de fichier :
#     ofi.write("DicoExercice10.50\n")
#     # parcours du dictionnaire entier, converti au préalable en une liste :
#     for cle, valeur in list(dico.items()):
#         # utilisation du formatage des chaînes pour créer l'enregistrement :
#         ofi.write("{0}@{1}#{2}\n".format(cle, valeur[0], valeur[1]))
#     ofi.close()
#
#
# def lectureFichier():
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     try:
#         ofi = open(fich, "r")
#     except:
#         print("*** fichier inexistant ***")
#     return
#     # Vérification : le fichier est-il bien de notre type spécifique ? :
#     repere =ofi.readline()
#     if repere != "DicoExercice10.50\n":
#         print("*** type de fichier incorrect ***")
#         return
#     # Lecture des lignes restantes du fichier :
#     while 1:
#         ligne = ofi.readline()
#         if ligne =='': # détection de la fin de fichier
#             break
#         enreg = ligne.split("@") # restitution d'une liste [clé,valeur]
#         cle = enreg[0]
#         valeur = enreg[1][:-1] # élimination du caractère de fin de ligne
#         data = valeur.split("#") # restitution d'une liste [âge, taille]
#         age, taille = int(data[0]), float(data[1])
#         dico[cle] = (age, taille) # reconstitution du dictionnaire
#     ofi.close()
#
#
# ######## * Programme principal * #########
# dico ={}
# lectureFichier()
# while 1:
#     choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
#     if choix.upper() == 'T':
#         break
#     elif choix.upper() == 'R':
#         remplissage()
#     elif choix.upper() == 'C':
#         consultation()
# enregistrement()

# ===================================================================
"""Contrôle du flux d'exécution à l'aide d'un dictionnaire"""
# ===================================================================

# def consultation():
#     while 1:
#         nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#         if nom == "":
#             break
#         if nom in dico:  # le nom est-il répertorié ?
#             item = dico[nom]  # consultation proprement dite
#             age, taille = item[0], item[1]
#             print("Nom : {0} - âge : {1} ans - taille : {2} m.".\
#                   format(nom, age, taille))
#         else:
#             print("*** nom inconnu ! ***")
#
#
# def remplissage():
#     while 1:
#         nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#         if nom == "":
#             break
#         age = int(input("Entrez l'âge (nombre entier !) : "))
#         taille = float(input("Entrez la taille (en mètres) : "))
#         dico[nom] = (age, taille)
#
#
# def enregistrement():
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     ofi = open(fich, "w")
#     # écriture d'une ligne-repère pour identifier le type de fichier :
#     ofi.write("DicoExercice10.50\n")
#     # parcours du dictionnaire entier, converti au préalable en une liste :
#     for cle, valeur in list(dico.items()):
#         # utilisation du formatage des chaînes pour créer l'enregistrement :
#         ofi.write("{0}@{1}#{2}\n".format(cle, valeur[0], valeur[1]))
#     ofi.close()
#
#
# def lectureFichier():
#     fich = input("Entrez le nom du fichier de sauvegarde : ")
#     try:
#         ofi = open(fich, "r")
#     except:
#         print("*** fichier inexistant ***")
#     return
#     # Vérification : le fichier est-il bien de notre type spécifique ? :
#     repere =ofi.readline()
#     if repere != "DicoExercice10.50\n":
#         print("*** type de fichier incorrect ***")
#         return
#     # Lecture des lignes restantes du fichier :
#     while 1:
#         ligne = ofi.readline()
#         if ligne =='': # détection de la fin de fichier
#             break
#         enreg = ligne.split("@") # restitution d'une liste [clé,valeur]
#         cle = enreg[0]
#         valeur = enreg[1][:-1] # élimination du caractère de fin de ligne
#         data = valeur.split("#") # restitution d'une liste [âge, taille]
#         age, taille = int(data[0]), float(data[1])
#         dico[cle] = (age, taille) # reconstitution du dictionnaire
#     ofi.close()
#
#
# def sortie():
#     print("*** Job terminé ***")
#     return 1        # afin de provoquer la sortie de la boucle
#
#
# def autre():
#     print("Veuillez frapper R, A, C, S ou T, svp.")
#
#
# ######## * Programme principal * #########
# dico ={}
# fonc ={"R":lectureFichier, "A":remplissage, "C":consultation,
#  "S":enregistrement, "T":sortie}
# while 1:
#     choix = input("Choisissez :\n" + \
#                   "(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier\n" + \
#                   "(A)jouter des données au dictionnaire courant\n" + \
#                   "(C)onsulter le dictionnaire courant\n" + \
#                   "(S)auvegarder le dictionnaire courant dans un fichier\n" + \
#                   "(T)erminer : ").upper()
#     # l'instruction ci-dessous appelle une fonction différente pour chaque
#     # choix, par l'intermédiaire du dictionnaire <fonc> :
#     if fonc.get(choix, autre)():
#         break
#     # note : toutes les fonctions appelées ici renvoient <None> par défaut
#     # sauf la fonction sortie() qui renvoie 1 => sortie de la boucle
