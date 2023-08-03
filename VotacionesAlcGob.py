#FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA-01
#PROYECTO FINAL - VOTACION EN ALCALDIA Y GOBERNACION
#NICOLAS HERRERA MARULANDA - 2182551
#SAMUEL ESTEIMAN GALINDO CUEVAS - 2177491
#YENNY MARGOT RIVAS TELLO - 2182527

from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from pathlib import Path

Datos = [[],[],[],[]]
CantidadVotos = [[],[],[],[],[],[],[]]
CantidadGeneros = [[],[],[],[]]

def RegistrarValidarCedulaGenero():
    Cedula = ecedula.get()

    Validacion = 0
    
    if Cedula != "":
        if Cedula.isdigit() == True:
            if Datos[0] != []:
                for i in Datos[0]:
                    if i == Cedula:
                        messagebox.showerror(message="Esta cedula ya esta registrada")
                        Validacion = 1
        else:
            messagebox.showinfo(title="Error", message="Por favor digite unicamente numeros enteros")
            Validacion = 1         
    else:
        messagebox.showinfo(title="Error", message="Por favor digite un numero de cedula")
        Validacion = 1
    
    if Validacion == 0:
        if 1 <= Genero.get() <= 2:
            if Genero.get() == 2:
                Datos[1].append("F")
            elif Genero.get() == 1:
                Datos[1].append("M")
            Datos[0].append(Cedula)
            PagRegistroCedulaGenero.destroy()
        else:
            messagebox.showinfo(title="Error",message="Por favor seleccione un genero")
               
def RegistrarValidarVotos():

    VotoAlcaldia, VotoGobernacion = selection.get(), selection2.get()

    if 1 <= VotoAlcaldia <= 4 or 1 <= VotoGobernacion <= 4:
        if VotoAlcaldia == 1:
            Datos[2].append("V1")
        elif VotoAlcaldia == 2:
            Datos[2].append("V2")
        elif VotoAlcaldia == 3:
            Datos[2].append("V3")
        elif VotoAlcaldia == 4:
            Datos[2].append("VB")

        if VotoGobernacion == 1:
            Datos[3].append("V1")
        elif VotoGobernacion == 2:
            Datos[3].append("V2")
        elif VotoGobernacion == 3:
            Datos[3].append("V3")
        elif VotoGobernacion == 4:
            Datos[3].append("VB")
        PagRegistroVotos.destroy()
    else:
        messagebox.showinfo(title="Error", message="Por favor elija un candidato de una coorporacion")

def PararVotacion():
    PagLoginAdministrador = Toplevel()
    PagLoginAdministrador.title("Login")
    Centrar(PagLoginAdministrador, 150, 150)
    lusurario = Label(PagLoginAdministrador, text="Usuario", font=("Arial",9,"bold"))
    eusuario = Entry(PagLoginAdministrador)
    lcontraseña = Label(PagLoginAdministrador, text="Contraseña", font=("Arial",9,"bold"))
    econtraseña = Entry(PagLoginAdministrador)
    blogin = Button(PagLoginAdministrador, text="Login", command= lambda : Login(econtraseña, eusuario, PagLoginAdministrador))

    lusurario.pack()
    eusuario.pack()
    lcontraseña.pack()
    econtraseña.pack()
    blogin.pack()

    PagLoginAdministrador.grab_set()
    PagLoginAdministrador.focus_set()
    PagLoginAdministrador.resizable(0,0)
    PagLoginAdministrador.mainloop()

def Login(self, self2, pag):
    Contraseña = self.get()
    Usuario = self2.get()
    if Contraseña == "12345" and Usuario == "Admin":
        global x
        x = 1
        PagRegistroCedulaGenero.destroy()
        pag.destroy()
    elif Contraseña != "12345" or Usuario != "Admin":
        messagebox.showerror(title="Error", message="Usuario o Contraseña incorrectas")

