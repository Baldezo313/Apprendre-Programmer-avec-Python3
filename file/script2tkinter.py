# -*- coding:Utf8 -*-

##########################################
# Programme en Python                    #
# Author : M. S. Baldezo313              #
# Licence:   GPL                         #
##########################################

from tkinter import *
from random import randrange
from math import *

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# fen1 = Tk()
# tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
# tex1.pack()
# bou1 = Button(fen1, text='Quitter', command=fen1.destroy)
# bou1.pack()
# fen1.mainloop()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""Petit exo utilisant la bibliothèque graphique tkinter """

# --- définition des fonctions gestionnaires d'événements : ----


# def drawline():
#     "Tracé d'une ligne dans le canevas can1"
#     global x1, y1, x2, y2, coul
#     can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
#
#     # modification des coordonnées pour la ligne suivante :
#     y2, y1 = y2 + 10, y1 - 10
#
#
# def changecolor():
#     "Changement aléatoire de la couleur du tracé"
#     global coul
#     pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
#     c = randrange(8)  # => génére un nbr aléatoire de 0 à 7
#     coul = pal[c]
#
#
# # ------- Programme principal -----------
# # les variables suivantes seront utilisées de manière globale :
# x1, y1, x2, y2 = 10, 190, 190, 10  # coordonnées de la ligne
# coul = 'dark green'  # couleur de la ligne
#
# # Création du widget principal ("maître") :
# fen1 = Tk()
# # Création des widgets "escaves" :
# can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
# can1.pack()
# bou1 = Button(fen1, text='Quiter', command=fen1.quit)
# bou1.pack(side=BOTTOM)
# bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
# bou2.pack()
# bou3 = Button(fen1, text='Autre couleur', command=changecolor)
# bou3.pack()
#
# fen1.mainloop()             # démarrage du réceptionnaire d'événements
#
# fen1.destroy()              # destruction (fermeture) de la fenêtre


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Dessiner les 5 anneaux olympiques dans un rectangle de fond blanc"""

# # Coordonnées X, Y des 5 anneaux :
# coord = [[20, 30], [120, 30], [220, 30], [70, 80], [170, 80]]
# # Couleurs des 5 anneaux :
# coul = ["red", "yellow", "blue", "green", "black"]
#
# base = Tk()
# can = Canvas(base, width=335, height=200, bg="white")
# can.pack()
# bou = Button(base, text="Quitter", command=base.quit)
# bou.pack(side=RIGHT)
#
# # Dessin des 5 anneaux :
# i = 0
# while i < 5:
#     x1, y1 = coord[i][0], coord[i][1]
#     can.create_oval(x1, y1, x1+100, y1+100, width=2, outline=coul[i])
#     i += 1
# base.mainloop()

# +++++++++++++++++++++++++++++++++++++++++++++++++
"""Autre Methode pour les anneaux olympiques"""

# Dessin des 5 anneaux :
# def dessineCercle(i):
#     x1, y1 = coord[i][0], coord[i][1]
#     can.create_oval(x1, y1, x1 + 100, y1 + 100, width=2, outline=coul[i])
#
#
# def a1():
#     dessineCercle(0)
#
#
# def a2():
#     dessineCercle(1)
#
#
# def a3():
#     dessineCercle(2)
#
#
# def a4():
#     dessineCercle(3)
#
#
# def a5():
#     dessineCercle(4)
#
#
# # Coordonnées X, Y des 5 anneaux :
# coord = [[20, 30], [120, 30], [220, 30], [70, 80], [170, 80]]
# # Couleurs des 5 anneaux :
# coul = ["red", "yellow", "blue", "green", "black"]
#
# base = Tk()
# can = Canvas(base, width=335, height=200, bg="white")
# can.pack()
# bou = Button(base, text="Quitter", command=base.quit)
# bou.pack(side=RIGHT)
#
# # Installation des 5 boutons :
# Button(base, text='1', command=a1).pack(side=LEFT)
# Button(base, text='2', command=a2).pack(side=LEFT)
# Button(base, text='3', command=a3).pack(side=LEFT)
# Button(base, text='4', command=a4).pack(side=LEFT)
# Button(base, text='5', command=a5).pack(side=LEFT)
# base.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++
""" Exemple graphique: Deux dessins alternés """

# def cercle(x, y, r, coul='black'):
#     "tracer d'une cercle de centre (x,y) et de rayon r"
#     can.create_oval(x - r, y - r, x + r, y + r, outline=coul)
#
#
# def figure_1():
#     "Dessiner une cible "
#     # Effacer d'abord tout dessin préexistant :
#     can.delete(ALL)
#     # tracer les deux lignes (vert. Et Horiz.)
#     can.create_line(100, 0, 100, 200, fill='blue')
#     can.create_line(0, 100, 200, 100, fill='blue')
#     # tracer plusieurs cercles concentriques :
#     rayon = 15
#     while rayon < 100:
#         cercle(100, 100, rayon)
#         rayon += 15
#
#
# def figure_2():
#     "dessiner un visage simplifié"
#     # Effacer d'abord tout dessin préexistant :
#     can.delete(ALL)
#     # Les caractèrisques de chaque cercle sont
#     # placées dans une liste de liste:
#     cc = [[100, 100, 80, 'red'],  # visage
#           [70, 70, 15, 'blue'],  # yeux
#           [130, 70, 15, 'blue'],
#           [70, 70, 5, 'black'],
#           [130, 70, 5, 'black'],
#           [44, 115, 20, 'red'],  # joues
#           [156, 115, 20, 'red'],
#           [100, 95, 15, 'purple'],  # nez
#           [100, 145, 30, 'purple']]  # bouche
#     # on trace tous les cercles à l'aide d'une boucle :
#     i = 0
#     while i < len(cc):  # parcours de la liste
#         el = cc[i]  # chaque élément est lui-même une liste
#         cercle(el[0], el[1], el[2], el[3])
#         i += 1
#
#
# ##### Programme principale : #########
#
# fen = Tk()
# can = Canvas(fen, width=200, height=200, bg='ivory')
# can.pack(side=TOP, padx=5, pady=5)
# b1 = Button(fen, text='dessin 1', command=figure_1)
# b1.pack(side=LEFT, padx=3, pady=3)
# b2 = Button(fen, text='dessin 2', command=figure_2)
# b2.pack(side=RIGHT, padx=3, pady=3)
# fen.mainloop()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Dessin d'un damier, avec placement de pions au hasard """

