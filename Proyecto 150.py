# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:43:20 2023

@author: anyta
"""

from tkinter import *
import random

root =Tk()
root.geometry("500x500")
root.title("Super sonic")

Heroe = Entry(root)
Villano = Entry(root)

Lista_heroe = []
Lista_villano = []

Luchador = Label(root)
Luchador2 = Label(root)

def Pelea():
    Heroe.get()
    Villano.get()
    
    Lista_heroe.append(Heroe)
    Lista_villano.append(Villano)
    
    
btn = Button(root, text= "Que peleen", command= Pelea)   

def Enfrentamiento():
    Longitud = len(Lista_heroe)
    Longitud2 = len(Lista_villano)
    
    Heroe_aleatorio = random.randint(0, Longitud - 1)
    
    Villano_aleatorio = random.randint(0, Longitud2 - 1)
    
    Luchador["text"] = str( Lista_heroe)
    Luchador2["text"] = str(Lista_villano)
    
btn2 = Button(root, text= "pelea aleatoria", command= Enfrentamiento)
    
Heroe.place(relx=0.5, rely=0.3, anchor=CENTER)
Villano.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
Luchador.place(relx=0.5, rely=0.6, anchor=CENTER)
Luchador2.place(relx=0.5, rely=0.7, anchor=CENTER)
btn2.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()