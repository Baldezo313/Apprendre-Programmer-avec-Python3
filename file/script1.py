# -*- coding:Utf8 -*-

##########################################
# Programme en Python                    #
# Author : M. S. Baldezo313              #
# Licence:   GPL                         #
##########################################

from tkinter import *

"""
Suite de Fibonacci
Afficher les dix premiers termes de cette suite;
Il s'agit d'une suite de nombres dont chaque terme est égale à la somme des deux
termes qui le précèdent.
"""

a, b, c = 1, 1, 1
while c < 11:
    print(b, end=" ")
    a, b, c = b, a+b, c+1
print("\n")
a1 = 7
b1 = 1
while b1 < 10:
    print(a1*b1, end=" ")
    b1 = b1 + 1

print("\n")

# =====================================================================
"""
Affichage des 20 premiers termes de la table par 7, avec un signalement des multiples de 3
"""
i = 1
while i < 21:
    # calcul du terme à afficher:
    t = i * 7
    # Affichage sans saut à la ligne (utilisation de la virgule)
    print(t, end=' ')
    # ce terme est-il multiple de 3 ? (utilisation de modulo):
    if t % 3 == 0:
        print("*", end=' ')    # affichage d'une asterisque dans ce cas
    i = i + 1                  # incrémentation du compteur dans tous les cas

print("\n")

"""
Affichage des multiple de 7 pour les 50 premiers termes de la table par 13
"""
i = 1
while i < 51:
    # calcul du terme à afficher:
    t = i * 13

    # ce terme est-il multiple de 7 ? (utilisation de modulo):
    if t % 7 == 0:
        print(t, end=' ')
    i = i + 1

print("\n")

# =============================================================
"""
Recherche d'un caractère particulier dans une chaîne
"""
# chaine fournie au depart:
ch = "Monty python flying circus"
# caractere rechercher :
cr = "e"
# recherche propement dite:
lc = len(ch)       # nbr de caractere à tester
i = 0              # indice du caractere en cours d'examen
t = 0             # "drapeau" à lever si le caractere recherché est présent
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1
print("Le caractère", cr, end=' ')
if t == 1:
    print("est present", end=' ')
else:
    print("est introuvable", end=' ')
print("dans la chaine", ch)
print("\n")
# =================================================
""" Insertion d'une caractere d'espacement dans une chaine"""

# chaine fournie au depart
ch = "Baldezobaldeba"
# Caractere à inserer
cr = "*"
"""
le nbr de caractere à inserer est inférieur d'une unité au nbr de caractère de la chaine
"""
lc = len(ch)    # nbr de caractère total
i = 1           # indice du premiere caractere à examiner
nch = ch[0]     # nvl chaine à construire (contient déja le premier)
while i < lc:
    nch = nch + cr + ch[i]
    i = i + 1
# Affichage:
print(nch)

print("\n")

# ==================================================================
"""Inversion d'une chaine de caractère"""

# chaine fourni au depart:
ch = "tsitneics"
lc = len(ch)        # nbr de caractère total
i = lc - 1          # le traitement commencera à partir du dernier caractere
nch = ""            # nvl chaine à construire (vide au depart)
while i >= 0:
    nch = nch + ch[i]
    i = i - 1
# Affichage
print(nch)

print("\n")

# =========================================================
""" Combinaison de deux listes en une seule """

# Liste fournies au depart:
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Main', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
# Nvl liste à costruire (vide au départ)
t3 = []
# Boucle de traitement:
i = 0
while i < len(t1):
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1
# Affichage
print(t3)

print("\n")
# =================================================================
""" Affichage de tous les élements d'une  liste """
# Liste fournie au depart:
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Main', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
# Affichage
i = 0
while i < len(t2):
    print(t2[i], end=' ')
    i += 1

print("\n")
# =================================================================
"""Recherche du plus grand elément d'une liste"""

# liste fournie au depart
tt = [32, 5, 12, 8, 3, 75, 2, 15]
max = 0
# examen de tous les éléments :
i = 0
while i < len(tt):
    if tt[i] > max:
        max = tt[i]             # mémorisation d'une nveau maximum
    i += 1
# Affichage:
print("Le plus grand élément de cette liste a la valeur", max)

print("\n")
# =================================================================
"""Séparation des nombres pairs et impairs"""
tt = [32, 5, 12, 8, 3, 75, 2, 15]
pairs = []
impairs = []
# Examen de tous les elements :
i = 0
while i < len(tt):
    if tt[i] % 2 == 0:
        pairs.append(tt[i])
    else:
        impairs.append(tt[i])
    i += 1
# Affichage:
print("Nombres pairs :", pairs)
print("Nombres impairs ", impairs)

print("\n")
# =================================================================
""" Séparation par le nombre de caractère """
# Liste d'entrée
Name = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
Namesup6 = []
Nameinf6 = []
i = 0
while i < len(Name):
    if len(Name[i]) >= 6:
        Namesup6.append(Name[i])
    else:
        Nameinf6.append(Name[i])
    i += 1
