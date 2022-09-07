from math import *
from random import *
from carte import JeuDeCartes


class Point(object):
    "Définition d'un point géométrique"


# p9 = Point()
# # print(p9)
# # print(p9.__doc__)
# p9.x = 3.0
# p9.y = 4.0
# # print(p9.x**2 + p9.y**2)
#
#
# def affichage_point(p):
#     print("coord. horizontale =", p.x, "coord. verticale =", p.y)


# print(affichage_point(p9))

# ===================================================================
"""FCT qui permet de calculer la distance entre deux points"""

# ===================================================================


# def distance(p1, p2):
#     # On applique le théorème de Pythagore :
#     dx = abs(p1.x - p2.x)               # abs() => valeur absolue
#     dy = abs(p1.y - p2.y)
#     return sqrt(dx*dx + dy*dy)
#
#
# def affichage_point(p):
#     print("Coord. Horiz.", p.x, "Coord. vert.", p.y)
#
#
# class Point(object):
#     "Class de points géométriques"
#
#
# p8, p9 = Point(), Point()
# p8.x, p8.y, p9.x, p9.y = 12.3, 5.7, 6.2, 9.1
#
# print(affichage_point(p8))
# print(affichage_point(p9))
# print("Distance =", distance(p8, p9))

# =============================================================


# class Rectangle(object):
#     "définition d'une classe de rectangles"
#
#
# boite = Rectangle()
# boite.largeur = 50.0
# boite.hauteur = 35.0
#
# boite.coin = Point()
# boite.coin.x = 12.0
# boite.coin.y = 27.0
#
#
# def trouveCentre(box):
#     p = Point()
#     p.x = box.coin.x + box.largeur/2.0
#     p.y = box.coin.y + box.hauteur/2.0
#     return p
#
#
# centre = trouveCentre(boite)
# # print(centre.x, centre.y)
#
# boite.hauteur = boite.hauteur + 20
# boite.largeur = boite.largeur - 5
# ===================================================================


# class Time(object):
#     "définition d'objets temporels"
#
#
# instant = Time()
# instant.heure = 11
# instant.minute = 34
# instant.seconde = 25
#
#
# def affichage_heure(t):
#     print(str(t.heure) + ":" + str(t.minute) + ":" + str(t.seconde))
#
#
# print(affichage_heure(instant))


# class Time(object):
#     "Nouvelle classe temporelle"
#
#     def affichage_heure(t):
#         print("{0}:{1}:{2}".format(t.heure, t.minute, t.seconde))

# class Time(object):
#     "Nouvelle classe temporelle"
#
#     def affichage_heure(self):
#         print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
#
#
# maintenant = Time()
# maintenant.heure = 13
# maintenant.minute = 34
# maintenant.seconde = 21
# print(maintenant.affichage_heure())


# class Time(object):
#     "Encore une nouvelle classe temporelle"
#
#     def __init__(self, hh=12, mm=0, ss=0):
#         self.heure = hh
#         self.minute = mm
#         self.seconde = ss
#
#     def affichage_heure(self):
#         print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
#
#
# # tstart = Time(10, 15, 18)
# # tstart = Time(10, 30)
# tstart = Time(hh=18)
# print(tstart.affichage_heure())
# ====================================================================
"""CLASS qui permette d'instancier des objets simulant les pièces d'un jeu de dominos"""
# ====================================================================


# class Domino(object):
#     def __init__(self, pa, pb):
#         self.pa, self.pb = pa, pb
#
#     def affiche_points(self):
#         print("face A :", self.pa)
#         print("face B :", self.pb)
#
#     def valeur(self):
#         return self.pa + self.pb
#
#
# # Programme de test :
# d1 = Domino(2, 6)
# d2 = Domino(4, 3)
#
# print(d1.affiche_points())
# print(d2.affiche_points())
#
# print("Total des points :", d1.valeur() + d2.valeur())
#
# liste_dominos = []
# for i in range(7):
#     liste_dominos.append(Domino(6, i))
#
# vt = 0
# for i in range(7):
#     liste_dominos[i].affiche_points()
#     vt = vt + liste_dominos[i].valeur()
#
# print("Valeur total des points", vt)
# print(liste_dominos[3], liste_dominos[4])
# ====================================================================
"""CLASS qui permette d'instancier des objets de Compte Bancaires"""
# ====================================================================


