from tkinter import *


# =================================================================================
"""Combo box Simplifié:
Ce script nous montre comment construire une widget de type Combo box.
On appelle ainsi un widget qui associe un champ d'entrée à une boîte de liste:
l'utilisateur peut entrer dans le système soit un des éléments de la liste proposé (
en cliquant sur son nom), soit un élément non répertorié(en saisissant un nouveau nom dans le champ d'entrée).
Notre widget combo va donc regrouper en une seule entité trois widgets de base tkinter: un champ d'entrée
une boite de liste(listbox) et un <<ascenseur>> (barre de défilement vertical ou scrollbar)"""
# =================================================================================
#
#
# class ComboBox(Frame):
#     "Widget composite associant un champ d'entrée avec une boîte de liste"
#     def __init__(self, boss, item='', items=[], command='', width=10, listSize=5):
#         Frame.__init__(self, boss)          # constructeur de la classe parente
#                                             # (<boss> est la réf. du widget 'maître')
#         self.items = items                  # items à placer dans la boîte de liste
#         self.command = command              # fonction à invoquer après clic ou <Enter>
#         self.item = item                    # item entré ou sélectionné
#
#         # Champ d'entrée :
#         self.entree = Entry(self, width=width)      # largeur en caractères
#         self.entree.insert(END, item)
#         self.entree.bind("<Return>", self.sortieE)
#         self.entree.pack(side=TOP)
#
#         # Boîte de liste, munie d'un ascenseur (scroll bar) :
#         cadreLB = Frame(self)                       # cadre pour l'ensemble des 2
#         self.bListe = Listbox(cadreLB, height=listSize, width=width-1)
#         scrol = Scrollbar(cadreLB, command=self.bListe.yview)
#         self.bListe.config(yscrollcommand=scrol.set)
#         self.bListe.bind("<ButtonRelease-1>", self.sortieL)
#         self.bListe.pack(side=LEFT)
#         scrol.pack(expand=YES, fill=Y)
#         cadreLB.pack()
#
#         # Remplissage de la boîte de liste avec les items fournis :
#         for it in items:
#             self.bListe.insert(END, it)
#
#     def sortieL(self, event=None):
#         # Extraire de la liste l'item qui a été sélectionné :
#         index = self.bListe.curselection()              # renvoie un tuple d'index
#         ind0 = int(index[0])                            # on ne garde que le premier
#         self.item = self.items[ind0]
#         # Actualiser le champ d'entrée avec l'item choisi :
#         self.entree.delete(0, END)
#         self.entree.insert(END, self.item)
#         # Executer la commande indiquée, avec l'item choisi comme argument :
#         self.command(self.item)
#
#     def sortieE(self, event=None):
#         # Exécuter la command indiquée, avec l'argument-item encodé tel quel :
#         self.command(self.entree.get())
#
#     def get(self):
#         # Renvoyer le dernier item sélectionné dans la boîte de liste
#         return self.item
#
#
# if __name__ == '__main__':                  # --- Programme de test ----
#     def changeCoul(col):
#         fen.configure(background=col)
#
#     def changeLabel():
#         lab.configure(text=combo.get())
#
#     couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
#                 'lawn green', 'forest green', 'yellow', 'dark red',
#                 'grey80', 'grey60', 'grey40', 'grey20', 'pink')
#     fen = Tk()
#     combo = ComboBox(fen, item="néant", items=couleurs, command=changeCoul, width=15, listSize=6)
#     combo.grid(row=1, columnspan=2, padx=10, pady=10)
#     bou = Button(fen, text="Test", command=changeLabel)
#     bou.grid(row=2, column=0, padx=8, pady=8)
#     lab = Label(fen, text="Bonjour", bg="ivory", width=15)
#     lab.grid(row=2, column=1, padx=8)
#     fen.mainloop()

# =====================================================================================================================
""" Perfectionner notre widget << combo box simplifié>> de manière à ce que la liste soit cachée au départ, et qu'un petit bouton à droite
du champ d'entrée le fasse apparaître. On devrait pour ce faire placer la liste et son ascenseur dans une fenêtre satellite
sans bordure, positionner celle-ci correctement, et nous assurer que cette fenêtre disparaisse après que l'utilisateur a sélectionner un item dans la liste"""
# =====================================================================================================================