# Affichage
print("Mots comportant plus de 6 lettres:", Namesup6)
print("Mots comportant moins de 6 lettre :", Nameinf6)

print("\n")
# =================================================================
""" Entrée d'éléments dans une liste """
# tt = []             # Liste à compléter (vide au depart)
# ch = "start"        # valeur quelconque (mais non nulle)
# while ch != "":
#     print("Veuillez entrer une valeur : ")
#     ch = input()
#     if ch != "":
#         tt.append(float(ch))        # variante: tt.append(ch)
#
# # Affichage de la liste:
# print(tt)
#
# print("\n")
# =================================================================
""" Bibliotheque turtle """

# from turtle import *
#
# reset()
# a = 0
# while a < 12:
#     a += 1
#     forward(150)
#     left(150)

print("\n")
# =================================================================
""""""
# print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end=' ')
# ch = input()
# a = int(ch)
# while a:            # équivalent à : < while a != 0: >
#     if a == 1:
#         print("Vous avez choisi un :")
#         print("le premier, l'unique, l'unité ...")
#     elif a == 2:
#         print("Vous préférez le deux :")
#         print("la paire, le couple, le duo ...")
#     elif a == 3:
#         print("Vous optez pour le plus grand des trois :")
#         print("le trio, la trinité, le triplet ...")
#     else:
#         print("Un nombre entre UN et TROIS, s.v.p.")
#     print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end=' ')
#     a = int(input())
# print("Vous avez entré zéro :")
# print("L'exercice est donc terminé.")


print("\n")
# =================================================================
""" Traitement de nombres entiers compris entre deux limites """
# print("Veuillez entrer la limite inférieur:", end=' ')
# a = eval(input())
# print("Veuillez entrer la limite superieur :", end=' ')
# b = eval(input())
# s = 0
# # parcours de la série des nbre compris entre a et b:
# n = a           # nbr en cours de traitement
# while n <= b:
#     if n % 3 == 0 and n % 5 == 0:
#         s += n
#     n += 1
# print("La somme recherchée vaut", s)


print("\n")
# =================================================================
# """ Année bissextiles """
# print("Veuillez entrer l'année à tester:", end=' ')
# a = eval(input())
#
# if a % 4 != 0:
#     # a n'est pas divisible par 4 -> année non bissextile
#     bs = 0
# else:
#     if a % 400 == 0:
#         # a divisible par 400 -> année bissextile
#         bs = 1
#     elif a % 100 == 0:
#         # a divisible par 100 -> année non bissextile
#         bs = 0
#     else:
#         # autre cas ou a est divisible par 4 -> année bisextille
#         bs = 1
# if bs == 1:
#     ch = "est"
# else:
#     ch = "n'est pas"
# print("L'année", a, ch, "bissextille.")

""" Autre méthode """
# a = eval(input('Veuillez entrer une année :'))
#
# if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
#     print(a, "est une année bissextile")
# else:
#     print(a, "n'est pas une année bissextile")


print("\n")
# =================================================================
""" Notes de travaux scolaires """

# notes = []          # liste à construire
# n = 2               # valeur positive quelconque pour initier la boucle
# while n >= 0:
#     print("Entrez la note suivante, s.v.p. : ", end=' ')
#     n = float(input())              # conversion de l'entrée en un nombre réel
#     if n < 0:
#         print("OK. Terminé.")
#     else:
#         notes.append(n)         # ajout d'une note à la liste
#         # Calculs divers sur les notes dèja entrées :
#         # valeurs minimale et maximale + total de toutes les notes.
#         min = 500           # valeur supérieur à toute note
#         max, tot, i = 0, 0, 0
#         nn = len(notes)             # nbr de notes dèjà entrées
#         while i < nn:
#             if notes[i] > max:
#                 max = notes[i]
#             if notes[i] < min:
#                 min = notes[i]
#             tot = tot + notes[i]
#             moy = tot/nn
#             i += 1
#         print(nn, "notes entrées. Max =", max, "Min =", min, "Moy =", moy)


print("\n")
# =================================================================
""" Table 7 """


def table7():
    n = 1
    while n < 11:
        print(n * 7, end=' ')
        n += 1


print(table7())

print("\n")
# =================================================================
""" Table 7 à trois fois """


def table7triple():
    print('La table par 7 en triple exemplaire :')
    print(table7())
    print(table7())
    print(table7())


print(table7triple())

print("\n")
# =================================================================
""" Table de multiplication """


def table(base):
    n = 1
    while n < 11:
        print(n * base, end=' ')
        n += 1


print(table(13))
print(table(9))

a = 1
while a < 20:
    print(table(a))
    a += 1

print("\n")
# =================================================================
""" Table de multiplication plusplus """


def tableMulti(base, debut, fin):
    print('Fragment de la table de multiplication par', base, ':')
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n * base)
        n += 1


print(tableMulti(8, 13, 17))

t, d, f = 11, 5, 10
while t < 12:
    print(tableMulti(t, d, f))
    t, d, f = t + 1, d + 3, f + 5


print("\n")
# =================================================================
""" Fonction avec return """