#
# def damier():
#     "Dessiner dix lignes de carrés avec décalage alterné"
#     y = 0
#     while y < 10:
#         if y % 2 == 0:                  # une fois sur deux, on
#             x = 0                       # commencera la ligne de
#         else:                           # carrés avec un décalage
#             x = 1                       # de la taille d'un carré
#         ligne_de_carres(x*c, y*c)
#         y += 1
#
#
# def ligne_de_carres(x, y):
#     "dessiner une ligne de carrés, en partant de x, y"
#     i = 0
#     while i < 5:
#         can.create_rectangle(x, y, x+c, y+c, fill='navy')
#         i += 1
#         x += c*2                  # espacer les carrés
#
#
# def cercle(x, y, r, coul):
#     "dessiner un cercle de centre x, y et de rayon r"
#     can.create_oval(x-r, y-r, x+r, y+r, fill=coul)
#
#
# def ajouter_pion():
#     "dessiner un pion au hasard sur le damier "
#     # tirer au hasard les coordonnées du pion :
#     x = c/2 + randrange(10) * c
#     y = c/2 + randrange(10) * c
#     cercle(x, y, c/3, 'red')
#
#
# #### --- Programme Principal : ---- ######
#
# # Tâche de bien "paramétrer" vos programmes, comme nous l'avons fait
# # dans ce script. Celui-ci peut en effet tracer des damiers de n'importe
# # quelle taille en changeant seulement la valeur d'une seul variable, à savoir la dimension des carrés :
#
# c = 30                      # taille des carrés
#
# fen = Tk()
# can = Canvas(fen, width=c*10, height=c*10, bg='ivory')
# can.pack(side=TOP, padx=5, pady=5)
# b1 = Button(fen, text='damier', command=damier)
# b1.pack(side=LEFT, padx=3, pady=3)
# b2 = Button(fen, text='pions', command=ajouter_pion)
# b2.pack(side=RIGHT, padx=3, pady=3)
# fen.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Exemple graphique: Calculatrice minimaliste"""

# Définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :


# def evaluer(event):
#     chaine.configure(text="Résultat = " + str(eval(entree.get())))
#
# # ------- Programme Principal : ------
#
#
# fenetre = Tk()
# entree = Entry(fenetre)
# entree.bind("<Return>", evaluer)
# chaine = Label(fenetre)
# entree.pack()
# chaine.pack()
#
# fenetre.mainloop()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Exemple graphique: Détection et positionnement d'un clic de souris """

# Détection et positionnement d'un clic de souris dans une fenetre :


# def pointeur(event):
#     chaine.configure(text="Clic détecté en X =" + str(event.x) +\
#                             ", Y =" + str(event.y))
#
#
# fen = Tk()
# cadre = Frame(fen, width=200, height=150, bg="light yellow")
# cadre.bind("<Button-1>", pointeur)
# cadre.pack()
# chaine = Label(fen)
# chaine.pack()
#
# fen.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Utilisation de la méthode grid pour contrôler la disposition des widgets"""

# fen1 = Tk()
# txt1 = Label(fen1, text='Premier champ :')
# txt2 = Label(fen1, text='Second :')
# entr1 = Entry(fen1)
# entr2 = Entry(fen1)
# txt1.pack(side=LEFT)
# txt2.pack(side=LEFT)
# entr1.pack(side=RIGHT)
# entr2.pack(side=RIGHT)
#
# fen1.mainloop()

"""Autre méthode"""

# fen1 = Tk()
# # création de widgets 'Label' et 'Entry' :
#
# txt1 = Label(fen1, text='Premier champ :')
# txt2 = Label(fen1, text='Second :')
# txt3 = Label(fen1, text='Troisème :')
# entr1 = Entry(fen1)
# entr2 = Entry(fen1)
# entr3 = Entry(fen1)
#
# # création d'un widget 'Canvas' contenant une image bitmap :
# can1 = Canvas(fen1, width=160, height=160, bg='white')
# photo = PhotoImage(file='manchester-united-fc.gif')
# item = can1.create_image(80, 80, image=photo)
#
# # Mise en page à l'aide de la méthode 'grid' :
# txt1.grid(row=1, sticky=E)
# txt2.grid(row=2, sticky=E)
# txt3.grid(row=3, sticky=E)
# entr1.grid(row=1, column=2)
# entr2.grid(row=2, column=2)
# entr3.grid(row=3, column=2)
# can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)
#
# # Démarrage :
# fen1.mainloop()

"""Code précedent plus Compact """
# fen1 = Tk()
#
# # création de widgets Label(), Entry(), et Checkbutton() :
# Label(fen1, text='Premier champ :').grid(sticky=E)
# Label(fen1, text='Deuxième :').grid(sticky=E)
# Label(fen1, text='Troisième :').grid(sticky=E)
# entr1 = Entry(fen1)
# entr2 = Entry(fen1)                 # ces widgets devront certainement
# entr3 = Entry(fen1)                 # être référencés plus loin:
# entr1.grid(row=0, column=1)         # il faut donc les assigner chacun
# entr2.grid(row=1, column=1)         # à une variable distincte
# entr3.grid(row=2, column=1)
# chek1 = Checkbutton(fen1, text='Case à cocher, pour voir')
# chek1.grid(columnspan=2)
#
# # création d'un widget 'Canvas' contenant une image bitmap
# can1 = Canvas(fen1, width=160, height=160, bg='white')
# photo = PhotoImage(file='manchester-united-fc.gif')
# can1.create_image(80, 80, image=photo)
# can1.grid(row=0, column=2, rowspan=4, padx=10, pady=5)
#
# # Démarrage :
# fen1.mainloop()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""" Modification des propriétés d'un objet - Animation """

