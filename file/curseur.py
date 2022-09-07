from tkinter import *
from math import *


"""On va construire un widget Scale qui est une sorte de panneau de contrôle
comportant trois curseurs de réglage et une case à cocher.
Le widget Scale se présente comme un curseur qui coulisse devant une échelle.
Il permet à l'utilisateur de choisir rapidement la valeur d'un paramètre
quelconque, d'une manière très attrayante."""


# def updateLabel(x):
#     lab.configure(text='valeur actuelle = ' + str(x))
#
#
# root = Tk()
# Scale(root, length=250, orient=HORIZONTAL, label='Réglage :',
#       troughcolor='dark grey', sliderlength=20,
#       showvalue=0, from_=-25, to=125, tickinterval=25, command=updateLabel).pack()
# lab = Label(root)
# lab.pack()
#
# root.mainloop()


class ChoixVibra(Frame):
    """Curseurs pour choisir fréquence, phase & amplitude d'une vibration"""
    def __init__(self, boss=None, coul='red'):
        Frame.__init__(self)                # constructeur de la classe parente
        # Initialisation de quelques attributs d'instance :
        self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
        # Variable d'état de la case à cocher :
        self.chk = IntVar()                     # 'objet-variable' tkinter
        Checkbutton(self, text='Afficher', variable=self.chk, fg=self.coul,
                    command=self.setCurve).pack(side=LEFT)
        # Définition des 3 widgets curseurs :
        Scale(self, length=150, orient=HORIZONTAL, sliderlength=25, label='Fréquence (Hz) :',
              from_=1., to=9., tickinterval=2, resolution=0.25, showvalue=0,command=self.setFrequency).pack(side=LEFT)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength=25, label='Phase (degrès) :',
              from_=-180, to=180, tickinterval=90, showvalue=0, command=self.setPhase).pack(side=LEFT)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength=25, label='Amplitude :',
              from_=1, to=9, tickinterval=2, showvalue=0, command=self.setAmplitude).pack(side=LEFT)

    def setCurve(self):
        self.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq = float(f)
        self.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp = float(p)
        self.phase = pp*2*pi/360               # conversion degrès -> radians
        self.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.event_generate('<Control-Z>')


# ### CODE pour tester la classe : ###
if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text= '{0} - {1} - {2} - {3}'.\
                      format(fra.chk.get(), fra.freq, fra.phase, fra.ampl))
    root = Tk()
    fra = ChoixVibra(root, 'navy')
    fra.pack(side=TOP)
    lab = Label(root, text='test')
    lab.pack()
    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