def table(base):
    resultat = []           # resultat est d'abord une liste vide
    n = 1
    while n < 11:
        b = n * base
        resultat.append(b)      # ajout d'une terme à la liste
        n += 1
    return resultat


tab9 = table(9)
print(tab9)
print(tab9[0])
print(tab9[2:5])


print("\n")
# =================================================================
""" volume d'un sphère """


def cube(n):
    return n**3


def volumSphere(r):
    return 4*3.1416*cube(r) / 3


# r = input('Entrer la valeur du rayon : ')
# print('Le volume de cette sphère vaut', volumSphere(float(r)))

print("\n")
# =================================================================


def essai():
    "Cette fonction est bien documentée mais ne fait presque rien."
    print("rien a signaler")


print(essai())
print(essai.__doc__)

print("\n")
# =================================================================
""" Utilisation de module """


# from dessins_tortue import *
#
# up()        # relever le crayon
# goto(-150, 50)      # reculer en haut à gauche
#
# # dessiner dix carrés rouges, alignés
# i = 0
# while i < 10:
#     down()          # abaisser le crayon
#     carre(25, 'red')                # tracer un carré
#     up()                            # relever le crayon
#     forward(30)                     # avancer + loin
#     i += 1
# a = input()                         # attendre

print("\n")
# =================================================================
""" Maximume de trois elements """


def maximum(n1, n2, n3):
    "Renvoie le plus grand de trois nombres"
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


# test :
print(maximum(4.5, 5.7, 3.9))
print(maximum(8.2, 2.1, 6.7))
print(maximum(1.3, 4.8, 7.6))

print("\n")
# =================================================================
""" obtenir le nbr de caractère dans une phrase """


def compterCar(ca, ch):
    "Renvoie le nbr de caractère ca trouvés dans la chaîne ch"
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot += 1
        i += 1
    return tot


# test
print(compterCar("e", "Cette chaîne est un exemple"))

print("\n")
# =================================================================


def indexMax(tt):
    "renvoie l'indice du plus grand élément de la liste tt"
    i, max = 0, 0
    while i < len(tt):
        if tt[i] > max:
            max, imax = tt[i], i
        i += 1
    return imax


# test:
serie = [5, 8, 2, 1, 9, 3, 6, 4]
print(indexMax(serie))

print("\n")
# =================================================================


def nomMois(n):
    "renvoie le nom du n-ième mois de l'année"
    mois = ['Janvier,', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
            'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return mois[n -1] # les indices sont numérotés à partir de zéro


# test :
print(nomMois(4))


print("\n")
# =================================================================


def afficher3fois(arg):
    print(arg, arg, arg)


print(afficher3fois(5))
print(afficher3fois('zut'))
print(afficher3fois([5, 7]))

print("\n")
# =================================================================


def politesse(nom, vedette='Monsieur'):
    print("Veuillez agrée ,", vedette, nom, ", mes salutations cordiales.")


print(politesse('Dupont'))
print(politesse('Durant', 'Mademoiselle'))

print("\n")
# =================================================================


def question(annonce, essais=4, please='Oui ou non, s.v.p.!'):
    while essais > 0:
        reponse = input(annonce)
        if reponse in ('o', 'oui', 'Oui', 'OUI'):
            return 1
        if reponse in ('n', 'non', 'N', 'Non', 'NON'):
            return 0
        print(please)
        essais -= 1


# rep = question('Voulez-vous vraiment terminer ? ')
# # print(rep)
# rep = question('Faut-il effacer ce fichier ? ', 3)
# # print(rep)
# rep = question('Avez-vous compris ? ', 2, 'Repondez par oui ou par non !')
# # print(rep)

print("\n")
# =================================================================

""" Changement de caractère dans une phrase """


def changeCar(ch, ca1, ca2, debut = 0, fin = -1):
    "Remplace tous les caractères ca1 par des ca2 dans la chaîne ch"
    if fin == -1:
        fin = len(ch)
    nch, i = "", 0          # nch : nouvelle chaîne à construire
    while i < len(ch):
        if debut <= i <= fin and ch[i] == ca1:
            nch = nch + ca2
        else:
            nch = nch + ch[i]
        i += 1
    return nch


# test :
print((changeCar("Ceci est une toute petite phrase", " ", "*")))
print((changeCar("Ceci est une toute petite phrase", " ", "*", 8, 12)))
print((changeCar("Ceci est une toute petite phrase", " ", "*", 8)))
print((changeCar("Ceci est une toute petite phrase", " ", "*", fin=12)))


print("\n")
# =================================================================
""" Renvoie la plus grand élément de la liste"""


def eleMax(lst, debut=0, fin=-1):
    "renvoie le plus grand élément de la liste lst"
    if fin == -1:
        fin = len(lst)
    max, i = 0, 0
    while i < len(lst):
        if debut <= i <= fin and lst[i] > max:
            max = lst[i]
        i += 1
    return max


# test :
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, fin=3, debut=1))

print("\n")
# =================================================================
""" Renvoie la plus grand élément de la liste"""