# procédure générale de déplaacement :
# def avance(gd, hb):
#     global x1, y1
#     x1, y1 = x1 + gd, y1 + hb
#     can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)
#
#
# # gestionnaires d'événements
# def depl_gauche():
#     avance(-10, 0)
#
#
# def depl_droite():
#     avance(10, 0)
#
#
# def depl_haut():
#     avance(0, -10)
#
#
# def depl_bas():
#     avance(0, 10)
#
#
# # ------ Programme principal ---------
# # Les variables suivantes seront utilisées de manières globale :
# x1, y1 = 10, 10  # coordonnées initiales
#
# # Création du widget principal("maître") :
# fen1 = Tk()
# fen1.title("Exercice d'animation avec Tkinter")
#
# # Création des widgets "esclaves"
# can1 = Canvas(fen1, bg='dark grey', height=300, width=300)
# oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, width=2, fill='red')
# can1.pack(side=LEFT)
# Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
# Button(fen1, text='Gauche', command=depl_gauche).pack()
# Button(fen1, text='Droite', command=depl_droite).pack()
# Button(fen1, text='Haut', command=depl_haut).pack()
# Button(fen1, text='Bas', command=depl_bas).pack()
#
# # Démarrage du réceptionnaire d'évènements (boucle principale) :
# fen1.mainloop()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Simulation du phénomène de gravitation universelle

# def distance(x1, y1, x2, y2):
#     "Distance séparant les points x1, y1 et x2, y2"
#     d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # théorème de Pythagore
#     return d
#
#
# def forceG(m1, m2, di):
#     "force de gravitation s'exerçant entre m1 et m2 pour une distnce di"
#     return m1*m2*6.67e-11/di**2                     # loi de Newton
#
#
# def avance(n, gd, hb):
#     "Déplacement de l'astre n, de gauche à droite ou de haut en bas"
#     global x, y, step
#     # nouvelles coordonnées :
#     x[n], y[n] = x[n]+gd, y[n]+hb
#     # déplacement du dessin dans le canvas :
#     can.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)
#     # calcul de la nouvelle interdistance :
#     di = distance(x[0], y[0], x[1], y[1])
#     # conversion de la distance "écran" en distance "astronomique":
#     diA = di*1e9                    # (1 pixel ==> 1 million de km)
#     # calcul de la force de gravitation correspondante :
#     f = forceG(m1, m2, diA)
#     # Affichage des nouvelles valeurs de distance et force :
#     valDis.configure(text="Distance = " +str(diA) +" m")
#     valFor.configure(text="Force =" +str(f) +" N")
#     # adaptation du "pas" de déplacement en fonction de la distance :
#     step = di/10
#
#
# def gauche1():
#     avance(0, -step, 0)
#
#
# def droite1():
#     avance(0, step, 0)
#
#
# def haut1():
#     avance(0, 0, -step)
#
#
# def bas1():
#     avance(0, 0, step)
#
#
# def gauche2():
#     avance(1, -step, 0)
#
#
# def droite2():
#     avance(1, step, 0)
#
#
# def haut2():
#     avance(1, 0, -step)
#
#
# def bas2():
#     avance(1, 0, step)
#
#
# # Masse des deux astres :
# m1 = 6e24                   # (valeur de la masse de la terre, en kg )
# m2 = 6e24                   #
# astre = [0]*2               # liste servant à mémoriser les références des dessins
# x = [50., 350.]             # liste des coord. X de chaque astre (à l'écran)
# y = [100., 100.]            # liste des coord. Y de chaque astre
# step = 10                   # "pas" de déplacements initial
#
# # Construction de la fenêtre :
# fen = Tk()
# fen.title('Gravitation universelle suivant Newton')
# # Libelés :
# valM1 = Label(fen, text="M1 = " +str(m1) +" kg")
# valM1.grid(row=1, column=0)
# valM2 = Label(fen, text="M2 = " +str(m2) +" kg")
# valM2.grid(row=1, column=1)
# valDis = Label(fen, text="Distance")
# valDis.grid(row=3, column=0)
# valFor = Label(fen, text="Force")
# valFor.grid(row=3, column=1)
# # Canevas avec le dessin des 2 astres:
# can = Canvas(fen, bg="light yellow", width=400, height=200)
# can.grid(row=2, column=0, columnspan=2)
# astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10, fill="red", width=1)
# astre[1] = can.create_oval(x[1]-10, y[1]-10, x[1]+10, y[1]+10, fill="blue", width=1)
#
# # 2 groupes de 4 boutons, chacun installé dans un cadre (frame) :
# fra1 = Frame(fen)
# fra1.grid(row=4, column=0, sticky=W, padx=10)
# Button(fra1, text="<-", fg='red', command=gauche1).pack(side=LEFT)
# Button(fra1, text="->", fg='red', command=droite1).pack(side=LEFT)
# Button(fra1, text="^", fg='red', command=haut1).pack(side=LEFT)
# Button(fra1, text="v", fg='red', command=bas1).pack(side=LEFT)
#
# fra2 = Frame(fen)
# fra2.grid(row=4, column=1, sticky=E, padx=10)
# Button(fra2, text="<-", fg='blue', command=gauche2).pack(side=LEFT)
# Button(fra2, text="->", fg='blue', command=droite2).pack(side=LEFT)
# Button(fra2, text="^", fg='blue', command=haut2).pack(side=LEFT)
# Button(fra2, text="v", fg='blue', command=bas2).pack(side=LEFT)
#
# fen.mainloop()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""" Conversions de températures Fahrenheit <==> Celcius """


