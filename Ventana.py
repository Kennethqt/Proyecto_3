from tkinter import *
from Escuderia import *
from tkinter.filedialog import askopenfilename
color1="gray20"
from Carro import *
from Piloto import *
from Pickle import *
import os
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
        Sponsors = Esc.getPatrocinadoresLista()
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()

    #----------------------------------------------------
    #Crea los carros
    def crear_carros(self):
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Automóviles")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/racecar.ico")
        self.fondoam= PhotoImage(file="Fondos/fautos2.png")
        canvas.create_image(0,0,image=self.fondoam,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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
        canvas.create_text(150,75,anchor=NW,text="Crear Automovil",font=("Fixedsys","20"),fill="black")       
        canvas.create_text(150,130,anchor=NW,text="Marca",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,180,anchor=NW,text="Modelo",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,230,anchor=NW,text="Pais",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,280,anchor=NW,text="Temporada",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,330,anchor=NW,text="Baterias",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,380,anchor=NW,text="Pilas",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,430,anchor=NW,text="Estado",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,480,anchor=NW,text="Consumo",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,530,anchor=NW,text="Sensores",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,580,anchor=NW,text="Peso",font=("Fixedsys","17"),fill="black")
        canvas.create_text(150,630,anchor=NW,text="Eficiencia",font=("Fixedsys","17"),fill="black")
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
        self.__btnCrear = Button(self.__master,text="Crear",command=lambda:self.newCar(self.__entryMarca.get(),self.__entryModelo.get(),self.__entryPais.get(),self.__entryTemporada.get(),self.__entryNumBaterias.get(),self.__entryCanPilas.get(),self.__entryEstado.get(),self.__entryConsumo.get(),self.__entrySensores.get(),self.__entryPeso.get(),self.__entryEficiencia.get()))
        self.__btnCrear.place(x=300,y=660)

        canvas.create_text(600,75,anchor=NW,text="Editar Automovil",font=("Fixedsys","20"),fill="black")
        canvas.create_text(600,130,anchor=NW,text="Nueva Marca",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,180,anchor=NW,text="Nuevo Modelo",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,230,anchor=NW,text="Nuevo Pais",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,280,anchor=NW,text="Nueva Temporada",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,330,anchor=NW,text="Baterias",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,380,anchor=NW,text="Cantidad de Pilas",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,430,anchor=NW,text="Nuevo Estado",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,480,anchor=NW,text="Consumo",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,530,anchor=NW,text="Sensores",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,580,anchor=NW,text="Nuevo Peso",font=("Fixedsys","17"),fill="black")
        canvas.create_text(600,630,anchor=NW,text="Eficiencia",font=("Fixedsys","17"),fill="black")
        self.__carroselect = StringVar(self.__master)
        self.__carroselect.set("Seleccionar Carro")
        self.__select = self.optionMenuCar()
        self.__select.config()
        self.__select.place(x=850,y=130)
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
        self.__btnEditar = Button(self.__master,text="Editar",command=lambda:self.editCarro(self.__carroselect.get()))
        self.__btnEditar.place(x=850,y=660)
        self.__btnGuardar = Button(self.__master,text="Guardar",command=lambda:self.guardaInfoCar(self.__carroselect.get()))
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
        newCar = Carro(marca,modelo,pais,temporada,baterias,pilas,estado,consumo,sensores,peso,eficiencia)
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
        self.__entryN.delete(0,END)
        self.__entryE.delete(0,END)
        self.__entryNa.delete(0,END)
        self.__entryT.delete(0,END)
        self.__entryC.delete(0,END)
        self.__entryD.delete(0,END)
        self.__entryF.delete(0,END)
        newPiloto=Piloto(nombre,edad,nacionalidad,temporada,can_competencias,destacadas,fallidas)
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
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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

    #Editar Carro
    def editCarro(self,carro):
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
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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
        self.testmenu.add_command(label="Halo View")
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
        self.__master.iconbitmap("iconos/credits.ico")
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        self.fondo=PhotoImage(file="Fondos/Fondo.gif")
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
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Salir")#Agregar comando
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
        self.testmenu.add_command(label="Halo View")
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
        logo = self.__laEscuderia.getLogo()
        self.__master.title("Formula E CE TEC")
        self.fondo=PhotoImage(file="Fondos/fprincipal.png")
        self.__master.iconbitmap("iconos/principal.ico")
        canvas.create_image(0,0,image=self.fondo,anchor=NW)
        canvas.create_text(400,75,anchor=NW,text="Indice Ganador de Escudería",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(500,30,anchor=NW,text="Temporada: 2019",font=("Fixedsys","20","bold"),fill="grey92")
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
        self.optionsmenu.add_command(label="Inicio",command=self.inicio)
        self.optionsmenu.add_command(label="Editar Escuderia",command=self.editarEscuderia)
        self.optionsmenu.add_command(label="Salir")
        self.menuvar.add_cascade(label="Opciones",menu=self.optionsmenu)
        self.aboutmenu = Menu(self.menuvar,tearoff=0)
        self.aboutmenu.add_command(label="Créditos", command = self.show_about)
        self.aboutmenu.add_command(label="Como Útilizar", command=self.show_helpwindow)#Agregar comando
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
        canvas.create_image(1050,165,image=self.__logoEscuderia)
        sumaD=0
        for i in self.__laEscuderia.getPilotos():
            destacadas = i.getDestacadas()
            sumaD = sumaD + int(destacadas)
        sumaC=0
        for j in self.__laEscuderia.getPilotos():
            competencias = i.getCompetencias()
            sumaC = sumaC + int(competencias)
        sumaF=0
        for k in self.__laEscuderia.getPilotos():
            fallidas = i.getFallidas()
            sumaF = sumaF + int(fallidas)
        self.__ige = round(sumaD/sumaC,1)
        canvas.create_rectangle(550, 150, 700, 200)
        canvas.create_text(610,165,anchor=NW,text=self.__ige,font=("Fixedsys","17"),fill="black")
        estado=""
        for l in self.__laEscuderia.getAutomoviles():
            estado = l.getEstado()
        self.__autoestado = estado
        canvas.create_text(450,250,anchor=NW,text="Estado del Automovil",font=("Fixedsys","20"),fill="black")
        canvas.create_text(580,300,anchor=NW,text=self.__autoestado,font=("Fixedsys","17"),fill="black")
        canvas.create_rectangle(530, 290, 725, 345)
        self.__carroselect = StringVar(self.__master)
        self.__carroselect.set("Seleccionar Carro")
        self.__select = self.optionMenuInicio()
        self.__select.config()
        self.__select.place(x=150,y=130)
        return
    #------------------------------------------------------------------------
    #Option Menu pantalla
    def optionMenuInicio(self):
        lista=[]
        for i in self.__laEscuderia.getAutomoviles():
            marca = i.getMarca()
            lista.append(marca)
            menu = OptionMenu(self.__master,self.__carroselect, *lista)
        return menu
    #-------------------------------------------------------------------
    #Editar Escuderia
    def editarEscuderia(self):
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Test Drive")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("engranaje.ico")
        self.informacion= PhotoImage(file="fprincipal.png")
        canvas.create_image(0,0,image=self.informacion,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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
        canvas.create_text(100,100,anchor=NW,text="Editar Escuderia",font=("Fixedsys","20","bold"),fill="black")
        canvas.create_text(100,180,anchor=NW,text="Ubicación Geografica",font=("Fixedsys","17"),fill="black")
        canvas.create_text(100,230,anchor=NW,text="Añadir Patrocinador",font=("Fixedsys","17"),fill="black")
        canvas.create_text(100,280,anchor=NW,text="Nuevo Logo",font=("Fixedsys","17"),fill="black")
        self.__entryUbicacion = Entry(self.__master)
        self.__entryUbicacion.place(x=350,y=180)
        self.__entryPatrocinador = Entry(self.__master)
        self.__entryPatrocinador.place(x=350,y=230)
        self.__patrocinador = StringVar(self.__master)
        self.__patrocinador.set("Patrocinadores")
        self.__select = self.optionMenuPatrocinadores()
        self.__select.config()
        self.__select.place(x=550,y=280)
        self.__txtnewLogo = Label(self.__master,image=self.__logoEscuderia)
        self.__btnBuscar=Button(self.__master,text="Buscar",command=lambda:self.logoEdit())
        self.__btnBuscar.place(x=350,y=280)
        self.__btnGuardar = Button(self.__master,text="Guardar",command=lambda:self.guardaEdit(self.__entryUbicacion.get(),self.__entryPatrocinador.get(),a))
        self.__btnGuardar.place(x=500,y=280)
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
        self.__rutaImagen = askopenfilename()
        self.__imagen = os.path.abspath(self.__rutaImagen)
        self.__logo = PhotoImage(file=self.__imagen)
        self.__labelImagen = Label(self.__master,image=self.__logo).place(x=100,y=330)
        
    #-------------------------------------------------------------------
    #Guarda Edit
    def guardaEdit(self,ubicacion,patrocinador,logo):
        self.__entryUbicacion.delete(0,END)
        self.__entryPatrocinador.delete(0,END)
        Esc = self.__laEscuderia
        Esc.setLogo(logo)
        Drivers = Esc.getPilotos()
        Cars = Esc.getAutomoviles()
        Esc.setUbicacion(ubicacion)
        Esc.addPatrocinador(patrocinador)
        Sponsors = Esc.getPatrocinadoresLista()
        logo = Esc.getLogo()
        Location = Esc.getUbicacion()
        myEscuderia = Escuderia("Alpine",logo,Location,Sponsors,Drivers,Cars)
        write_inicial(myEscuderia)
        
    #-------------------------------------------------------------------

    #Funcion para crear ventana donde se mostrara el Test Drive
    def show_testdrive(self):
        for i in self.__master.winfo_children():
            i.destroy()
            
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("Test Drive")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/engranaje.ico")
        self.informacion= PhotoImage(file="Fondos/interior.png")
        canvas.create_image(0,0,image=self.informacion,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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
        self.__master.iconbitmap("iconos/racecar.ico")
        self.fondoam= PhotoImage(file="Fondos/fautos2.png")
        canvas.create_image(0,0,image=self.fondoam,anchor=NW)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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


    #Funcion para crear ventana que despliega la información de como utilizar la interfaz
    def show_helpwindow(self):
        for i in self.__master.winfo_children():
            i.destroy()
        
        canvas=Canvas(self.__master,bg="white",width=1280,height=800)
        canvas.pack()
        canvas.create_text(200,150,anchor=NW,text="En la parte de arriba encontrará una barra con diferentes\nmenus de las cuales"
                           " dependiendo al lugar que quiera ingresar\nusted debe clickar, ejemplo, en el apartado de 'opciones'\n"
                           "estarán tres botones, el primero 'Escuderías' lo enviará a\nuna ventana en el que usted puede editar y crear pilotos.\n"
                           "En la opción de 'Inicio' lo retornará almenu principal y el\nde 'Salir' cerrará la interfaz.\n\nEn la opción de 'Tabla de posiciones'",font=("Fixedsys","20","bold"),fill="black")
        Frame.__init__(self,self.__master,background="black")
        self.__master.title("¿Cómo se utiliza?")
        self.__master.geometry("1280x800")
        self.__master.iconbitmap("iconos/question.ico")
        
            
        self.menuvar = Menu(self.__master)
        self.menuvar = Menu(self.__master)
        self.optionsmenu = Menu(self.menuvar,tearoff=0)
        self.optionsmenu.add_command(label="Crear Pilotos",command=self.crear_pilotos)
        self.optionsmenu.add_command(label="Crear Carros",command=self.crear_carros)
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
    

     

#Datos de la ventana
root= Tk()
root.geometry("1280x800")
iniciar = Ventana_inicio(root)
root.mainloop()