# class CompteBancaire(object):
#     def __init__(self, nom='Baldezo', solde=1000):
#         self.nom, self.solde = nom, solde
#
#     def depot(self, somme):
#         self.solde = self.solde + somme
#
#     def retrait(self, somme):
#         self.solde = self.solde - somme
#
#     def affichage(self):
#         print("Le solde du compte bancaire de {0} est de {1} euros".\
#               format(self.nom, self.solde))
#
#
# # Programme de test :
#
# if __name__ == '__main__':
#     c1 = CompteBancaire('Baldezo', 800)
#     c1.depot(350)
#     c1.retrait(200)
#     c1.affichage()
#     c2 = CompteBancaire()
#     c2.depot(25)
#     c2.affichage()
# ====================================================================
"""CLASS qui permette d'instancier des objets reproduisant le comportement
de voitures automobiles."""
# ====================================================================


# class Voiture(object):
#     def __init__(self, marque='Ford', couleur='rouge'):
#         self.couleur = couleur
#         self.marque = marque
#         self.pilote = 'personne'
#         self.vitesse = 0
#
#     def accelerer(self, taux, duree):
#         if self.pilote == 'personne':
#             print("Cette voiture n'a pas de conducteur !")
#         else:
#             self.vitesse = self.vitesse + taux*duree
#
#     def choix_conducteur(self, nom):
#         self.pilote = nom
#
#     def affichage_tout(self):
#         print("{0} {1} pilotée par {2}, vitesse = {3} m/s".\
#               format(self.marque, self.couleur, self.pilote, self.vitesse))
#
#
# a1 = Voiture('Peugeot', 'bleue')
# a2 = Voiture(couleur='verte')
# a3 = Voiture('Mercedes')
# a1.choix_conducteur('Chaimae')
# a2.choix_conducteur('Baldezo')
# a2.accelerer(1.8, 12)
# a1.accelerer(1.9, 11)
# a2.affichage_tout()
# a1.affichage_tout()
# a3.affichage_tout()
# ====================================================================
"""CLASS qui permette d'instancier des objets simulant des satellites
artificiels lancés dans l'espace, autour de la terre."""
# ====================================================================


# class Satellite(object):
#     def __init__(self, nom, masse=100, vitesse=0):
#         self.nom, self.masse, self.vitesse = nom, masse, vitesse
#
#     def impulsion(self, force, duree):
#         self.vitesse = self.vitesse + force*duree / self.masse
#
#     def energie(self):
#         return self.masse * self.vitesse**2 / 2
#
#     def affichage_vitesse(self):
#         print("Vitesse du sattelite {0} = {1} m/s".\
#               format(self.nom, self.vitesse))
#
#
# # Programme de Test :
# s1 = Satellite('Baldezo', masse=250, vitesse=10)
# s1.impulsion(500, 15)
# s1.affichage_vitesse()
# print("énérgie =", s1.energie())
# s1.impulsion(500, 15)
# s1.affichage_vitesse()
# print("Nouvelle énérgie =", s1.energie())
# ====================================================================


# class Espaces(object):
#     aa = 33
#
#     def affiche(self):
#         print(aa, Espaces.aa, self.aa)
#
# aa = 12
# essai = Espaces()
# essai.aa = 67
# # essai.affiche()
#
# print(aa, Espaces.aa, essai.aa)
# ===================================================================


