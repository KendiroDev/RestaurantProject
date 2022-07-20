from tkinter import *


###variaveis
refeição = 35
meia = 17.50
lata = 5
suco = 8 
heineken = 15
original = 14
skol = 12
sorvete = 4
caipirinha = 15
agua = 3
agua_gas = 3.5
contador = 0
marmitex = 35
pinga = 5
relatorio = 0
valor = 0
qtdn_ref = 0
qtdn_meia =0
qtdn_agua = 0
qtdn_agua_gas = 0
qtdn_lata = 0
qtdn_suco = 0
qtdn_heineken =  0
qtdn_original = 0
qtdn_skol = 0
qtdn_sorvete = 0
qtdn_caipirinha = 0 
qtdn_pinga = 0 
qtdn_marmitex =  0



        
        





root = Tk()
def somar():
        top = Toplevel()
        top.configure(bg='#e6ccb3')
        top.title ('Valor da comanda')
        top.geometry('300x200')
        text_valor = Label(top, text='Valor de comsumo a pagar é de: R$')
        text_valor.pack()
       


root.title('TORRESMARIA')
root.iconbitmap('imagens/icone.ico')
logo = PhotoImage (file= 'imagens/LOGO2.png')
root.configure(bg='#e6ccb3')
largura = 900
altura = 500
largura_screen = root.winfo_screenwidth()
altura_screen= root.winfo_screenheight() - 100
posx = (largura_screen / 2) - (largura / 2)
posy = (altura_screen /2 ) - (altura / 2)

root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))



imagem = Label(root, image= logo).place(x=320, y=110)
titulo = Label(root, text='CONTROLE DE COMANDAS', bg='#e6ccb3', font='arial 22 bold').place(x=270, y=10)
espace1 = Label(root, text=' ',bg='#e6ccb3').grid(row=0 , column=0)
espace2 = Label(root, text=' ',bg='#e6ccb3').grid(row=1 , column=0)
espace3 = Label(root, text=' ',bg='#e6ccb3').grid(row=2 , column=0)


qtdn_ref = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=3, column=1)
qtdn_meia = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=4, column=1)
qtdn_lata = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=5, column=1)
qtdn_suco = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=6, column=1)
qtdn_heineken = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=7, column=1)
qtdn_original = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=8, column=1)
qtdn_skol = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=9, column=1)
qtdn_sorvete = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=10, column=1)
qtdn_caipirinha = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=11, column=1)
qtdn_agua = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=12, column=1)
qtdn_agua_gas = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=13, column=1)
qtdn_marmitex = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=14, column=1)
qtdn_pinga = Spinbox(root, from_= 0, to=15, justify=CENTER, width=5, wrap=TRUE).grid(row=15, column=1)


text_refeição = Label(root, text= 'REFEIÇÃO', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID, 
        justify=LEFT, width= 14).grid(row=3,column=0)
text_meia = Label(root, text= 'MEIA', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=4,column=0)
text_lata = Label(root, text= 'REFRIGERANTE', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
        justify=LEFT, width= 14).grid(row=5,column=0)
text_suco = Label(root, text= 'SUCO', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=6,column=0)
text_heineken = Label(root, text= 'HEINEKEN', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=7,column=0)
text_original = Label(root, text= 'ORIGINAL', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=8,column=0)
text_skol = Label(root, text= 'SKOL', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=9,column=0)
text_sorvete = Label(root, text= 'SORVETE', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=10,column=0)
text_caipirinha = Label(root, text= 'CAIPIRINHA', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=11,column=0)
text_agua = Label(root, text= 'ÁGUA', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID, 
        justify=LEFT, width= 14).grid(row=12,column=0)
text_agua_gas =Label(root, text= 'ÁGUA/GAS', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=13,column=0)
text_marmitex = Label(root, text= 'MARMITEX', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=14,column=0)
text_pinga =Label(root, text= 'PINGA', font='arial 14',bg='#e6ccb3', bd = 1, relief=SOLID,
         justify=LEFT, width= 14).grid(row=15,column=0)



btn = Button(root, text='SOMAR', command=somar).place(x=250, y=120)




#valor = (qtdn_ref * refeição) + (qtdn_meia * meia) + (qtdn_lata * lata) + (qtdn_suco * suco) + (qtdn_heineken*heineken) + (qtdn_original * original) + (qtdn_skol * skol) + (qtdn_sorvete * sorvete) + (qtdn_caipirinha * caipirinha) + (qtdn_agua * agua) + (qtdn_agua_gas * agua_gas) + (qtdn_marmitex * marmitex) + (qtdn_pinga * pinga)





root.mainloop()