# def convFar(event):
#     "valeur de cette température, exprimée en degrés Fahrenheit"
#     tF = eval(champTC.get())
#     varTF.set(str(tF*1.8+32))
#
#
# def convCel(event):
#     "valeur de cette température, exprimée en degrés Celsius"
#     tC = eval(champTF.get())
#     varTC.set(str((tC-32)/1.8))
#
#
# fen = Tk()
# fen.title('Fahrenheit/Celcius')
#
# Label(fen, text='Temp. Celsius :').grid(row=0, column=0)
# # "variable tkinter" associée au champ d'entrée. Cet "objet-variable"
# # assure l'interface entre TCL et Python (voir notes, pages 165) :
# varTC = StringVar()
# champTC = Entry(fen, textvariable=varTC)
# champTC.bind("<Return>", convFar)
# champTC.grid(row=0, column=1)
# # Initialisation du contenu de la variable tkinter :
# varTC.set("100.0")
#
# Label(fen, text='Temp. Fahrenheit :').grid(row=1, column=0)
# varTF = StringVar()
# champTF = Entry(fen, textvariable=varTF)
# champTF.bind("<Return>", convCel)
# champTF.grid(row=1, column=1)
# varTF.set("212.0")
#
# fen.mainloop()


# ====================================================================
"""Cercles et Courbes de Lissajous """
# =============================================================

#
# def move():
#     global ang, x, y
#     # O, mémorise les coordonnées précédentes avant de calculer les nouvelles :
#     xp, yp = x, y
#     # rotation d'un angle de 0.1 radian :
#     ang = ang + .1
#     # sinus et cosinus de cet angle => coord. d'un point du cercle trigono.
#     # x, y = sin(ang), cos(ang)
#     # Variante déterminant une courbe de Lissajous avec f1/f2 = 2/3 :
#     x, y = sin(2*ang), cos(3*ang)
#     # Mise à l'échelle (120=rayon du cercle, (150, 150)=centre du canevas)
#     x, y = x*120+150, y*120+150
#     can.coords(balle, x-10, y-10, x+10, y+10)
#     can.create_line(xp, yp, x, y, fill="blue")       # trace la trajectoire
#
#
# ang, x, y = 0., 150., 270.
# fen = Tk()
# fen.title('Courbes de Lissajous')
# can = Canvas(fen, width=300, height=300, bg="white")
# can.pack()
# balle = can.create_oval(x-10, y-10, x+10, y+10, fill="red")
# Button(fen, text='GO', command=move).pack()
# # fen.mainloop()

# =======================================================
"""Animation automatique - Récursivité """
# ========================================================
# Définition des gestionnaires d'événements :