# class Mammifere(object):
#     caract1 = "il allaite ses petits ;"
#
#
# class Carnivore(Mammifere):
#     caract2 = "il se nourrit de la chair de ses proies ;"
#
#
# class Chien(Carnivore):
#     caract3 = "Son cri s'appelle aboiement ;"
#
#
# mirza = Chien()
# print(mirza.caract1, mirza.caract2, mirza.caract3)
# ==================================================================


# class Atome:
#     """atomes simplifiés, choisis parmi les 10 premiers éléments du TP"""
#     table = [None, ('hydrogène', 0), ('hélium', 2), ('lithium', 4),
#              ('béryllium', 5), ('bore', 6), ('carbone', 6), ('azote', 7),
#              ('oxygène', 8), ('fluor', 9), ('néon', 10)]
#
#     def __init__(self, nat):
#         "le n° atomique détermine le n. de protons, d'électrons et de neutrons"
#         self.np, self.ne = nat, nat
#         self.nn = Atome.table[nat][1]
#
#     def affiche(self):
#         print()
#         print("Nom de l'élément :", Atome.table[self.np][0])
#         print("{0} protons, {1} électrons, {2} neutrons".\
#               format(self.np, self.ne, self.nn))
#
#
# class Ion(Atome):
#     """Les ions sont des atomes qui ont gagné ou perdu des électrons"""
#
#     def __init__(self, nat, charge):
#         "Le n° atomique et la charge éléctrique détermine l'ion"
#         Atome.__init__(self, nat)
#         self.ne = self.ne -charge
#         self.charge = charge
#
#     def affiche(self):
#         Atome.affiche(self)
#         print("Particule électrisée. Charge =", self.charge)
#
#
# ### Programme principal : ####
#
# a1 = Atome(5)
# a2 = Ion(3, 1)
# a3 = Ion(8, -2)
# a1.affiche()
# a2.affiche()
# a3.affiche()

##########################################################
# Programme Python type                                  #
# Auteur : M.S Baldezo                                   #
# Licence : GPL                                          #
##########################################################


# class Point(object):
#     """point géométrique"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Rectangle(object):
#     """rectangle"""
#     def __init__(self, ang, lar, hau):
#         self.ang = ang
#         self.lar = lar
#         self.hau = hau
#
#     def trouveCentre(self):
#         xc = self.ang.x + self.lar / 2
#         yc = self.ang.y + self.hau / 2
#         return Point(xc, yc)
#
#
# class Carre(Rectangle):
#     """carré = rectangle particulier"""
#     def __init__(self, coin, cote):
#         Rectangle.__init__(self, coin, cote, cote)
#         self.cote = cote
#
#     def surface(self):
#         return self.cote**2
#
#
# #############################################
# # Programme principale : ##
#
# # coord. de 2 coins sup. gauches :
# CsgR = Point(40, 30)
# CsgC = Point(10, 25)
#
# # "Boites" rectangulaire et carrée :
# boiteR = Rectangle(CsgR, 100, 50)
# boiteC = Carre(CsgC, 40)
#
# # Coordonnées du centre pour chacune :
# cR = boiteR.trouveCentre()
# cC = boiteC.trouveCentre()
#
# print("centre du rect. :", cR.x, cR.y)
# print("centre du carré :", cC.x, cC.y)
#
# print("surf. du carré :", end=' ')
# print(boiteC.surface())
# ====================================================================
"""CLASS de cylindres et de cônes"""