class ComboFull(Frame):
    "Widget composite 'Combo box' (champ d'entrée + liste 'déroulante')"
    def __init__(self, boss, item='', items=[], command='', width=10, listSize=5):
        Frame.__init__(self, boss)                      # constructeur de la classe parente
        self.boss = boss                                # réference du widget 'maître'
        self.items = items                              # items à placer dans la boîte de liste
        self.command = command                          # fct à invoquer après clic ou <enter>
        self.item = item                                # item entré ou sélectionné
        self.listSize = listSize                        # Nbre d'items visible dans la liste
        self.width = width                              # largeur du champ d'entrée (en caract.)

        # Champ d'entrée :
        self.entree = Entry(self, width=width)             # largeur en caractères
        self.entree.insert(END, item)
        self.entree.bind("<Return>", self.sortieE)
        self.entree.pack(side=LEFT)

        # Button pour faire apparaître la liste associée :
        self.gif1 = PhotoImage(file="manchester-united-fc.gif")        # ! variable persistante
        Button(self, image=self.gif1, width=15, height=15, command=self.popup).pack()

    def sortieL(self, event=None):
        # Extraction de la liste l'item qui a été sélectionné :
        index = self.bListe.curselection()                  # renvoie un tuple d'index
        ind0 = int(index[0])                                # on ne garde que le premier
        self.item = self.items[ind0]
        # Actualiser le champ d'entrée avec l'item choisi :
        self.entree.delele(0, END)
        self.entree.insert(END, self.item)
        # Exécuter la commande indiquée, avec l'item choisi comme argument :
        self.command(self.item)
        self.pop.destroy()                                  # supprimer la fenêtre satellite

    def sortieE(self, event=None):
        # Exécuter la commande indiquée, avec l'argument-item encodé tel quel :
        self.command(self.entree.get())

    def get(self):
        # Renvoyer la dernier item sélectionné dans la boîte de Liste
        return self.item

    def popup(self):
        # Faire apparaître la petite fenêtre satellite contenant la liste.
        # On commence par récupérer les coordonnées du coin supérieur gauche
        # du présent widget dans la fenêtre principal :
        xW, yW = self.winfo_x(), self.winfo_y()
        # ... et les coordonnées de la fenêtre principale sur l'écran, grâce à
        # la méthode geometry() qui renvoie une chaîne avec taille et coordo. :
        geo = self.boss.geometry().split("+")
        xF, yF = int(geo[1]), int(geo[2])                   # coord. coin supérieur gauche
        # On peut alors positionner une petite fenêtre, modale et sans bordure,
        # exactement sous le champ d'entrée :
        xP, yP = xF+xW+10, yF+yW+45                 # +45: compenser haut champ Entry
        self.pop = Toplevel(self)                   # fenêtre secondaire ("pop up")
        self.pop.geometry("+{0}+{1}".format(xP, yP))        # positionnement / écran
        self.pop.overrideredirect(1)                # => fen. sans bordure ni bandeau
        self.pop.transient(self.master)             # => fen. 'modale'

        # Boîte de liste, munie d'un 'ascenseur' (scroll bar) :
        cadreLB = Frame(self.pop)                   # cadre pour l'ensemble des 2
        self.bListe = Listbox(cadreLB, height=self.listSize, width=self.width-1)
        scrol = Scrollbar(cadreLB, command=self.bListe.yview)
        self.bListe.config(yscrollcommand=scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.pack(side=LEFT)
        scrol.pack(expand=YES, fill=Y)
        cadreLB.pack()
        # Remplissage de la boîte de liste avec les items fournis :
        for it in self.items:
            self.bListe.insert(END, it)


if __name__ == "__main__":                  # --- Programme de test ---
    def changeCoul(col):
        fen.configure(background=col)

    def changeLabel():
        lab.configure(text=combo.get())

    couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
                'lawn green', 'forest green', 'yellow', 'dark red',
                'grey80', 'grey60', 'grey40', 'grey20', 'pink')

    fen = Tk()
    combo = ComboFull(fen, item="neant", items=couleurs, command=changeCoul,
                      width=15, listSize=6)
    combo.grid(row=1, columnspan=2, padx=10, pady=10)
    bou = Button(fen, text="Test", command=changeLabel)
    bou.grid(row=3, column=0, padx=8, pady=8)
    lab = Label(fen, text="Bonjour", bg="ivory", width=15)
    lab.grid(row=3, column=1, padx=8)
    fen.mainloop()