def Centrar(r, altura, anchura):
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    CordenadasX = (anchura_pantalla // 2) - (anchura//2)
    CordenadasY = (altura_pantalla//2) - (altura//2)
    r.geometry(str(anchura)+"x"+str(altura)+"+"+str(CordenadasX)+"+"+str(CordenadasY))   

def ContarVotosGeneros():
    m, f = Datos[1].count("M"), Datos[1].count("F")
    Candidatos = ["V1", "V2", "V3", "VB"]
    for i in range (2,4,1):
        for a in Candidatos:
            if i == 2:
                if a == "VB":
                    CantidadVotos[2].append(Datos[2].count(a))
                else:
                    CantidadVotos[0].append(Datos[2].count(a)) 
            if i == 3:
                if a == "VB":
                    CantidadVotos[3].append(Datos[3].count(a))
                else:
                    CantidadVotos[1].append(Datos[3].count(a))
    
    Generos =["F", "M"]
    for i in Generos:
        CantidadGeneros[0].append(Datos[1].count(i))
    TotalGeneros = len(Datos[1])
    if TotalGeneros != 0:    
        CantidadGeneros[1].append((CantidadGeneros[0][0]/TotalGeneros)*100)
        CantidadGeneros[1].append((CantidadGeneros[0][1]/TotalGeneros)*100)
    else:
        CantidadGeneros[1].append(0)
        CantidadGeneros[1].append(0)

    CantidadVotos[4].append(len(Datos[2]))
    CantidadVotos[5].append(len(Datos[3]))
    CantidadVotos[6].append(CantidadVotos[4][0] + CantidadVotos[5][0])

RutaImagenCandidato = Path('cand.png').absolute()
RutaImagenCandidatoSeleccioando = Path('candsec.png').absolute()
RutaImagenVotoBlanco = Path('vb.png').absolute()
RutaImagenVotoBlancoSeleccioando = Path('vbs.png').absolute()

x = 0
while True:
    PagRegistroCedulaGenero = Tk()
    Centrar(PagRegistroCedulaGenero, 300, 300)
    PagRegistroCedulaGenero.title("Registrar datos del votante")
    Genero = IntVar()

    lcedula = Label(PagRegistroCedulaGenero, text="Cedula", font=("Arial",9,"bold"))
    ecedula = Entry(PagRegistroCedulaGenero, text="Cedula")
    lgenero = Label(PagRegistroCedulaGenero, text="Genero", font=("Arial",9,"bold"))
    brmasculino = Radiobutton(PagRegistroCedulaGenero, text="Masculino", variable= Genero, value=1)
    brfemenino = Radiobutton(PagRegistroCedulaGenero, text="Femenino", variable= Genero, value=2)
    bregistrar = Button(PagRegistroCedulaGenero, text="Registrar", command=RegistrarValidarCedulaGenero)
    bpararVotacion = Button(PagRegistroCedulaGenero, text="Parar Votación", fg="red", command=PararVotacion)

    lcedula.grid(row=0, column=0, columnspan=3)
    ecedula.grid(row=1, column=0, columnspan=3)
    lgenero.grid(row=3, column=0, columnspan=3)
    brmasculino.grid(row=4, column=0, padx=30)
    brfemenino.grid(row=4, column=2, padx=30)
    bregistrar.grid(row=6, column=2, padx=30, pady=160)
    bpararVotacion.grid(row=6, column=0, padx=30, pady=160)

    PagRegistroCedulaGenero.protocol("WM_DELETE_WINDOW", False)
    PagRegistroCedulaGenero.resizable(0,0)
    PagRegistroCedulaGenero.mainloop()

    if x == 1:
        break

    PagRegistroVotos = Tk()
    PagRegistroVotos.title("Votación")
    Centrar(PagRegistroVotos, 400, 700)

    selection = IntVar()
    selection2 = IntVar()

    ImagenCandidato = PhotoImage(file=RutaImagenCandidato)
    ImagenSeleccionCandidato = PhotoImage(file=RutaImagenCandidatoSeleccioando)
    ImagenVotoBlanco = PhotoImage(file=RutaImagenVotoBlanco)
    ImagenSeleccionVotaBlanco = PhotoImage(file=RutaImagenVotoBlancoSeleccioando)

    FontInstitucion = Font(size=16, weight="bold")

    lalcaldia = Label(PagRegistroVotos, text="Alcaldia", font=FontInstitucion)
    lcandidatoAlcaldia1 = Label(PagRegistroVotos, text="Candidato 1", justify="center")
    BRcandidatoAlcaldia1 = Radiobutton(PagRegistroVotos, text="Candidato 1", image= ImagenCandidato, variable= selection, value= 1, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lcandidatoAlcaldia2 = Label(PagRegistroVotos, text="Candidato 2", justify="center")
    BRcandidatoAlcaldia2 = Radiobutton(PagRegistroVotos, text="Candidato 2", variable= selection, value= 2, image= ImagenCandidato, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lcandidatoAlcaldia3 = Label(PagRegistroVotos, text="Candidato 3", justify="center")
    BRcandidatoAlcaldia3 = Radiobutton(PagRegistroVotos, text="Candidato 3", variable= selection, value= 3, image= ImagenCandidato, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lvotoblancoAlcaldia = Label(PagRegistroVotos, text="Voto en blanco", justify="center")
    BRvotoBlancoAlcaldia = Radiobutton(PagRegistroVotos, text="Voto en blanco", variable= selection, value= 4, image= ImagenVotoBlanco, indicatoron=0, selectimage=ImagenSeleccionVotaBlanco)

    lgobernacion = Label(PagRegistroVotos, text="Gobernación", font=FontInstitucion)
    lcandidatoGob1 = Label(PagRegistroVotos, text="Candidato 1", justify="center")
    BRcandidatoGob1 = Radiobutton(PagRegistroVotos, text="Candidato 1", variable= selection2, value= 1, image= ImagenCandidato, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lcandidatoGob2 = Label(PagRegistroVotos, text="Candidato 2", justify="center")
    BRcandidatoGob2 = Radiobutton(PagRegistroVotos, text="Candidato 2", variable= selection2, value= 2, image= ImagenCandidato, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lcandidatoGob3 = Label(PagRegistroVotos, text="Candidato 3", justify="center")
    BRcandidatoGob3 = Radiobutton(PagRegistroVotos, text="Candidato 3", variable= selection2, value= 3, image= ImagenCandidato, indicatoron=0, selectimage=ImagenSeleccionCandidato)
    lvotoblancoGob = Label(PagRegistroVotos, text="Voto en blanco", justify="center")
    BRvotoBlancoGob = Radiobutton(PagRegistroVotos, text="Voto en blanco", variable= selection2, value= 4, image= ImagenVotoBlanco, indicatoron=0, selectimage=ImagenSeleccionVotaBlanco)
    
    Bvotar = Button(PagRegistroVotos, text="Votar", command=RegistrarValidarVotos)

    lalcaldia.grid(column=0, row=0, columnspan=4, pady=20)
    lcandidatoAlcaldia1.grid(column=0, row=1, padx=50)
    lcandidatoAlcaldia2.grid(column=1, row=1, padx=50)
    lcandidatoAlcaldia3.grid(column=2, row=1, padx=50)
    lvotoblancoAlcaldia.grid(column=3, row=1, padx=50)
    
    BRcandidatoAlcaldia1.grid(column=0, row=2, padx=50)
    BRcandidatoAlcaldia2.grid(column=1, row=2, padx=50)
    BRcandidatoAlcaldia3.grid(column=2, row=2, padx=50)
    BRvotoBlancoAlcaldia.grid(column=3, row=2, padx=50)

    lgobernacion.grid(column=0, row=4, columnspan=4, pady=20)
    lcandidatoGob1.grid(column=0, row=5)
    lcandidatoGob2.grid(column=1, row=5)
    lcandidatoGob3.grid(column=2, row=5)
    lvotoblancoGob.grid(column=3, row=5)
    
    BRcandidatoGob1.grid(column=0, row=6)
    BRcandidatoGob2.grid(column=1, row=6)
    BRcandidatoGob3.grid(column=2, row=6)
    BRvotoBlancoGob.grid(column=3, row=6)
    
    Bvotar.grid(column=3, row=8, pady=20)

    altura = PagRegistroVotos.winfo_reqheight()
    anchura = PagRegistroVotos.winfo_reqwidth()

    PagRegistroVotos.protocol("WM_DELETE_WINDOW", False)
    PagRegistroVotos.resizable(0,0)
    PagRegistroVotos.mainloop()

ContarVotosGeneros()

PagResultados = Tk()
PagResultados.title("Resultados")
Centrar(PagResultados, 320, 572)

for i in range (0,2,1):
    if CantidadVotos[i].count(max(CantidadVotos[i])) == 1:
        print(max(CantidadVotos[i]))
        for a in range (0,3,1):
            if i == 0 and CantidadVotos[0][a] == max(CantidadVotos[0]):
                ganadoralc = "Candidato "+str(a+1)
            elif i == 1 and CantidadVotos[1][a] == max(CantidadVotos[1]):
                ganadorgob = "Candidato "+str(a+1)
    else:
        if i == 0:
            ganadoralc = "Empate"
        if i == 1:
            ganadorgob = "Empate"

MResultados = [["Alcaldia"],["GANADOR",ganadoralc],["TOTAL VOTOS", CantidadVotos[4][0]],["VOTOS EN BLANCO", CantidadVotos[2][0]],["Gobernacion"],["GANADOR", ganadorgob],["TOTAL VOTOS", CantidadVotos[5][0]],["VOTOS EN BLANCO", CantidadVotos[3][0]],["Totales"], ["TOTAL VOTOS",CantidadVotos[6][0]],["TOTAL HOMBRES", CantidadGeneros[0][1]],["TOTAL MUJERES", CantidadGeneros[0][0]],["PORCENTAJE HOMBRES", CantidadGeneros[1][1]],["PORCENTAJE MUJERES", CantidadGeneros[1][0]]]

for i in range(len(MResultados)):
    for a in range(len(MResultados[i])):
        if i == 0 or i ==4 or i == 8:
            lresultados = Label(PagResultados, text=MResultados[i][a], width=20, relief="solid", borderwidth=1, font=("Arial",16,"bold"))
            lresultados.grid(row=i, column=a, padx=1, pady=1, columnspan=2, sticky="nesw")
        else:
            lresultados = Label(PagResultados, text=MResultados[i][a], width=40, relief="solid", borderwidth=1)
            lresultados.grid(row=i, column=a, padx=1, pady=1, sticky="nesw")
        PagResultados.grid_rowconfigure(i, weight=1)
        PagResultados.grid_columnconfigure(a, weight=1)

PagResultados.mainloop()