# # ====================================================================
# # Classes dérivées - Polymorphisme
#
#
# class Cercle(object):
#     def __init__(self, rayon):
#         self.rayon = rayon
#
#     def surface(self):
#         return 3.1416 * self.rayon ** 2
#
#
# class Cylindre(Cercle):
#     def __init__(self, rayon, hauteur):
#         Cercle.__init__(self, rayon)
#         self.hauteur = hauteur
#
#     def volume(self):
#         return self.surface() * self.hauteur
#
#     # La méthode surface() est héritée de la classe parente
#
#
# class Cone(Cylindre):
#     def __init__(self, rayon, hauteur):
#         Cylindre.__init__(self, rayon, hauteur)
#
#     def volume(self):
#         return Cylindre.volume(self) / 3
#         # cette nouvelle méthode volume() remplace celle qque l'on a
#         # héritée de la classe parente (exemple de polymorphisme)
#
#
# # Programme test :
#
# cyl = Cylindre(5, 7)
# print("Surf. de section du cylindre =", cyl.surface())
# print("Volume du cylindre =", cyl.volume())
#
# co = Cone(5, 7)
# print("Surf. de base du cône =", co.surface())
# print("Volume du cône =", co.volume())
# ====================================================================
"""CLASS permettant d'instancier des objets dont le comportement soit similaire
à celui d'un vrai jeu de carte"""


# ====================================================================

# Tirage de cartes

#
# class JeuDeCartes(object):
#     """Jeu de cartes"""
#     # attributs de classe (communs à toutes les instances) :
#     couleur = ('Pique', 'Trèfle', 'Carreau', 'Coeur')
#     valeur = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as')
#
#     def __init__(self):
#         "Construction de la liste des 52 cartes"
#         self.carte = []
#         for coul in range(4):
#             for val in range(13):
#                 self.carte.append((val + 2, coul))  # la valeur commence à 2
#
#     def nom_carte(self, c):
#         "Renvoi du nom de la carte c, en clair"
#         return "{0} de {1}".format(self.valeur[c[0]], self.couleur[c[1]])
#
#     def battre(self):
#         "Mélange des cartes"
#         t = len(self.carte)  # nbr de cartes restantes
#         # pour mélanger, on procède à un nbr d'échanges équivalent :
#         for i in range(t):
#             # tirage au hasard de 2 emplacements dans la liste :
#             h1, h2 = randrange(t), randrange(t)
#             # échange des cartes situées à ces emplacements :
#             self.carte[h1], self.carte[h2] = self.carte[h2], self.carte[h1]
#
#     def tirer(self):
#         "Tirage de la première carte de la pile"
#         t = len(self.carte)  # vérifie qu'il reste des cartes
#         if t > 0:
#             carte = self.carte[0]  # choisir la première carte du jeu
#             del (self.carte[0])  # la retirer du jeu
#             return carte  # en renvoyer copie au prog. appelant
#         else:
#             return None  # facultatif
#
#
# # ## Programme test :
#
# if __name__ == '__main__':
#     jeu = JeuDeCartes()  # instanciation d'un objet
#     jeu.battre()  # mélange des cartes
#     for n in range(53):  # tirage des 52 cartes
#         c = jeu.tirer()
#         if c == None:  # il ne reste aucune carte
#             print('Terminé !')  # dans la liste
#         else:
#             print(jeu.nom_carte(c))     # valeur et couleur de la carte
# ====================================================================
"""Bataille de la carte"""
# ====================================================================

jeuA = JeuDeCartes()                # instanciation du premier jeu
jeuB = JeuDeCartes()                # instanciation du second jeu
jeuA.battre()                       # mélange de chacun
jeuB.battre()
pA, pB = 0, 0                       # compteurs de points des joueurs A et B

# tirer 52 fois une carte de chaque jeu :
for n in range(52):
    cA, cB = jeuA.tirer(), jeuB.tirer()
    vA, vB = cA[0], cB[0]               # valeurs de ces cartes
    if vA > vB:
        pA += 1
    elif vB > vA:
        pB += 1                 # (rien ne se passe si vA = vB)
    # affichage des points successifs et des cartes tirées :
    print("{0} * {1} ==> {2} * {3}".format(jeuA.nom_carte(cA),
                                           jeuB.nom_carte(cB), pA, pB))
print("le joueur A obtient {0} pts, le joueur B en obtient {1}.".format(pA, pB))