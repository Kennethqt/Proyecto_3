from tkinter import *
from Escuderia import *
from tkinter.filedialog import askopenfilename
color1="gray20"
colorfondo="gray10"
colorletra="white"
from Carro import *
from Piloto import *
from Pickle import *
import os
#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU
import winsound

class Ventana_inicio(Frame):
    
    #Definicion de variables globales


    def __init__(self,master):
        self.__master = master
        self.__laEscuderia = read()
        self.__control_de_luces_frontales=0
        self.__control_de_luces_traseras=0
        self.__direccional_izquierda=0
        self.__direccional_derecha=0
        self.__circulo=1
        self.__dir_derecha=1
        self.__dir_izquierda=-1
        self.__dir_directo=0
        self.inicio()
        return
    #--------------------------------------------------
    #Print Escuderia
    def printInfo(self):
        Esc = self.__laEscuderia
        Name = Esc.getNombre()
        Location = Esc.getUbicacion()
        Sponsors = Esc.getPatrocinadoresLista()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
    #----------------------------------------------------
    #Crea los carros
    def crear_carros(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Automóviles")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/racecar.ico")
        self.fondoam= PhotoImage(file="Fondos/fautos1.png")
        canvas.create_image(0,0,image=self.fondoam,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(150,75,anchor=NW,text="Crear Automovil",font=("Fixedsys","20"),fill="black")       
        canvas.create_text(150,130,anchor=NW,text="Marca",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,180,anchor=NW,text="Modelo",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,230,anchor=NW,text="Pais",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,280,anchor=NW,text="Temporada",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,330,anchor=NW,text="Baterias",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,380,anchor=NW,text="Pilas",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,430,anchor=NW,text="Estado",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,480,anchor=NW,text="Consumo",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,530,anchor=NW,text="Sensores",font=("Fixedsys","17"),fill="red")
        canvas.create_text(150,580,anchor=NW,text="Peso",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,630,anchor=NW,text="Eficiencia",font=("Fixedsys","17"),fill="red")
        #                                      _____________________________________________________
        #_____________________________________/Entrys y botones
        self.__entryMarca = Entry(self.__master)
        self.__entryMarca.place(x=300,y=130)
        self.__entryModelo = Entry(self.__master)
        self.__entryModelo.place(x=300,y=180)
        self.__entryPais = Entry(self.__master)
        self.__entryPais.place(x=300,y=230)
        self.__entryTemporada = Entry(self.__master)
        self.__entryTemporada.place(x=300,y=280)
        self.__entryNumBaterias = Entry(self.__master)
        self.__entryNumBaterias.place(x=300,y=330)
        self.__entryCanPilas = Entry(self.__master)
        self.__entryCanPilas.place(x=300,y=380)
        self.__entryEstado = Entry(self.__master)
        self.__entryEstado.place(x=300,y=430)
        self.__entryConsumo = Entry(self.__master)
        self.__entryConsumo.place(x=300,y=480)
        self.__entrySensores = Entry(self.__master)
        self.__entrySensores.place(x=300,y=530)
        self.__entryPeso = Entry(self.__master)
        self.__entryPeso.place(x=300,y=580)
        self.__entryEficiencia = Entry(self.__master)
        self.__entryEficiencia.place(x=300,y=630)
        self.__btnCrear = Button(self.__master,fg=colorletra,bg=colorfondo,text="Crear",command=lambda:self.newCar(self.__entryMarca.get(),self.__entryModelo.get(),self.__entryPais.get(),self.__entryTemporada.get(),self.__entryNumBaterias.get(),self.__entryCanPilas.get(),self.__entryEstado.get(),self.__entryConsumo.get(),self.__entrySensores.get(),self.__entryPeso.get(),self.__entryEficiencia.get()))
        self.__btnCrear.place(x=300,y=660)
                                            #  _____________________________________________________
        #_____________________________________/Menus

        canvas.create_text(600,75,anchor=NW,text="Editar Automovil",font=("Fixedsys","20"),fill="black")
        canvas.create_text(600,130,anchor=NW,text="Nueva Marca",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,180,anchor=NW,text="Nuevo Modelo",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,230,anchor=NW,text="Nuevo Pais",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,280,anchor=NW,text="Nueva Temporada",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,330,anchor=NW,text="Baterias",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,380,anchor=NW,text="Cantidad de Pilas",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,430,anchor=NW,text="Nuevo Estado",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,480,anchor=NW,text="Consumo",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,530,anchor=NW,text="Sensores",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,580,anchor=NW,text="Nuevo Peso",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,630,anchor=NW,text="Eficiencia",font=("Fixedsys","17"),fill="red4")
        #                                      _____________________________________________________
        #_____________________________________/Entrys y botones        
        self.__carroselect = StringVar(self.__master)
        self.__carroselect.set("Seleccionar Carro")
        self.__select = self.optionMenuCar()
        self.__select.config()
        self.__select.place(x=1025,y=130)
        self.__entryEditMarca = Entry(self.__master)
        self.__entryEditMarca.place(x=850,y=130)
        self.__entryEditModelo = Entry(self.__master)
        self.__entryEditModelo.place(x=850,y=180)
        self.__entryEditPais = Entry(self.__master)
        self.__entryEditPais.place(x=850,y=230)
        self.__entryEditTemporada = Entry(self.__master)
        self.__entryEditTemporada.place(x=850,y=280)
        self.__entryEditNumBaterias = Entry(self.__master)
        self.__entryEditNumBaterias.place(x=850,y=330)
        self.__entryEditCanPilas = Entry(self.__master)
        self.__entryEditCanPilas.place(x=850,y=380)
        self.__entryEditEstado = Entry(self.__master)
        self.__entryEditEstado.place(x=850,y=430)
        self.__entryEditConsumo = Entry(self.__master)
        self.__entryEditConsumo.place(x=850,y=480)
        self.__entryEditSensores = Entry(self.__master)
        self.__entryEditSensores.place(x=850,y=530)
        self.__entryEditPeso = Entry(self.__master)
        self.__entryEditPeso.place(x=850,y=580)
        self.__entryEditEficiencia = Entry(self.__master)
        self.__entryEditEficiencia.place(x=850,y=630)
        self.__btnEditar = Button(self.__master,fg=colorletra,bg=colorfondo,text="Editar",command=lambda:self.editCarro(self.__carroselect.get()))
        self.__btnEditar.place(x=850,y=660)
        self.__btnGuardar = Button(self.__master,fg=colorletra,bg=colorfondo,text="Guardar",command=lambda:self.guardaInfoCar(self.__carroselect.get()))
        self.__btnGuardar.place(x=900,y=660)
    #---------------------------------------------------------------------------------------------------
    #OptionMenu Carros
    def optionMenuCar(self):
        lista=[]
        for i in self.__laEscuderia.getAutomoviles():
            marca = i.getMarca()
            lista.append(marca)
        menu = OptionMenu(self.__master,self.__carroselect, *lista)
        return menu
    #---------------------------------------------------------------------------------------------------
    #Crear Auto
    def newCar(self,marca,modelo,pais,temporada,baterias,pilas,estado,consumo,sensores,peso,eficiencia):
        self.__entryMarca.delete(0,END)
        self.__entryModelo.delete(0,END)
        self.__entryPais.delete(0,END)
        self.__entryTemporada.delete(0,END)
        self.__entryNumBaterias.delete(0,END)
        self.__entryCanPilas.delete(0,END)
        self.__entryEstado.delete(0,END)
        self.__entryConsumo.delete(0,END)
        self.__entrySensores.delete(0,END)
        self.__entryPeso.delete(0,END)
        self.__entryEficiencia.delete(0,END)
        self.__rutaImagen = askopenfilename()
        self.__imagen = os.path.abspath(self.__rutaImagen)
        foto=self.__imagen
        newCar = Carro(marca,modelo,pais,temporada,baterias,pilas,estado,consumo,sensores,peso,eficiencia,foto)
        self.__laEscuderia.addAutomovil(newCar)
        logo = self.__laEscuderia.getLogo()
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Sponsors = Esc.getPatrocinadoresLista()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia) 
    #--------------------------------------------------
    #Crear piloto
    def newPiloto(self,nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas):
        #                                      _____________________________________________________
        #_____________________________________/Guarda info        
        self.__entryN.delete(0,END)
        self.__entryE.delete(0,END)
        self.__entryNa.delete(0,END)
        self.__entryT.delete(0,END)
        self.__entryC.delete(0,END)
        self.__entryD.delete(0,END)
        self.__entryF.delete(0,END)
        self.__rutaImagen = askopenfilename()
        self.__imagen = os.path.abspath(self.__rutaImagen)
        foto = self.__imagen
        newPiloto=Piloto(nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas,foto)
        self.__laEscuderia.addPiloto(newPiloto)
        logo = self.__laEscuderia.getLogo()
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Sponsors = Esc.getPatrocinadoresLista()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        
    #---------------------------------------------------
    #Crea los pilotos
    def crear_pilotos(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame        
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Escuderias")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/logo.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        self.fondoescuderias=PhotoImage(file="Fondos/fondoescuderias.png")
        canvas.create_image(0,0,image=self.fondoescuderias,anchor=NW)
        canvas.pack()
        #                                      _____________________________________________________
        #_____________________________________/Menu         
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) 
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) 
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(150,75,anchor=NW,text="Crear Piloto",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(150,130,anchor=NW,text="Nombre",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,180,anchor=NW,text="Edad",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,230,anchor=NW,text="Nacionalidad",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,280,anchor=NW,text="Temporada",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,330,anchor=NW,text="Competencias",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,380,anchor=NW,text="Destacadas",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(150,430,anchor=NW,text="Fallidas",font=("Fixedsys","17"),fill="red4")
        #                                      _____________________________________________________
        #_____________________________________/Entrys y botones
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
        self.__btnCrearPiloto = Button(self.__master,fg=colorletra,bg=colorfondo,text="Crear Piloto",command=lambda: self.newPiloto(self.__entryN.get(),self.__entryE.get(),self.__entryNa.get(),
                                                                                                        self.__entryT.get(),self.__entryC.get(),self.__entryD.get(),self.__entryF.get()))
        self.__btnCrearPiloto.place(x=200,y=550)
        canvas.create_text(600,75,anchor=NW,text="Editar Piloto",font=("Fixedsys","20","bold"),fill="black")

        
        self.__pilotosselect = StringVar(self.__master)
        self.__pilotosselect.set("Seleccionar piloto")
        self.__select = self.actOptionMenu()
        self.__select.config()
        self.__select.place(x=850,y=130)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(600,180,anchor=NW,text="Nuevo Nombre",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,230,anchor=NW,text="Nueva Edad",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,280,anchor=NW,text="Nueva Nacionalidad",font=("Fixedsys","17"),fill="red4")
        canvas.create_text(600,330,anchor=NW,text="Nueva Temporada",font=("Fixedsys","17"),fill="red4")
        #                                      _____________________________________________________
        #_____________________________________/Entrys y Botones 
        self.__entryEditNombre = Entry(self.__master)
        self.__entryEditNombre.place(x=850, y=180)
        self.__entryEditEdad = Entry(self.__master)
        self.__entryEditEdad.place(x=850, y=230)
        self.__entryEditNacionalidad = Entry(self.__master)
        self.__entryEditNacionalidad.place(x=850, y=280)
        self.__entryEditTemporada = Entry(self.__master)
        self.__entryEditTemporada.place(x=850, y=330)
        
        self.__btnEdit = Button(self.__master,fg=colorletra,bg=colorfondo,text="Editar",command=lambda: self.editPiloto(self.__pilotosselect.get()))
        self.__btnEdit.place(x=850,y=380)
        self.__btnGuardar =Button(self.__master,fg=colorletra,bg=colorfondo,text="Guardar",command=lambda:self.guardaInfo(self.__pilotosselect.get()))
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
    #Editar Carro
    def editCarro(self,carro):
        #                                      _____________________________________________________
        #_____________________________________/Guarda Info Carro 
        self.__entryEditMarca.delete(0,END)
        self.__entryEditModelo.delete(0,END)
        self.__entryEditPais.delete(0,END)
        self.__entryEditTemporada.delete(0,END)
        self.__entryEditNumBaterias.delete(0,END)
        self.__entryEditCanPilas.delete(0,END)
        self.__entryEditEstado.delete(0,END)
        self.__entryEditConsumo.delete(0,END)
        self.__entryEditSensores.delete(0,END)
        self.__entryEditPeso.delete(0,END)
        self.__entryEditEficiencia.delete(0,END)
        
        for i in self.__laEscuderia.getAutomoviles():
            if i.getMarca() == carro:
                carroSelect = i
                break
        self.__entryEditMarca.insert(0,carroSelect.getMarca())
        self.__entryEditModelo.insert(0,carroSelect.getModelo())
        self.__entryEditPais.insert(0,carroSelect.getPais())
        self.__entryEditTemporada.insert(0,carroSelect.getTemporada())
        self.__entryEditNumBaterias.insert(0,carroSelect.getNumBaterias())
        self.__entryEditCanPilas.insert(0,carroSelect.getCanPilas())
        self.__entryEditEstado.insert(0,carroSelect.getEstado())
        self.__entryEditConsumo.insert(0,carroSelect.getConsumo())
        self.__entryEditSensores.insert(0,carroSelect.getSensores())
        self.__entryEditPeso.insert(0,carroSelect.getPeso())
        self.__entryEditEficiencia.insert(0,carroSelect.getEficiencia())
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
    #-----------------------------------------------------------------
    #GuardaEditCarros
    def guardaInfoCar(self,carro):
        #                                      _____________________________________________________
        #_____________________________________/Guarda info carro
        for i in self.__laEscuderia.getAutomoviles():
            if i.getMarca() == carro:
                carroSelect = i
                break
        carroSelect.setMarca(self.__entryEditMarca.get())
        carroSelect.setModelo(self.__entryEditModelo.get())
        carroSelect.setPais(self.__entryEditPais.get())
        carroSelect.setTemporada(self.__entryEditTemporada.get())
        carroSelect.setNumBaterias(self.__entryEditNumBaterias.get())
        carroSelect.setCanPilas(self.__entryEditCanPilas.get())
        carroSelect.setEstado(self.__entryEditEstado.get())
        carroSelect.setConsumo(self.__entryEditConsumo.get())
        carroSelect.setSensores(self.__entryEditSensores.get())
        carroSelect.setPeso(self.__entryEditPeso.get())
        carroSelect.setEficiencia(self.__entryEditEficiencia.get())
        Esc = self.__laEscuderia
        logo = self.__laEscuderia.getLogo()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Sponsors = Esc.getPatrocinadoresLista()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        self.__entryEditMarca.delete(0,END)
        self.__entryEditModelo.delete(0,END)
        self.__entryEditPais.delete(0,END)
        self.__entryEditTemporada.delete(0,END)
        self.__entryEditNumBaterias.delete(0,END)
        self.__entryEditCanPilas.delete(0,END)
        self.__entryEditEstado.delete(0,END)
        self.__entryEditConsumo.delete(0,END)
        self.__entryEditSensores.delete(0,END)
        self.__entryEditPeso.delete(0,END)
        self.__entryEditEficiencia.delete(0,END)
        self.inicio()
    #-------------------------------------------------------
    #GuardaEdit
    def guardaInfo(self,piloto):
        #                                      _____________________________________________________
        #_____________________________________/Guarda Info piloto 
        for i in self.__laEscuderia.getPilotos():
            if i.getNombrePiloto() == piloto:
                pilotoSelect = i
                break
        pilotoSelect.setNombre(self.__entryEditNombre.get())
        pilotoSelect.setEdad(self.__entryEditEdad.get())
        pilotoSelect.setNacionalidad(self.__entryEditNacionalidad.get())
        pilotoSelect.setTemporada(self.__entryEditTemporada.get())
        Esc = self.__laEscuderia
        logo = self.__laEscuderia.getLogo()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Sponsors = Esc.getPatrocinadoresLista()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        self.__entryEditNombre.delete(0,END)
        self.__entryEditEdad.delete(0,END)
        self.__entryEditNacionalidad.delete(0,END)
        self.__entryEditTemporada.delete(0,END)
        self.inicio()
        
    #-------------------------------------------------
    #Enseña la tabla de posiciones
    def position_table(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master)
        self.__master.title("Tablas de Posiciones")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/pilot.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondopilotos=PhotoImage(file="Fondos/fpilotos.png")
        canvas.create_image(0,0,image=self.fondopilotos,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/     Textos
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
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)

                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(150,15,anchor=NW,text="Piloto",font=("Fixedsys","14"),fill="red")
        canvas.create_text(250,15,anchor=NW,text="Competencias",font=("Fixedsys","14"),fill="red")
        canvas.create_text(425,15,anchor=NW,text="REP",font=("Fixedsys","14"),fill="red")
        #PILOTO 1
        self.__photo1 = PhotoImage(file="Fotos/sebastian.png")
        canvas.create_image(50,52,image=self.__photo1,anchor=NW)
        drivername1 = canvas.create_text(150,50,anchor=NW,text="Sebastian Vettel",font=("Fixedsys","10"),fill="black")
        driveredad1= canvas.create_text(150,70,anchor=NW,text="32",font=("Fixedsys","10"),fill="black")
        drivernacionalidad1 = canvas.create_text(150,90,anchor=NW,text="Alemán",font=("Fixedsys","10"),fill="black")
        drivertemporada1 = canvas.create_text(150,110,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias1 = canvas.create_text(325,50,anchor=NW,text="49",font=("Fixedsys","10"),fill="black")
        driverrgp1 = canvas.create_text(425,50,anchor=NW,text="61,54",font=("Fixedsys","10"),fill="black")
        
        #PILOTO 2
        self.__photo2 = PhotoImage(file="Fotos/valtteri.png")
        canvas.create_image(50,178,image=self.__photo2,anchor=NW)
        drivername2 = canvas.create_text(150,175,anchor=NW,text="Valtteri Bottas",font=("Fixedsys","10"),fill="black")
        driveredad2 = canvas.create_text(150,195,anchor=NW,text="30",font=("Fixedsys","10"),fill="black")
        drivernacionalidad2 = canvas.create_text(150,215,anchor=NW,text="Finlandés",font=("Fixedsys","10"),fill="black")
        drivertemporada2 = canvas.create_text(150,235,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias2 = canvas.create_text(325,175,anchor=NW,text="68",font=("Fixedsys","10"),fill="black")
        driverrgp2 = canvas.create_text(425,175,anchor=NW,text="60,00",font=("Fixedsys","10"),fill="black")
        
        #PILOTO3
        self.__photo3 = PhotoImage(file="Fotos/sergio.png")
        canvas.create_image(50,304,image=self.__photo3,anchor=NW)
        drivername3 = canvas.create_text(150,300,anchor=NW,text="Sergio Pérez",font=("Fixedsys","10"),fill="black")
        driveredad3 = canvas.create_text(150,320,anchor=NW,text="29",font=("Fixedsys","10"),fill="black")
        drivernacionalidad3 = canvas.create_text(150,340,anchor=NW,text="Mexicano",font=("Fixedsys","10"),fill="black")
        drivertemporada3 = canvas.create_text(150,360,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias3 = canvas.create_text(325,300,anchor=NW,text="57",font=("Fixedsys","10"),fill="black")
        driverrgp3 = canvas.create_text(425,300,anchor=NW,text="60,47",font=("Fixedsys","10"),fill="black")

        #PILOTO 4
        self.__photo4 = PhotoImage(file="Fotos/romain.png")
        canvas.create_image(50,430,image=self.__photo4,anchor=NW)
        drivername4 = canvas.create_text(150,425,anchor=NW,text="Romain Grosjean",font=("Fixedsys","10"),fill="black")
        driveredad4 = canvas.create_text(150,445,anchor=NW,text="35",font=("Fixedsys","10"),fill="black")
        drivernacionalidad4 = canvas.create_text(150,465,anchor=NW,text="Francés",font=("Fixedsys","10"),fill="black")
        drivertemporada4 = canvas.create_text(150,485,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias4 = canvas.create_text(325,425,anchor=NW,text="70",font=("Fixedsys","10"),fill="black")
        driverrgp4 = canvas.create_text(425,425,anchor=NW,text="58,49",font=("Fixedsys","10"),fill="black")

        #PILOTO 5
        self.__photo5 = PhotoImage(file="Fotos/nico.png")
        canvas.create_image(50,556,image=self.__photo5,anchor=NW)
        drivername5 = canvas.create_text(150,550,anchor=NW,text="Nico Hulkenberg",font=("Fixedsys","10"),fill="black")
        driveredad5 = canvas.create_text(150,570,anchor=NW,text="32",font=("Fixedsys","10"),fill="black")
        drivernacionalidad5 = canvas.create_text(150,590,anchor=NW,text="Alemán",font=("Fixedsys","10"),fill="black")
        drivertemporada5 = canvas.create_text(150,610,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias5 = canvas.create_text(325,550,anchor=NW,text="64",font=("Fixedsys","10"),fill="black")
        driverrgp5 = canvas.create_text(425,550,anchor=NW,text="55,56",font=("Fixedsys","10"),fill="black")

        #PILOTO 6
        self.__photo6 = PhotoImage(file="Fotos/carlos.png")
        canvas.create_image(552,52,image=self.__photo6,anchor=NW)
        drivername6 = canvas.create_text(650,50,anchor=NW,text="Carlos Sainz",font=("Fixedsys","10"),fill="black")
        driveredad6 = canvas.create_text(650,70,anchor=NW,text="25",font=("Fixedsys","10"),fill="black")
        drivernaciolidad6 = canvas.create_text(650,90,anchor=NW,text="Español",font=("Fixedsys","10"),fill="black")
        drivertemporada6 = canvas.create_text(650,110,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias6 = canvas.create_text(875,50,anchor=NW,text="49",font=("Fixedsys","10"),fill="white")
        driverrgp6 = canvas.create_text(1000,50,anchor=NW,text="55.26",font=("Fixedsys","10"),fill="white")
        
        #PILOTO 7
        self.__photo7 = PhotoImage(file="Fotos/antonio.png")
        canvas.create_image(552,178,image=self.__photo7,anchor=NW)
        drivername7 = canvas.create_text(650,175,anchor=NW,text="Antonio Giovinazzi",font=("Fixedsys","10"),fill="black")
        driveredad7 = canvas.create_text(650,195,anchor=NW,text="26",font=("Fixedsys","10"),fill="black")
        drivernacionalidad7 = canvas.create_text(650,215,anchor=NW,text="Italiano",font=("Fixedsys","10"),fill="black")
        drivertemporada7 = canvas.create_text(650,235,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias7 = canvas.create_text(875,175,anchor=NW,text="59",font=("Fixedsys","10"),fill="black")
        driverrgp7 = canvas.create_text(1000,175,anchor=NW,text="48,94",font=("Fixedsys","10"),fill="black")

        #PILOTO 8
        self.__photo8 = PhotoImage(file="Fotos/daniil.png")
        canvas.create_image(552,304,image=self.__photo8,anchor=NW)
        drivername8 = canvas.create_text(650,300,anchor=NW,text="Daniil Kvyat",font=("Fixedsys","10"),fill="black")
        driveredad8 = canvas.create_text(650,320,anchor=NW,text="25",font=("Fixedsys","10"),fill="black")
        drivernacionalidad8 = canvas.create_text(650,340,anchor=NW,text="Ruso",font=("Fixedsys","10"),fill="black")
        drivertemporada8 = canvas.create_text(650,360,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias8 = canvas.create_text(875,300,anchor=NW,text="55",font=("Fixedsys","10"),fill="black")
        driverrgp8 = canvas.create_text(1000,300,anchor=NW,text="40,43",font=("Fixedsys","10"),fill="black")

        #PILOTO 9
        self.__photo9 = PhotoImage(file="Fotos/george.png")
        canvas.create_image(552,430,image=self.__photo9,anchor=NW)
        drivername9 = canvas.create_text(650,425,anchor=NW,text="George Russell",font=("Fixedsys","10"),fill="black")
        driveredad9 = canvas.create_text(650,445,anchor=NW,text="21",font=("Fixedsys","10"),fill="black")
        drivernacionalidad9 = canvas.create_text(650,465,anchor=NW,text="Inglés",font=("Fixedsys","10"),fill="black")
        drivertemporada9 = canvas.create_text(650,485,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias9 = canvas.create_text(875,425,anchor=NW,text="40",font=("Fixedsys","10"),fill="black")
        driverrgp9 = canvas.create_text(1000,425,anchor=NW,text="30,56",font=("Fixedsys","10"),fill="black")

        #PILOTO 10
        self.__photo10 = PhotoImage(file="Fotos/pierre.png")
        canvas.create_image(552,556,image=self.__photo10,anchor=NW)
        drivername10 = canvas.create_text(650,550,anchor=NW,text="Pierre Gasly",font=("Fixedsys","10"),fill="black")
        driveredad10 = canvas.create_text(650,570,anchor=NW,text="23",font=("Fixedsys","10"),fill="black")
        drivernacionalidad10 = canvas.create_text(650,590,anchor=NW,text="Francés",font=("Fixedsys","10"),fill="black")
        drivertemporada10 = canvas.create_text(650,610,anchor=NW,text="2019",font=("Fixedsys","10"),fill="black")
        drivercompetencias10 = canvas.create_text(875,550,anchor=NW,text="45",font=("Fixedsys","10"),fill="black")
        driverrgp10 = canvas.create_text(1000,550,anchor=NW,text="25,00",font=("Fixedsys","10"),fill="black")
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #
    #Enseñar la información de ayuda
    def show_about(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("About")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/credits.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondo=PhotoImage(file="Fondos/Fondo.gif")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Textos
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
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)#Agregar comando
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        #---------------------------------------------------
         
    def inicio(self):
        for i in self.__master.winfo_children():
            i.destroy()
        Frame.__init__(self,self.__master,background="black")

        #---------------------------------------------------
        Esc = self.__laEscuderia
        Name = Esc.getNombre()
        Icon = Esc.getLogo()
        Location = Esc.getUbicacion()
        Sponsorstring =Esc.getPatrocinadores()
        Sponsors = Esc.getPatrocinadoresLista()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        logo = self.__laEscuderia.getLogo()
        self.__master.title("Formula E CE TEC")
        self.fondo=PhotoImage(file="Fondos/fprincipal.png")
        self.__master.iconbitmap("iconos/principal.ico")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(400,75,anchor=NW,text="Indice Ganador de Escudería",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(500,30,anchor=NW,text="Temporada: 2019",font=("Fixedsys","20","bold"),fill="grey92")
                                                    #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        self.__logoEscuderia = PhotoImage(file=logo)
        canvas.create_image(1050,325,image=self.__logoEscuderia)
        #                                      _____________________________________________________
        #_____________________________________/Iteraciones para datos
        sumaD=0
        for i in self.__laEscuderia.getPilotos():
            destacadas = i.getDestacadas()
            sumaD = sumaD + int(destacadas)
        sumaC=0
        for j in self.__laEscuderia.getPilotos():
            competencias = j.getCompetencias()
            sumaC = sumaC + int(competencias)
        sumaF=0
        for k in self.__laEscuderia.getPilotos():
            fallidas = j.getFallidas()
            sumaF = sumaF + int(fallidas)
        self.__ige = round(sumaD/sumaC,1)
        canvas.create_rectangle(550, 150, 700, 200)
        canvas.create_text(610,165,anchor=NW,text=self.__ige,font=("Fixedsys","17"),fill="red4")
        estado=""
        for l in self.__laEscuderia.getAutomoviles():
            estado = l.getEstado()
        self.__autoestado = estado
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(450,250,anchor=NW,text="Estado del Automovil",font=("Fixedsys","20"),fill="black")
        canvas.create_text(579,305,anchor=NW,text=self.__autoestado,font=("Fixedsys","17"),fill="red4")
        canvas.create_text(450,375,anchor=NW,text="Nombre de la Escuderia",font=("Fixedsys","20"),fill="black")
        canvas.create_text(580,425,anchor=NW,text=Name,font=("system","17"),fill="red4")
        canvas.create_text(545,475,anchor=NW,text="Ubicación",font=("Fixedsys","20"),fill="black")
        canvas.create_text(565,525,anchor=NW,text=Location,font=("system","17"),fill="red4")
        canvas.create_text(75,125,anchor=NW,text="Patrocinadores",font=("Fixedsys","17"),fill="black")
        canvas.create_text(225,125,anchor=NW,text=Sponsorstring,font=("system","17"),fill="red4")
        canvas.create_rectangle(530, 290, 725, 345)
        self.__foto= PhotoImage(file="Automoviles/joselito.gif")
        canvas.create_image(550,600,image=self.__foto,anchor=NW)

        return
    #-------------------------------------------------------------------
    #Editar Escuderia
    def editarEscuderia(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Editar Escuderia")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/engranaje.ico")
        Esc = self.__laEscuderia
        Icon = Esc.getLogo()
        self.informacion= PhotoImage(file="Fondos/feditescuderia.png")
        canvas.create_image(0,0,image=self.informacion,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) 
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(100,100,anchor=NW,text="Editar Escuderia",font=("Fixedsys","20"),fill="black")
        canvas.create_text(100,180,anchor=NW,text="Ubicación Geografica",font=("Fixedsys","17"),fill="black")
        canvas.create_text(100,230,anchor=NW,text="Añadir Patrocinador",font=("Fixedsys","17"),fill="black")
        canvas.create_text(100,280,anchor=NW,text="Eliminar Patrocinador",font=("Fixedsys","17"),fill="black")
        canvas.create_text(100,330,anchor=NW,text="Nuevo Logo",font=("Fixedsys","17"),fill="black")
        #                                      _____________________________________________________
        #_____________________________________/Entrys y botones 
        self.__entryUbicacion = Entry(self.__master)
        self.__entryUbicacion.place(x=350,y=180)
        self.__entryPatrocinador = Entry(self.__master)
        self.__entryPatrocinador.place(x=350,y=230)
        self.__patrocinador = StringVar(self.__master)
        self.__patrocinador.set("Patrocinadores")
        self.__select = self.optionMenuPatrocinadores()
        self.__select.config()
        self.__select.place(x=325,y=280)
        self.__btnBuscar=Button(self.__master,text="Buscar",command=lambda:self.logoEdit())
        self.__btnBuscar.place(x=350,y=330)
        self.__btnGuardar = Button(self.__master,text="Guardar",command=lambda:self.guardaEdit(self.__entryUbicacion.get(),self.__entryPatrocinador.get()))
        self.__btnGuardar.place(x=350,y=380)
        self.__btnBorrar =Button(self.__master,text="Borrar",command=lambda:self.borraPatrocinadores(self.__patrocinador.get()))
        self.__btnBorrar.place(x=500,y=280)
    #--------------------------------------------------------------------------
    #Actualiza el optionmenu de patrocinadores
    def optionMenuPatrocinadores(self):
        lista=[]
        for i in self.__laEscuderia.getPatrocinadoresLista():
            lista.append(i)
        menu = OptionMenu(self.__master,self.__patrocinador,*lista)
        return menu 
    #------------------------------------------------------------------
    #Boorar patrocinadores
    def borraPatrocinadores(self,patrocinador):
        #                                      _____________________________________________________
        #_____________________________________/Borra Patrocinadores
        Esc = self.__laEscuderia
        Esc.removePatrocinadores(patrocinador)
        logo = self.__laEscuderia.getLogo()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Sponsors = Esc.getPatrocinadoresLista()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        
    #-------------------------------------------------------------------
    #Editar Logo
    def logoEdit(self):
        #                                      _____________________________________________________
        #_____________________________________/Guarda el nuevo logo
        self.__rutaImagen = askopenfilename()
        self.__imagen = os.path.abspath(self.__rutaImagen)
        self.__logo = PhotoImage(file=self.__imagen)
        self.__labelImagen = Label(self.__master,image=self.__logo).place(x=600,y=200)
        self.__laEscuderia.setLogo(self.__imagen)
        Esc = self.__laEscuderia
        Name = Esc.getNombre()
        Icon = Esc.getLogo()
        Location = Esc.getUbicacion()
        Sponsorstring =Esc.getPatrocinadores()
        Sponsors = Esc.getPatrocinadoresLista()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        myEscuderia = Escuderia("Alpine",Icon,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
    #-------------------------------------------------------------------
    #Guarda Edit
    def guardaEdit(self,ubicacion,patrocinador):
        #                                      _____________________________________________________
        #_____________________________________/Guarda Edicion del piloto
        self.__entryUbicacion.delete(0,END)
        self.__entryPatrocinador.delete(0,END)
        Esc = self.__laEscuderia
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Esc.setUbicacion(ubicacion)
        Esc.addPatrocinador(patrocinador)
        Sponsors = Esc.getPatrocinadoresLista()
        logo = Esc.getLogo()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        self.inicio()
    #-------------------------------------------------------------------
    #Funcion para crear ventana donde se mostrara el Test Drive
    def show_testdrive(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1004,height=753)
        canvas.pack()
        
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Test Drive")
        self.__master.geometry("1004x753")
        self.__master.iconbitmap("iconos/engranaje.ico")
        self.informacion= PhotoImage(file="interior.gif")
        canvas.create_image(0,0,image=self.informacion,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) 
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
        colorfondo="gray4"
        colorletra="floral white"

        #           _____________________________________
        #__________/Creando el cliente para NodeMCU
        myCar = NodeMCU()
        myCar.start()
        #                                      _____________________________________________________
        #_____________________________________/Botones
        Btn_gizquierda = Button(self.__master,text="Girar Izquierda",fg=colorletra,bg=colorfondo, font=('Agency FB',12),height=1,width=20,command=lambda:self.send("dir:-1;"))
        Btn_gizquierda.place(x=150,y=320)

        Btn_gderecha=Button(self.__master,text="Girar Derecha",fg=colorletra,bg=colorfondo, font=('Agency FB',12),height=1,width=20,command=lambda:self.send("dir:1;"))
        Btn_gderecha.place(x=580,y=320)

        Btn_detenerse=Button(self.__master,text="Detenerse",fg=colorletra,bg=colorfondo, font=('Agency FB',12),height=2,width=30,command=lambda:self.send("pwm:0;"))
        Btn_detenerse.place(x=150,y=625)

        Btn_adelante = Button(self.__master, text="Adelante",fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.send("pwm:1023;"),height=2,width=30)
        Btn_adelante.place(x=550,y=625)

        Btn_atras = Button(self.__master, text="Atras",fg=colorletra,bg=colorfondo, font=('Agency FB',12), command=lambda:self.send("pwm:-1023;"),height=2,width=30)
        Btn_atras. place(x=350, y=625)
    
        Btn_luces_delanteras = Button(self.__master, text="Luces Delanteras", fg=colorletra,bg=colorfondo, font=('Agency FB',12), command=lambda:self.controlar_luces(),height=1,width=20)
        Btn_luces_delanteras.place(x=675,y=250)
    
        Btn_luces_traseras = Button(self.__master, text="Luces Traseras",fg=colorletra,bg=colorfondo, font=('Agency FB',12), command=lambda:self.controlar_luces_traseras(),height=1,width=20)
        Btn_luces_traseras.place(x=675,y=395)

        Btn_direccion_izquierda = Button (self.__master, text="Direccional Izquierda", fg=colorletra,bg=colorfondo, font=('Agency FB',12), command=lambda:self.controlar_direccional_izquierda(),height=1,width=20)
        Btn_direccion_izquierda.place(x=65, y=395)

        Btn_direccion_derecha = Button(self.__master, text="Direccional Derecha", fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.controlar_direccional_derecha(),height=1,width=20)
        Btn_direccion_derecha.place(x=65, y=250)

        Btn_circulo = Button(self.__master, text="Circulo", fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.controlar_circulo(),height=1,width=20)
        Btn_circulo.place(x=550,y=140)

        Btn_ocho = Button(self.__master, text="Infinito",fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.send("infinito;"),height=1,width=20)
        Btn_ocho.place(x=160, y=140)

        Btn_zigzag = Button(self.__master, text="ZigZag", fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.send("zigzag;"),height=1,width=20)
        Btn_zigzag.place(x=370,y=55)

        Btn_especial = Button(self.__master, text="Especial", fg=colorletra,bg=colorfondo, font=('Agency FB',12),command=lambda:self.send("especial;"),height=1,width=20)
        Btn_especial.place(x=370, y=500)
        
    #----------------------------------------------------------------------------------------------------------------------
    #Envia los comandos al Node
        #                                      _____________________________________________________
        #_____________________________________/Comandos del Node
    def send (self,event):
        myCar = NodeMCU()
        myCar.start()
        mns = str(event)
        if(len(mns)>0 and mns[-1] == ";"):
            myCar.send(mns)
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")
    #------------------------------------------------------------------------------------------------------------------------
    #Funciones para hacer movimientos del carro
    def controlar_luces(self):
        control_de_luces_frontales = self.__control_de_luces_frontales
        if(control_de_luces_frontales==0):
            control_de_luces_frontales=1
            self.send("lf:1;")
        else:
            control_de_luces_frontales=0
            self.send("lf:0;")

    def controlar_luces_traseras(self):
        control_de_luces_traseras = self.__control_de_luces_traseras
        if(control_de_luces_traseras==0):
            control_de_luces_traseras=1
            self.send("lb:1;")
        else:
            control_de_luces_traseras=0
            self.send("lb:0;")

    def controlar_direccional_derecha(self):
        direccional_derecha =self.__direccional_derecha
        if(direccional_derecha==0):
           direccional_derecha=1
           self.send("lr:1;")
        else:
           direccional_derecha=0
           self.send("lr:0;")

    def controlar_direccional_izquierda(self):
        direccional_izquierda = self.__direccional_izquierda
        if(direccional_izquierda==0):
            direccional_izquierda=1
            self.send("ll:1;")
        else:
            direccional_izquierda=0
            self.send("ll:0;")

    def controlar_circulo(self):
        circulo = self.__circulo
        if(circulo==1):
            circulo=-1
            self.send("cr:1;")
        else:
            circulo=1
            self.send("cr:-1;")
    #------------------------------------------------------------------------------------------------------
    #Funcion para crear menu que mostrara los carros 
    def show_automoviles(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Automóviles")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/racecar.ico")
        self.fondoam= PhotoImage(file="Fondos/fpilotos.png")
        canvas.create_image(0,0,image=self.fondoam,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Textos
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
                                            #  _____________________________________________________
        #_____________________________________/Menus
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table)
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive)
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
                                            #  _____________________________________________________
        #_____________________________________/Textos
        canvas.create_text(150,15,anchor=NW,text="Automoviles",font=("Fixedsys","14"),fill="red4")
        canvas.create_text(350,15,anchor=NW,text="Eficiencia",font=("Fixedsys","14"),fill="red4")
        
        #Auto1
        self.__photo1 = PhotoImage(file="Automoviles/joselito.gif")
        canvas.create_image(175,52,image=self.__photo1,anchor=NW)
        driverrgp1 = canvas.create_text(425,50,anchor=NW,text="60",font=("Fixedsys","10"),fill="black")

        
        #Auto2
        self.__photo2 = PhotoImage(file="Automoviles/ferrari.png")
        canvas.create_image(50,178,image=self.__photo2,anchor=NW)
        driverrgp2 = canvas.create_text(425,175,anchor=NW,text="70",font=("Fixedsys","10"),fill="black")
        
        #Auto3
        self.__photo3 = PhotoImage(file="Automoviles/force_india.png")
        canvas.create_image(50,304,image=self.__photo3,anchor=NW)
        driverrgp3 = canvas.create_text(425,300,anchor=NW,text="50",font=("Fixedsys","10"),fill="black")

        #Auto4
        self.__photo4 = PhotoImage(file="Automoviles/haas.png")
        canvas.create_image(50,430,image=self.__photo4,anchor=NW)
        driverrgp4 = canvas.create_text(425,425,anchor=NW,text="40",font=("Fixedsys","10"),fill="black")

        #Auto5
        self.__photo5 = PhotoImage(file="Automoviles/mercedes.png")
        canvas.create_image(50,556,image=self.__photo5,anchor=NW)
        driverrgp5 = canvas.create_text(425,550,anchor=NW,text="70",font=("Fixedsys","10"),fill="black")

        #Auto6
        self.__photo6 = PhotoImage(file="Automoviles/redbull.png")
        canvas.create_image(552,52,image=self.__photo6,anchor=NW)
        driverrgp6 = canvas.create_text(1000,50,anchor=NW,text="55",font=("Fixedsys","10"),fill="white")
        
        #Auto7
        self.__photo7 = PhotoImage(file="Automoviles/renault.png")
        canvas.create_image(552,178,image=self.__photo7,anchor=NW)
        driverrgp7 = canvas.create_text(1000,175,anchor=NW,text="65",font=("Fixedsys","10"),fill="black")

        #Auto8
        self.__photo8 = PhotoImage(file="Automoviles/sauber.png")
        canvas.create_image(552,304,image=self.__photo8,anchor=NW)
        driverrgp8 = canvas.create_text(1000,300,anchor=NW,text="85",font=("Fixedsys","10"),fill="black")

        #Auto9
        self.__photo9 = PhotoImage(file="Automoviles/toro_rosso.png")
        canvas.create_image(552,430,image=self.__photo9,anchor=NW)
        driverrgp9 = canvas.create_text(1000,425,anchor=NW,text="45",font=("Fixedsys","10"),fill="black")

        #Auto10
        self.__photo10 = PhotoImage(file="Automoviles/williams.png")
        canvas.create_image(552,556,image=self.__photo10,anchor=NW)
        driverrgp10 = canvas.create_text(1000,550,anchor=NW,text="70",font=("Fixedsys","10"),fill="black")
    #-----------------------------------------------------------------------------------------------------------------------    
    #Funcion para crear ventana que despliega la información de como utilizar la interfaz
    def show_helpwindow(self):
        #                                      _____________________________________________________
        #_____________________________________/Crea Frame 
        for i in self.__master.winfo_children():
            i.destroy()
        
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fhelp= PhotoImage(file="Fondos/fayuda.png")
        canvas.create_image(0,0,image=self.fhelp,anchor=NW)
                                            #  _____________________________________________________
        #_____________________________________/Menus
        canvas.create_text(100,150,anchor=NW,text="En la parte de arriba encontrará una barra con diferentes menus de los cuales"
                           " dependiendo al lugar que quiera\ningresar usted debe cliquear, ejemplo, en el apartado de 'opciones'"
                           "estarán cuatro botones:\n"
                           "-Crear pilotos= Aquí podrá crear nuevos corredores o editando información de ellos como la edad,nombre y más.\n"
                           "-Crear Carros= Al igual que en la opción de pilotos usted puede crear nuevos vehiculos escogiendo el modelo o\n bien editar los autos disponibles.\n"
                           "-Inicio= Al darle a este botón nos retornara a la ventana principal.\n"
                           "-Salir= Esta opción hará que el programa se cierre.\n\n"
                           "En el menú de 'Tabla de posiciones' nos encontraremos con las siguientes opciones:\n"
                           "-Pilotos= Nos mostrará los corredores mas competitivos en un top 10 dependiendo de la cantidad de temporadas\n"
                           " ganadas.\n"
                           "-Automóviles= En esta ventana mostrará los autos acomodándolos del más eficiente al mas ineficiente del 1 al 10.\n\n"
                           "Y por último en el menú de 'Test Drive' aparecerá unicaménte la opción:\n"
                           "-Halo View= En ella saldrá una simulación del interior del coche y mostrará por medio de los sensores información,\n que le indicará"
                           " si el carro esta en condiciones para correr o si no lo está."
                           ,font=("Fixedsys","15"),fill="black")
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("¿Cómo se utiliza?")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/question.ico")
        #                                      _____________________________________________________
        #_____________________________________/Menu
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir",command=root.destroy)
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about) #Agregar comando
        self.aboutmenu.add_command(label="Como Útilizar",command=self.show_helpwindow)#Agregar comando
        self.menuvar.add_cascade(label="Ayuda",menu=self.aboutmenu)
        self.tablemenu = Menu(self.menuvar,tearoff=0)
        self.tablemenu.add_command(label="Pilotos",command=self.position_table) #Agrega comando
        self.tablemenu.add_command(label="Automoviles",command=self.show_automoviles)#Agregar comando
        self.menuvar.add_cascade(label="Tabla de Posiciones",menu=self.tablemenu)
        self.testmenu = Menu(self.menuvar,tearoff=0)
        self.testmenu.add_command(label="Halo View",command=self.show_testdrive) #Agregar comando
        self.menuvar.add_cascade(label="Test Drive",menu=self.testmenu)
        root.config(menu=self.menuvar)
#Datos de la ventana
root= Tk()
root.geometry("1280x800")
iniciar = Ventana_inicio(root)
root.mainloop()
