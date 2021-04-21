# -*- coding: utf-8 -*-
# Código para a Assistente em Py

## Atenção, antes de vc executar o código, precisa baixar as seguintes bibliotecas no tterinal

## Deve ser usado uma versão de python superior ao 3.0

## pip3 install pytesseract (para o versões 3.x)

## pip3 install PIL

## pip3 install Image

#-----Instalando o repositório do tesseract
#sudo apt update
#sudo apt install tesseract-ocr
#sudo apt install libtesseract-dev

## Não testei esse programa no Windows ainda!

## Biblioteca usada para escrever na tela do terminal

from sympy import *
from sympy.plotting import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter as tk

root = tk.Tk()

root.geometry('600x500') 

tkimage = ImageTk.PhotoImage(Image.open("texting.png"))
tk.Label(root, image=tkimage).place(x = 10, y = 20)



lab = Label(root,text="Texting - Textos\nem Imagens", font=("Aliens","30"))
lab.place(x=250,y=10)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
    
    

    
def open_img():
    x = openfn()
    img = Image.open(x)
    filename = openfn()
    #img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    
    

    

import numpy as np
import matplotlib.pyplot as plt
import pytesseract as ocr
import PIL
import pytesseract
def gerar():
    
    usuario=openfn()
    filepath = usuario
    
    img = pytesseract.image_to_string(Image.open(filepath))
    lab = Label(root,text='A equação/frase é: '+img, font=("Aliens","12"))
    lab.place(x=270,y=200)    
    
    
    #plt.plot(img)
    #plt.show()
    



btnt = Button(root, text='Abrir Arquivo de Imagem', command=gerar).place(x=20,y=250)

root.mainloop()
