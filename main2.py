# coding: utf-8
import os
import tkinter
from tkinter import *

if __name__ == '__main__':
    l=["coucou","compté du danmark de mes 2","ok pt'it test tranquillou","1"]
    fenetre= tkinter.Tk()
    test ='tsfdhgjvgnfbvdfsq'
    #label =tkinter.Label(fenetre,text="Bonjour voici votre Objectif!").pack()
    for i in range(0,len(l)):
        bouton=tkinter.Button(fenetre, text=l[i]).pack(side=LEFT)


    #bouton=tkinter.Button(fenetre, text="New Game", command=fenetre.).pack()
    fenetre.mainloop()