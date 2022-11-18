from tkinter import *


# ==============================================================
"""Le widget Text asorti d'un ascenseur:
Ce widget va nous servir à ébaucher un système de traitement de text rudimentaire.
Son principal composant est le widget 'Text' standard, qui peut afficher des textes formatés, c'est à dire
des textes intégrant divers attributs de style (comme le gras, l'italique, l'exposant...) ainsi que des
polices de caractères différentes, de la couleur, et même des images. Nous l'avons simplement associé à une
barre de défilement verticale pour nous montrer, une fois de plus, les interactions que nous pouvons créer
entre ces composants."""
# ================================================================


class ScrlolledText(Frame):
    """Widget composite, associant un widget Text et une barre de défiliement"""
    def __init__(self, boss, baseFont="Time", width=50, height=25):
        Frame.__init__(self, boss, bd=2, relief=SUNKEN)
        self.text = Text(self, font=baseFont, bg='ivory', bd=1, width=width, height=height)
        scroll = Scrollbar(self, bd=1, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
        scroll.pack(side=RIGHT, expand=NO, fill=Y, padx=2, pady=2)

    def importFichier(self, fichier, encodage="UTF8"):
        "insertion d'un texte dans le widget, à partir d'un fichier"
        of = open(fichier, "r", encoding=encodage)
        lignes = of.readlines()
        of.close()
        for li in lignes:
            self.text.insert(END, li)


def chercheCible(event=None):
    "défilement du texte jusqu'à la balise <cible>, grâce à la méthode see()"
    index = st.text.tag_nextrange('cible', '0.0', END)
    st.text.see(index[0])


# ### Programme principal : fenêtre avec un libellé et un 'ScrolledText'  ###
fen = Tk()
lib = Label(fen, text="Widget composite : Text + Scrollbar", font="Times 14 bold italic", fg="navy")
lib.pack(padx=10, pady=4)
st = ScrlolledText(fen, baseFont="Helvetica 12 normal", width=40, height=10)
st.pack(expand=YES, fill=BOTH, padx=8, pady=8)

# Définition de balises, liaison d'un événement <clic du bouton droite> :
st.text.tag_configure("titre", foreground="brown", font="Helvetica 11 bold italic")
st.text.tag_configure("lien", foreground="blue", font="helvetica 11 bold")
st.text.tag_configure("cible", foreground="forest green", font="Times 11 bold")
st.text.tag_bind("lien", "<Button-3>", chercheCible)

titre = """Le Corbeau et le Renard par Jean de la Fontaine, auteur Francais\n"""
auteur = """
Jean de la Fontaine
écrivain français (1621-1695)
célébre pour ses contes en vers,
et surtout ses Fables, publiées
de 1668 à 1694."""

# Remplissage du wiget Text (2 techniques) :
st.importFichier("CorbRenard.txt", encodage="Latin1")
st.text.insert("0.0", titre, "titre")
st.text.insert(END, auteur, "cible")

# Insertion d'une image :
# photo = PhotoImage(file="penguin.jpg")
# st.text.image_create("6.14", image=photo)

# Ajout d'une balise supplémentaire :
st.text.tag_add("lien", "2.4", "2.23")

fen.mainloop()

