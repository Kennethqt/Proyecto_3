from tkinter import *
class Ventana_inicio(Frame):

    def __init__(self,master):
        Frame.__init__(self,master, background="black")
        self.__master = master
        self.inicio()
        return
    def inicio(self):
        self.__master.title("Formula E CE TEC")
        self.fondo=PhotoImage(file="Fondo.gif")
        self.LabelFondo=Label(self.__master,image=self.fondo)
        self.LabelFondo.place(x=0,y=0)
        self.txt_temporada=Label(self.__master,text="Temporada",font="Fixedsys 24",fg="grey92",bg="black")
        self.txt_temporada.place(x=100, y=150)
        self.txt_ige=Label(self.__master,text="Indice Ganador\nde Escuderia", font="Fixedsys 24",fg="grey92",bg="black")
        self.txt_ige.place(x= 100,y=250)

        
        return
root= Tk()
root.geometry("1004x753")
iniciar = Ventana_inicio(root)
root.mainloop()
