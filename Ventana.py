from tkinter import *
from Escuderia import *

color1="gray20"

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
        self.__entryN.delete(0,END)
        self.__entryE.delete(0,END)
        self.__entryNa.delete(0,END)
        self.__entryT.delete(0,END)
        self.__entryC.delete(0,END)
        self.__entryD.delete(0,END)
        self.__entryF.delete(0,END)
        newPiloto=Piloto(nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas)
        self.__laEscuderia.addPiloto(newPiloto)
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        myEscuderia = Escuderia("Alpine","Cartago",["Coca Cola","Ranchitas","JET","Cacique","Bimbo"],Drivers,Cars)
        write_inicial(myEscuderia)
        
    #---------------------------------------------------
    #Crea las escuderias
    def crear_pilotos_autos(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Escuderias")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("logo.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        self.fondoescuderias=PhotoImage(file="Fotos/fondoescuderias.png")
        canvas.create_image(0,0,image=self.fondoescuderias,anchor=NW)
        canvas.pack()
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) 
        self.aboutmenu.add_command(label="Como Útilizar")
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) 
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)    
        canvas.create_text(150,75,anchor=NW,text="Crear Piloto",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(150,130,anchor=NW,text="Nombre",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,180,anchor=NW,text="Edad",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,230,anchor=NW,text="Nacionalidad",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,280,anchor=NW,text="Temporada",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,330,anchor=NW,text="Competencias",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,380,anchor=NW,text="Destacadas",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,430,anchor=NW,text="Fallidas",font=("Fixedsys","17"),fill="black")
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
        canvas.create_text(600,75,anchor=NW,text="Editar Piloto",font=("Fixedsys","20","bold"),fill="black")

        
        self.__pilotosselect = StringVar(self.__master)
        self.__pilotosselect.set("Seleccionar piloto")
        self.__select = self.actOptionMenu()
        self.__select.config()
        self.__select.place(x=850,y=130)
        canvas.create_text(600,180,anchor=NW,text="Nuevo Nombre",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,230,anchor=NW,text="Nueva Edad",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,280,anchor=NW,text="Nueva Nacionalidad",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,330,anchor=NW,text="Nueva Temporada",font=("Fixedsys","17"),fill="black")
        self.__entryEditNombre = Entry(self.__master)
        self.__entryEditNombre.place(x=850, y=180)
        self.__entryEditEdad = Entry(self.__master)
        self.__entryEditEdad.place(x=850, y=230)
        self.__entryEditNacionalidad = Entry(self.__master)
        self.__entryEditNacionalidad.place(x=850, y=280)
        self.__entryEditTemporada = Entry(self.__master)
        self.__entryEditTemporada.place(x=850, y=330)
        
        self.__btnEdit = Button(self.__master,text="Editar",command=lambda: self.editPiloto(self.__pilotosselect.get()))
        self.__btnEdit.place(x=850,y=380)
        self.__btnGuardar =Button(self.__master,text="Guardar",command=lambda:self.guardaInfo(self.__pilotosselect.get()))
        self.__btnGuardar.place(x=900,y=380)
    #------------------------------------------------------
    #Actualiza el optionmenu
    def actOptionMenu(self):
        
        lista=[]
        for i in self.__laEscuderia.getPilotos():
            nombre = i.getNombrePiloto()
            lista.append(nombre)
        menu = OptionMenu(self.__master,self.__pilotosselect,*lista)
        return menu
    #-----------------------------------------------------
    #Editar Personaje
    def editPiloto(self,piloto):
        self.__entryEditNombre.delete(0,END)
        self.__entryEditEdad.delete(0,END)
        self.__entryEditNacionalidad.delete(0,END)
        self.__entryEditTemporada.delete(0,END)
        
        for i in self.__laEscuderia.getPilotos():
            if i.getNombrePiloto() == piloto:
                pilotoSelect = i
                break
        
        self.__entryEditNombre.insert(0,pilotoSelect.getNombrePiloto())
        self.__entryEditEdad.insert(0,pilotoSelect.getEdad())
        self.__entryEditNacionalidad.insert(0,pilotoSelect.getNacionalidad())
        self.__entryEditTemporada.insert(0,pilotoSelect.getTemporada())
    #-------------------------------------------------------
    #GuardaEdit
    def guardaInfo(self,piloto):
        for i in self.__laEscuderia.getPilotos():
            if i.getNombrePiloto() == piloto:
                pilotoSelect = i
                break
        pilotoSelect.setNombre(self.__entryEditNombre.get())
        pilotoSelect.setEdad(self.__entryEditEdad.get())
        pilotoSelect.setNacionalidad(self.__entryEditNacionalidad.get())
        pilotoSelect.setTemporada(self.__entryEditTemporada.get())
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        myEscuderia = Escuderia("Alpine","Cartago",["Coca Cola","Ranchitas","JET","Cacique","Bimbo"],Drivers,Cars)
        write_inicial(myEscuderia)
        self.__entryEditNombre.delete(0,END)
        self.__entryEditEdad.delete(0,END)
        self.__entryEditNacionalidad.delete(0,END)
        self.__entryEditTemporada.delete(0,END)
        self.inicio()
        
    #-------------------------------------------------
    #Enseña la tabla de posiciones
    def position_table(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Tablas de Posiciones")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("pilot.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="fpilotos.png")
        canvas.create_image(0,0,image=self.fondopilotos,anchor=NW)
        canvas.create_text(25,50,anchor=NW,text="1",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(25,175,anchor=NW,text="2",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(25,300,anchor=NW,text="3",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(25,425,anchor=NW,text="4",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(25,550,anchor=NW,text="5",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(525,50,anchor=NW,text="6",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(525,175,anchor=NW,text="7",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(525,300,anchor=NW,text="8",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(525,425,anchor=NW,text="9",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(510,550,anchor=NW,text="10",font=("Fixedsys","20","bold"),fill="black")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) #Agregar comandos
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
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
        self.__master.iconbitmap("credits.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondo=PhotoImage(file="Fotos/Fondo.gif")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        canvas.create_text(50,50,anchor=NW,text="Instituto Tecnologico de Costa Rica",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,100,anchor=NW,text="Kenneth Quirós Torres\n2019243813",font=("Fixedsys","14","bold"),fill=color1)
        self.fotoK=PhotoImage(file="Fotos/Kenneth.gif")
        canvas.create_image(650,100,image=self.fotoK,anchor=NW)
        canvas.create_text(50,150,anchor=NW,text="Yonathan Monge Sanabria\n2019308543",font=("Fixedsys","14","bold"),fill=color1)    
        self.fotoY=PhotoImage(file="Fotos/Yonathan.png")
        canvas.create_image(950,100,image=self.fotoY,anchor=NW)
        canvas.create_text(50,200,anchor=NW,text="Ingenieria en Computadores",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,250,anchor=NW,text="Taller de Programacion",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,300,anchor=NW,text="Grupo5",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,350,anchor=NW,text="Alejandro Vargas Chaves",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,400,anchor=NW,text="Costa Rica",font=("Fixedsys","14","bold"),fill=color1)
        canvas.create_text(50,450,anchor=NW,text="Version 1.1",font=("Fixedsys","14","bold"),fill=color1)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias") #Agregar comandos
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=self.crear_pilotos_autos)
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
        self.fondo=PhotoImage(file="fprincipal.png")
        self.__master.iconbitmap("principal.ico")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        canvas.create_text(50,150,anchor=NW,text="Indice Ganador de Escudería",font=("Fixedsys","20","bold"),fill="black")
        self.__entryEditTemporada = Entry(self.__master)
        self.__entryEditTemporada.place(x=100,y=50)
        self.__btnEditTemporada = Button(self.__master,text="Editar",command=lambda:self.editTemporada(self.__entryEditTemporada.get()))
        self.__btnEditTemporada.place(x=150,y=50)
        self.__temporada = StringVar(self.__entryEditTemporada)
        
        canvas.create_text(50,50,anchor=NW,text="Temporada",font=("Fixedsys","20","bold"),fill="black")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar")#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        self.__logoEscuderia = PhotoImage(file="Fotos/Escuderia_2.gif")
        canvas.create_image(1050,165,image=self.__logoEscuderia)
        
        
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
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) 
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) 
        self.aboutmenu.add_command(label="Como Útilizar")
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
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
        self.optionsmenu.add_command(label="Escuderias",command=self.crear_pilotos_autos) #Agregar comandos
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
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
