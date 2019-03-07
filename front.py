#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
  

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Cairo", "14")
        self.primeiroContainer = Frame(master, bg = '#383428')
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master, bg = '#383428')
        self.segundoContainer["padx"] = 40
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master, bg = '#383428')
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master, bg = '#383428')
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Eletrodomésticos")
        self.titulo["font"] = ("Cairo", "14", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Gasolina", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Eletricidade", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Okay"
        self.autenticar["font"] = ("Cairo", "12",)
        self.autenticar["width"] = 12
        
        self.autenticar.pack()

  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def autenticar(self):
    	
    	self.newWindow = Toplevel(self.master)
    	self.app = Application2(self.newWindow)
    	#self.master.destroy()






class Application2:
    def __init__(self, master = None):
        self.fontePadrao = ("Cairo", "14")
        self.primeiroContainer = Frame(master, bg = '#383428')
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master, bg = '#383428')
        self.segundoContainer["padx"] = 40
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master, bg = '#383428')
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master, bg = '#383428')
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Carros")
        self.titulo["font"] = ("Cairo", "14", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Gasolina", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Eletricidade", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Yay"
        self.autenticar["font"] = ("Cairo", "12",)
        self.autenticar["width"] = 12
        
        self.autenticar.pack()

  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def autenticar(self):
    	self.master.destroy()
    	self.newWindow = Toplevel(self.master)
    	self.app = Application2(self.newWindow)

  
'''

class Demo1:
    def __init__(self, master):
    	
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = 'New Window', width = 500, height = 500, command = self.new_window, bg = "#383428")
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):

        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text = 'Quit', width = 500, height = 500, command = self.close_windows, bg = "#3834328")
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = Tk()
    root.title("Calculadora de Consumo Energético e CO2")
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main() 
  
'''  
def main():
	root = Tk()
	app = Application(root)
	root.title("Calculadora de CO2 equivalente")
	root.configure(background='#383428')
	windowWidth = root.winfo_reqwidth()
	windowHeight = root.winfo_reqheight()
	positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2 - windowWidth*0.2)
	positionDown = int(root.winfo_screenheight()/2 - windowHeight/2 - windowHeight*0.4)
	root.geometry("+{}+{}".format(positionRight, positionDown))
	root.mainloop()

if __name__ == '__main__':
	main()