# def move():
#     "déplacement de la bale"
#     global x1, y1, dx, dy, flag
#     x1,y1 = x1+dx, y1+dy
#     if x1 > 120:
#         x1, dx, dy = 210, 0, 15
#     if y1 > 210:
#         y1, dx, dy = 210, -15, 0
#     if x1 < 10:
#         x1, dx, dy = 10, 0, -15
#     if y1 < 10:
#         y1, dx, dy = 10, 15, 0
#     can1.coords(oval1, x1, y1, x1+30, y1+30)
#     if flag > 0:
#         fen1.after(50, move)                # ==> boucler, après 50 millisecondes
#
#
# def stop_it():
#     "arret de l'animation"
#     global flag
#     flag = 0
#
#
# def start_it():
#     "Démarrage de l'animation"
#     global flag
#     if flag == 0:             # pour ne lancer qu'une seulce boucle
#         flag = 1
#         move()
#
#
# # =====================Programme principal ==================
#
# # Les variables suivantes seront utilisées de manières globale :
# x1, y1 = 10, 10             # coordonnées initiales
# dx, dy = 15, 0              # 'pas' du déplacement
# flag = 0                    # commutateur
#
# # Création du widget principal ("parent")
# fen1 = Tk()
# fen1.title("Exercice d'animation avec Tkinter")
# # Création des widgets "enfants"
# can1 = Canvas(fen1, bg='dark grey', height=250, width=250)
# can1.pack(side=LEFT, padx=5, pady=5)
# oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
# bout1 = Button(fen1, text='Quitter', width=8, command=fen1.quit)
# bout1.pack(side=BOTTOM)
# bout2 = Button(fen1, text='Démarrer', width=8, command=start_it)
# bout2.pack()
# bout3 = Button(fen1, text='Arreter', width=8, command=stop_it)
# bout3.pack()
#
# # Démarrage du réceptionnaire d'événements (boucle principale):
# fen1.mainloop()


# ============================================================
"""Chutes et Rebonds """
# ============================================================


# def move():
#     global x, y, v, dx, dv, flag
#     xp, yp = x, y               # mémorisation des coord. précédentes
#     # déplacement horizontal :
#     if x > 385 or x < 15:              # rebond sur les parois latérales :
#         dx = -dx                        # on inverse le déplacement
#     x = x + dx
#     # variation de la vitesse verticale (toujours vers le bas) :
#     v = v + dv
#     # déplacement vertical (proportionnel à la vitesse)
#     y = y + v
#     if y > 240:                 # niveau du sol à 240 pixels :
#         y = 240                 # défense d'aller + loin !
#         v = -v                  # rebond : la vitesse s'inverse
#     # On repositionne la balle :
#     can.coords(balle, x-10, y-10, x+10, y+10)
#     # on trace un bout de trajectoire :
#     can.create_line(xp, yp, x, y, fill='light grey')
#     # ... et on remet ça jusqu'à plus soif :
#     if flag > 0:
#         fen.after(50, move)
#
#
# def start():
#     global flag
#     flag = flag + 1
#     if flag == 1:
#         move()
#
#
# def stop():
#     global flag
#     flag = 0
#
#
# # initialisation des coordonées, des vitesses et du témon d'animation"
# x, y, v, dx, dv, flag = 15, 15, 0, 6, 5, 0
#
# fen = Tk()
# fen.title('Chutes et rebonds')
# can = Canvas(fen, width=400, height=250, bg='white')
# can.pack()
# balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
# Button(fen, text='START', command=start).pack(side=LEFT, padx=10)
# Button(fen, text='Stop', command=stop).pack(side=LEFT)
# Button(fen, text='Quitter', command=fen.quit).pack(side=RIGHT, padx=10)
# fen.mainloop()

# ================================================================
""" Jeu du serpent """
# ================================================================

