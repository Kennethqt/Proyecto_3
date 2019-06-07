from tkinter import *
from Escuderia import *
from Piloto import *
from Pickle import *
class Ventana_inicio(Frame):

    def __init__(self,master):
        self.__master = master
        self.__laEscuderia = read()
        self.inicio()
        

        return
    #--------------------------------------------------
    #Print Escuderia
    def printInfo(self):
        Esc = self.__laEscuderia
        Name = Esc.getNombre()
        Location = Esc.getUbicacion()
        Sponsors = Esc.getPatrocinadores()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()           
    #--------------------------------------------------
    #Crear piloto
    def newPiloto(self,nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas):
        newPiloto=Piloto(nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas)
        self.__laEscuderia.addPiloto(newPiloto)
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        myEscuderia = Escuderia("Alpine","Cartago",["Coca Cola","Ranchitas","JET","Cacique","Bimbo"],Drivers,Cars)
        write_inicial(myEscuderia)
        self.__entryN.delete(0,END)
        self.__entryE.delete(0,END)
        self.__entryNa.delete(0,END)
        self.__entryT.delete(0,END)
        self.__entryC.delete(0,END)
        self.__entryD.delete(0,END)
        self.__entryF.delete(0,END)
    #---------------------------------------------------
    #Crea las escuderias
    def crear_pilotos_autos(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Escuderias")
        self.__master.geometry("1280x800")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="fondoescuderias.png")
        canvas.create_image(0,0,image=self.fondopilotos,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles")#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View") #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        canvas.create_text(150,75,anchor=NW,text="Crear Piloto",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(150,130,anchor=NW,text="Nombre",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,180,anchor=NW,text="Edad",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,230,anchor=NW,text="Nacionalidad",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,280,anchor=NW,text="Temporada",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,330,anchor=NW,text="Competencias",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,380,anchor=NW,text="Destacadas",font=("Fixedsys","17"),fill="grey92")
        canvas.create_text(150,430,anchor=NW,text="Fallidas",font=("Fixedsys","17"),fill="grey92")
        self.__entryN=Entry(self.__master)
        self.__entryN.place(x=300,y=130)
        self.__entryE=Entry(self.__master)
        self.__entryE.place(x=300,y=180)
        self.__entryNa=Entry(self.__master)
        self.__entryNa.place(x=300,y=230)
        self.__entryT=Entry(self.__master)
        self.__entryT.place(x=300,y=280)
        self.__entryC=Entry(self.__master)
        self.__entryC.place(x=300,y=330)
        self.__entryD=Entry(self.__master)
        self.__entryD.place(x=300,y=380)
        self.__entryF=Entry(self.__master)
        self.__entryF.place(x=300,y=430)
        self.__btnCrearPiloto = Button(self.__master,text="Crear Piloto",command=lambda: self.newPiloto(self.__entryN.get(),self.__entryE.get(),self.__entryNa.get(),
                                                                                                        self.__entryT.get(),self.__entryC.get(),self.__entryD.get(),self.__entryF.get()))
        self.__btnCrearPiloto.place(x=200,y=550)

        
    #-------------------------------------------------
    #
    #-------------------------------------------------
    #Enseña la tabla de posiciones
    def position_table(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Tablas de Posiciones")
        self.__master.geometry("1280x800")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="pilotos.png")
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
        canvas.create_image(550,50,image=self.driver6,anchor=NW)
        self.driver7=PhotoImage(file="pierre.png")
        canvas.create_image(550,175,image=self.driver7,anchor=NW)
        self.driver8=PhotoImage(file="romain.png")
        canvas.create_image(550,300,image=self.driver8,anchor=NW)
        self.driver9=PhotoImage(file="sebastian.png")
        canvas.create_image(550,425,image=self.driver9,anchor=NW)
        self.driver10=PhotoImage(file="sergio.png")
        canvas.create_image(550,550,image=self.driver10,anchor=NW)
        self.menuvar = Menu(self.__master)
        canvas.create_text(25,50,anchor=NW,text="1",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(25,175,anchor=NW,text="2",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(25,300,anchor=NW,text="3",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(25,425,anchor=NW,text="4",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(25,550,anchor=NW,text="5",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(525,50,anchor=NW,text="6",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(525,175,anchor=NW,text="7",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(525,300,anchor=NW,text="8",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(525,425,anchor=NW,text="9",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(510,550,anchor=NW,text="10",font=("Fixedsys","20","bold"),fill="grey92")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles")#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View") #Agregar comando
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
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondo=PhotoImage(file="Fondo.gif")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        canvas.create_text(50,50,anchor=NW,text="Instituto Tecnologico de Costa Rica",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,100,anchor=NW,text="Kenneth Quirós Torres\n2019243813",font=("Fixedsys","14","bold"),fill="grey92")
        self.fotoK=PhotoImage(file="Kenneth.gif")
        canvas.create_image(500,100,image=self.fotoK,anchor=NW)
        canvas.create_text(50,150,anchor=NW,text="Yonathan Monge Sanabria",font=("Fixedsys","14","bold"),fill="grey92")    
        self.fotoY=PhotoImage(file="Yonathan.png")
        canvas.create_image(800,100,image=self.fotoY,anchor=NW)
        canvas.create_text(50,200,anchor=NW,text="Ingenieria en Computadores",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,250,anchor=NW,text="Taller de Programacion",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,300,anchor=NW,text="Grupo5",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,350,anchor=NW,text="Alejandro Vargas Chaves",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,400,anchor=NW,text="Costa Rica",font=("Fixedsys","14","bold"),fill="grey92")
        canvas.create_text(50,450,anchor=NW,text="Version 1.1",font=("Fixedsys","14","bold"),fill="grey92")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias") #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=self.crear_pilotos_autos)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles")#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View") #Agregar comando
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
        self.fondo=PhotoImage(file="fondofuturista.png")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        self.carrito=PhotoImage(file="carrito.png")
        canvas.create_image(600,50,image=self.carrito,anchor=NW)
        canvas.create_text(50,50,anchor=NW,text="Temporada 2019",font=("Fixedsys","20","bold"),fill="grey92")
        canvas.create_text(50,150,anchor=NW,text="Indice Ganador de Escuderia",font=("Fixedsys","20","bold"),fill="grey92")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) #Agregar comandos
        self.optionsmenu.add_command(label="Incio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles")#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View") #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        return

root= Tk()
root.geometry("1280x800")
iniciar = Ventana_inicio(root)
root.mainloop()
