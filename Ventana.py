from tkinter import *
from Escuderia import *
color1="gray20"

class Ventana_inicio(Frame):


    def __init__(self,master):
        self.__master = master
        self.__escuderias={}
        
        self.inicio()
        return
    #---------------------------------------------------
    #Crea las escuderias
    def show_escuderias(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Escuderias")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("logo.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="fondoescuderias.png")
        canvas.create_image(0,0,image=self.fondopilotos,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        optionsescuderias=self.getEscuderias
        for escuderia in optionescuderias:
            selectescuderia = StringVar(self.__master)
            selectescuderia.set("Seleccione la Escuderia")
            self.optionescuderia=apply(OptionMenu,(self.__master,selectescuderia)+list(optionescuderia))
            self.optionescuderia.pack()    
    
    #Enseña la tabla de posiciones
    def position_table(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Tabla de posiciones")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("pilot.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="fpilotos.png")
        canvas.create_image(0,0,image=self.fondopilotos,anchor=NW)
        self.driver1=PhotoImage(file="valtteri.png")
        canvas.create_image(50,50,image=self.driver1,anchor=NW)
        self.driver2=PhotoImage(file="antonio.png")
        canvas.create_image(50,175,image=self.driver2,anchor=NW)
        self.driver3=PhotoImage(file="carlos.png")
        canvas.create_image(50,300,image=self.driver3,anchor=NW)
        self.driver4=PhotoImage(file="daniil.png")
        canvas.create_image(50,425,image=self.driver4,anchor=NW)
        self.driver5=PhotoImage(file="george.png")
        canvas.create_image(50,550,image=self.driver5,anchor=NW)
        self.driver6=PhotoImage(file="nico.png")
        canvas.create_image(650,50,image=self.driver6,anchor=NW)
        self.driver7=PhotoImage(file="pierre.png")
        canvas.create_image(650,175,image=self.driver7,anchor=NW)
        self.driver8=PhotoImage(file="romain.png")
        canvas.create_image(650,300,image=self.driver8,anchor=NW)
        self.driver9=PhotoImage(file="sebastian.png")
        canvas.create_image(650,425,image=self.driver9,anchor=NW)
        self.driver10=PhotoImage(file="sergio.png")
        canvas.create_image(650,550,image=self.driver10,anchor=NW)
        self.menuvar = Menu(self.__master)
        canvas.create_text(25,50,anchor=NW,text="1",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(25,175,anchor=NW,text="2",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(25,300,anchor=NW,text="3",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(25,425,anchor=NW,text="4",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(25,550,anchor=NW,text="5",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(625,50,anchor=NW,text="6",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(625,175,anchor=NW,text="7",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(625,300,anchor=NW,text="8",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(625,425,anchor=NW,text="9",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(610,550,anchor=NW,text="10",font=("Fixedsys","20","bold"),fill=color1)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)

        
        
    #Enseñar la información de ayuda
    def show_about(self):
        #Iteracion para borrar el contenido de la pantalla e inicializar el frame
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("About")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("credits.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondo=PhotoImage(file="Fondo.gif")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        canvas.create_text(50,50,anchor=NW,text="Instituto Tecnologico de Costa Rica",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,100,anchor=NW,text="Kenneth Quirós Torres\n2019243813",font=("Fixedsys","14","bold"),fill=color1)
        self.fotoK=PhotoImage(file="Kenneth.gif")
        canvas.create_image(650,100,image=self.fotoK,anchor=NW)
        canvas.create_text(50,150,anchor=NW,text="Yonathan Monge Sanabria\n2019308543",font=("Fixedsys","14","bold"),fill=color1)    
        self.fotoY=PhotoImage(file="Yonathan.png")
        canvas.create_image(950,100,image=self.fotoY,anchor=NW)
        canvas.create_text(50,200,anchor=NW,text="Ingenieria en Computadores",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,250,anchor=NW,text="Taller de Programacion",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,300,anchor=NW,text="Grupo5",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,350,anchor=NW,text="Alejandro Vargas Chaves",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,400,anchor=NW,text="Costa Rica",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,450,anchor=NW,text="Version 1.1",font=("Fixedsys","14","bold"),fill=color1)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=self.show_escuderias)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        #---------------------------------------------------
         
    def inicio(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master,background="black")

        #---------------------------------------------------
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        
        self.__master.title("Formula E CE TEC")
        self.fondo=PhotoImage(file="fprincipal.png")
        self.__master.iconbitmap("principal.ico")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        self.carrito=PhotoImage(file="carrito.png")
        canvas.create_image(600,50,image=self.carrito,anchor=NW)
        canvas.create_text(50,50,anchor=NW,text="Temporada 2019",font=("Fixedsys","20","bold"),fill=color1)
        canvas.create_text(50,150,anchor=NW,text="Indice Ganador de Escudería",font=("Fixedsys","20","bold"),fill=color1)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        return

    #Funcion para crear ventana donde se mostrara el Test Drive
    def show_testdrive(self):
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Test Drive")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("engranaje.ico")
        self.informacion= PhotoImage(file="interior.png")
        canvas.create_image(0,0,image=self.informacion,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
    #Funcion para crear menu que mostrara los carros 
    def show_automoviles(self):
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Automóviles")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("racecar.ico")
        self.fondoam= PhotoImage(file="fautos2.png")
        canvas.create_image(0,0,image=self.fondoam,anchor=NW)

        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.show_escuderias) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        
    
root= Tk()
root.geometry("1280x800")

iniciar = Ventana_inicio(root)
root.mainloop()