# === Définition de quelques gestionnaires d'événements :
#
# def start_it():
#     "Démarrage de l'animation"
#     global flag
#     if flag == 0:
#         flag = 1
#         move()
#
#
# def stopt_it():
#     "Arret de l'animation"
#     global flag
#     flag = 0
#
#
# def go_left(event=None):
#     "Déplacement vers la gauche"
#     global dx, dy
#     dx, dy = -1, 0
#
#
# def go_right(event=None):
#     "Déplacement vers la droite"
#     global dx, dy
#     dx, dy = 1, 0
#
#
# def go_up(event=None):
#     "Déplacement vers le haut"
#     global dx, dy
#     dx, dy = 0, -1
#
#
# def go_down(event=None):
#     global dx, dy
#     dx, dy = 0, 1
#
#
# def move():
#     "Animation du serpent par recursivité"
#     global flag
#     # Principe du mvment opéré : On déplace le carré de queue, dont les caractéristiques son
#     # mémorisées dans le premier élément de la liste <serp>, de manière à l'amener en
#     # avant du carré de tête, dont les caractéristiques sont mémorisées dans le dernier élément
#     # de la liste. On définit ainsi un nouveau carré de tête pour e serpent, dont on
#     # mémorise les caractéristiques en les ajoutant à la liste. Il ne reste plus qu'à
#     # éffacer alors le premier élément de la liste, et ainsi de suite ...:
#     c = serp[0]         # extraction des infos concernat le carré de queue
#     cq = c[0]           # réf. de ce carré (coordonnées inutiles ici)
#     l = len(serp)       # longueur actuelle du serpent (= n. de carrés)
#     c = serp[l-1]       # extraction des infos concernant le carré de tête
#     xt, yt = c[1], c[2]     # coordonnées de ce carré
#     # Préparation du déplacement proprement dit.
#     # (cc est la taille du carré. dx & dy indiquent le sens du déplacement) :
#     xq, yq = xt+dx*cc, yt+dy*cc         # coord. du nouveau carré de tête
#     # vérification : a-t-on atteint les limites du canevas ? :
#     if xq < 0 or xq > canX-cc or yq < 0 or yq > canY-cc:
#         flag = 0            # => arrêt de l'animation
#         can.create_text(canX/2, 20, anchor=CENTER, text="Perdu !!!",
#                         fill="red", font="Arial 14 bold")
#     can.coords(cq, xq, yq, xq+cc, yq+cc)        # déplacement effectif
#     serp.append([cq, xq, yq])           # mémorisation du nouveau carré de tête
#     del(serp[0])                        # effacement (retrait de la liste)
#     # Appel récursif de la fonction par elle-même (=> boucle d'animation) :
#     if flag > 0:
#         fen.after(50, move)
#
#
# # === Programme principale : =======
# # Variables globales modifiables par certaines fonctions :
# flag = 0            # commutateur pour l'animation
# dx, dy = 1, 0       # indicateurs pour le sens du déplacement
#
# # Autre variables globales :
# canX, canY = 500, 500    # dimensions du canevas
# x, y, cc = 100, 100, 15             # indicateurs pour le sens du déplacement
#
# # Création de l'espace de jeu (fenêtre, canevas, boutons, ...) :
# fen = Tk()
# can = Canvas(fen, bg='dark gray', height=canX, width=canY)
# can.pack(padx=10, pady=10)
# bou1 = Button(fen, text="Start", width=10, command=start_it)
# bou1.pack(side=LEFT)
# bou2 = Button(fen, text="Stop", width=10, command=stopt_it)
# bou2.pack(side=LEFT)
# bou3 = Button(fen, text="Gauche", width=10, command=go_right)
# bou3.pack(side=LEFT)
# bou4 = Button(fen, text="Droite", width=10, command=go_left)
# bou4.pack(side=LEFT)
# bou5 = Button(fen, text="Haut", width=10, command=go_up)
# bou5.pack(side=LEFT)
# bou6 = Button(fen, text="Bas", width=10, command=go_down)
# bou6.pack(side=LEFT)
#
# # Association de gestionnaires d'événements aux touches fléchées du clavier :
# fen.bind("<Left>", go_left)         # Attention : les événements clavier
# fen.bind("<Right>", go_right)       # doivent tjr être associés à la
# fen.bind("<Up>", go_up)             # fenètre principale, et non au canevas
# fen.bind("<Down>", go_down)         # ou à un autre widget.
#
# # Création du serpent initial (= ligne de 5 carrés).
# # On mémorisera les infos concernant les carrés créés dans une liste de listes :
# serp = []
# # Création et mémorisation des 5 carrés : le dernier (à droite) est la tête.
# i = 0
# while i < 5:
#     carre = can.create_rectangle(x, y, x+cc, y+cc, fill="green")
#     # Pour chaque carré, on mémorise une petite sous-liste contenant
#     # 3 éléments : la référance du carré et ses coordonnées de base :
#     serp.append([carre, x, y])
#     x = x+cc                # le carré suivant sera un peu plus à droite
#     i = i + 1
#
# fen.mainloop()

# =========================================================









