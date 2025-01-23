# DESGRACAAAAAAAAAAAAAAAAAaaa
import tkinter as tk
import random
from tkinter import *
    
wind= tk.Tk ()

wind.title("Eai?")
wind.geometry("700x400")
wind.configure(background='#415a56')
wind.resizable(True, True)

wind.maxsize(width=1920, height=1080)
wind.minsize(width=700, height=500)

frame1 = Frame (wind)
frame1.place(relx=0.05, rely=0.05,relwidth=0.9, relheight=0.9)

# DESGRACAAAAAAAAAAAAAAAAAaaa
def mover_nao(event):
    x = random.uniform(0.1, 0.75) 
    y = random.uniform(0.1, 0.75) 
    botao_nao.place(relx=x, rely=y) 

# botao
def sim():
  eba.configure(text='CORNO DESGRACADO VAI SE FUDER!!')

eba = tk.Label(wind, text=' ',font="Consolas 16")
eba.place(relx=0.15, rely=0.4,relwidth=0.7, relheight=0.2)

pergunta = tk.Label(wind, text="VOCE É CORNO??",font="Consolas 24")
pergunta.place(relx=0.15, rely=0.25,relwidth=0.75, relheight=0.1)

#BOTAOTES
botao_nao = tk.Button(wind, text='NAO ', font="Consolas", bg="#fa7258", fg="black", cursor='cross')
botao_nao.place(relx=0.55, rely=0.7, relwidth=0.15, relheight=0.1)
botao_nao.bind("<Enter>", mover_nao) 

botao_sim = tk.Button(wind, text='SIM ', font="Consolas", bg="#8dce4e", fg="black", command=sim)
botao_sim.place(relx=0.3, rely=0.7, relwidth=0.15, relheight=0.1)

wind.mainloop()

