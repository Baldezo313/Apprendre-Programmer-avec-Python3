from tkinter import *
from random import randrange

# ============================================================================
"""Comment déplacer des dessins à l'aide de la souris:
Au démarrage de notre petite application, une série de dessins sont tracés au hasard dans un Canvas.
On peut déplacer n'importe lequel de ces dessins en le <<saisissant>> à l'aide de notre souris.
Lorsqu'un dessin est déplacé, il passe à l'avant-plan par rapport aux autres, et sa bordure 
apparaît plus épaisse pendant toute la durée de sa manipulation."""


# ============================================================================


# class Bac_a_sable(Canvas):
#     "Canvas modifié pour prendre en compte quelques actions de la souris"
#
#     def __init__(self, boss, width=80, height=80, bg="white"):
#         # invocation du constructeur de la class parente :
#         Canvas.__init__(self, boss, width=width, height=height, bg=bg)
#         # Association-liaison d'événement <souris> au présent widget :
#         self.bind("<Button-1>", self.mouseDown)
#         self.bind("<Button1-Motion>", self.mouseMove)
#         self.bind("<Button1-ButtonRelease>", self.mouseUp)
#
#     def mouseDown(self, event):
#         "Opération à effectuer quand le bouton gauche de la souris est enfoncé"
#         self.currObject = None
#         # event.x et event.y contiennent les coordonnées du clic effectué :
#         self.x1, self.y1 = event.x, event.y
#         # <find_closest> renvoie la référence du dessin le plus proche :
#         self.selObject = self.find_closest(self.x1, self.y1)
#         # Modification de l'épaisseur du contour du dessin
#         self.itemconfig(self.selObject, width=3)
#         # <lift> fait passer le dessin à l'avant-plan :
#         self.lift(self.selObject)
#
#     def mouseMove(self, event):
#         "Op. à effectuer quand la souris se déplace, bouton gauche enfoncé"
#         x2, y2 = event.x, event.y
#         dx, dy = x2 - self.x1, y2 - self.y1
#         if self.selObject:
#             self.move(self.selObject, dx, dy)
#             self.x1, self.y1 = x2, y2
#
#     def mouseUp(self, event):
#         "Op. à effectuer quand le bouton gauche de la souris est relâché"
#         if self.selObject:
#             self.itemconfig(self.selObject, width=1)
#             self.selObject = None
#
#
# if __name__ == '__main__':              # ---- Programme de test ---
#     couleurs = ('red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet', 'purple')
#     fen = Tk()
#     # mise en place du canevas - dessin de 15 ellipses colorées
#     bac = Bac_a_sable(fen, width=400, height=300, bg='ivory')
#     bac.pack(padx=5, pady=3)
#     # bouton de sortie :
#     b_fin = Button(fen, text='Terminer', bg='royal blue', fg='white',
#                    font=('Helvetica', 10, 'bold'), command=fen.quit)
#     b_fin.pack(pady=2)
#     # tracé de 15 ellipses avec couleur et coordonnées aléatoires :
#     for i in range(15):
#         coul = couleurs[randrange(8)]
#         x1, y1 = randrange(300), randrange(200)
#         x2, y2 = x1 + randrange(10, 150), y1 + randrange(10, 150)
#         bac.create_oval(x1, y1, x2, y2, fill=coul)
#     fen.mainloop()


# =================================================================
"""On vas associé au Canevas standard deux barres de défilement (une
verticale et une horizontale).
Afin de rendre l'exercice plus attrayant, nous nous servirons de notre 
 nouvelle class de widget pour réaliser un petit jeu d'adresse, dans lequel l'utilisateur
 devra réussir à cliquer sur un bouton qui s'esquive sans cesse."""
# ==================================================================


class ScrolledCanvas(Frame):
    """Canevas extensible avec barres de défilement"""
    def __init__(self, boss, width=100, height=100, bg="white", bd=2,
                 scrollregion=(0, 0, 300, 300), relief=SUNKEN):
        Frame.__init__(self, boss, bd=bd, relief=relief)
        self.can = Canvas(self, width=width-20, height=height-20, bg=bg,
                          scrollregion=scrollregion, bd=1)
        self.can.grid(row=0, column=0)
        bdv = Scrollbar(self, orient=VERTICAL, command=self.can.yview, bd=1)
        bdh = Scrollbar(self, orient=HORIZONTAL, command=self.can.xview, bd=1)
        self.can.configure(xscrollcommand=bdh.set, yscrollcommand=bdv.set)
        bdv.grid(row=0, column=1, sticky=NS)        # sticky =>
        bdh.grid(row=1, column=0, sticky=EW)        # étirer la barre
        # Lier l'événement <redimensionnement> à un gestionnaire approprié :
        self.bind("<Configure>", self.redim)
        self.started = False

    def redim(self, event):
        "opérations à effectuer à chaque redimensionnement du widget"
        if not self.started:
            self.started = True             # Ne pas redimensionner dès la création
            return                          # du widget (sinon => bouclage)
        # À partir des nouvelles dimensions du cadre, redimensionner le canvas
        # (la diff. de 20 pixels sert à compenser l'épaisseur des scrollbars):
        larg, haut = self.winfo_width()-20, self.winfo_height()-20
        self.can.config(width=larg, height=haut)


class FenPrinc(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.libelle = Label(text="Scroll game", font="Helvetica 14 bold")
        self.libelle.pack(pady=3)
        terrainJeu = ScrolledCanvas(self, width=500, height=300, relief=SOLID,
                                    scrollregion=(-600, -600, 600, 600), bd=3)
        terrainJeu.pack(expand=YES, fill=BOTH, padx=6, pady=6)
        self.can = terrainJeu.can
        # Décor : tracé d'un série d'ellipses aléatoire :
        coul = ('sienna', 'maroon', 'brown', 'pink', 'tan', 'wheat', 'gold', 'orange',
                'plum', 'red', 'khaki', 'indian red', 'thistle', 'firebrick',
                'salmon', 'coral', 'yellow', 'cyan', 'blue', 'green')
        for r in range(80):
            x1, y1 = randrange(-600, 450), randrange(-600, 450)
            x2, y2 = x1 + randrange(40, 300), y1 + randrange(40, 300)
            couleur = coul[randrange(20)]
            self.can.create_oval(x1, y1, x2, y2, fill=couleur, outline='black')
        # Ajout d'une petite image GIF
        # self.img = PhotoImage(file='linux2.png')
        # self.can.create_image(50, 20, image=self.img)
        # Bouton à attraper :
        self.x, self.y = 50, 100
        self.bout = Button(self.can, text="Start", command=self.start)
        self.fb = self.can.create_window(self.x, self.y, window=self.bout)

    def anim(self):
        if self.run == 0:
            return
        self.x += randrange(-60, 61)
        self.y += randrange(-60,61)
        self.can.coords(self.fb, self.x, self.y)
        self.libelle.config(text='Cherchez en %s %s' % (self.x, self.y))
        self.after(250, self.anim)

    def stop(self):
        self.run = 0
        self.bout.configure(text="Start", command=self.start)

    def start(self):
        self.bout.configure(text="Attrapez-moi !", command=self.stop)
        self.run = 1
        self.anim()


# --------- Programme de test -----------------
if __name__ == '__main__':
    FenPrinc().mainloop()
