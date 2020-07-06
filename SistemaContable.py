# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:52:21 2020

@author: sar_n
"""
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql


#global loginNames
global empresas, meses, anios

empresas = ["Technolaser", "InfoSer", "Tech Lead", "Fallabela", "Paris", "Jumbo"]
empresas.sort()
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
         "Octubre","Noviembre","Diciempre"]
anios = [2016, 2017, 2018, 2019, 2020]
loginNames = [["nicolas", "qwerty"], ["admin", "admin"], ["rodrigo", "123"]]

#Clases
"""class database():
    def __init__(self):
        connection = pymysql.connect(
        host="localhost", user="root", password="", db="sistema_contable")
        cursor = connection.cursor()
    
    def __users__(self):
        sql = "SELECT * FROM login"
"""
        
#Programa
def seleccionContribuyente():
    global ventana_seleccion
    ventana_seleccion = Tk() 
    ventana_seleccion.title("Selección de Contribuyente") 
    ventana_seleccion.geometry('350x200')
    ventana_seleccion.config(bg = "lightblue")
    
    #column = 0, row = 0
    espacio_texto = Label(ventana_seleccion,
                    text = "Elija el contribuyente, mes y año que desea ver")
    espacio_texto.pack()
    espacio_seleccion = Label(ventana_seleccion)
    espacio_seleccion.pack()
    
    comboEmpresa = Combobox(espacio_seleccion, 
                            state = "readonly") #Combobox(ventana_seleccion)
    comboEmpresa.config(width = "30") 
    comboEmpresa['values']= empresas
    comboEmpresa.current(0) #set the selected item 
    comboEmpresa.grid(column = 0, row = 1)
    
    espacio = Label(espacio_seleccion, text = "")
    espacio.grid(column = 0, row = 2)
    
    comboMeses = Combobox(espacio_seleccion, state = "readonly") #Combobox(ventana_seleccion)
    comboMeses.config(width = "25") 
    comboMeses['values']= meses
    comboMeses.current(0) #set the selected item 
    comboMeses.grid(column = 0, row = 3)
    
    comboAnios = Combobox(espacio_seleccion, state = "readonly") #Combobox(ventana_seleccion)
    comboAnios.config(width = "10") 
    comboAnios['values']= anios
    comboAnios.current(0) #set the selected item 
    comboAnios.grid(column = 1, row = 3)
    
    espacio2 = Label(espacio_seleccion, text = "")
    espacio2.grid(column = 0, row = 4)
    
    seleccion = Button(espacio_seleccion,
           text="Seleccionar", 
           width=15, #height=2,
           #font = ("Arial", 15),
           command = menuEmpresa)
    seleccion.grid(column = 0, row = 5)
    
    volver = Button(espacio_seleccion,
           text="Volver", 
           width=15, #height=2,
           #font = ("Arial", 15),
           command = volverAtras)
    volver.grid(column = 1, row = 5)
     
    ventana_seleccion.mainloop()

def menuEmpresa():
    ventana_seleccion.destroy()
    menuBarEmpresa()
    
def volverAtras():
    ventana_seleccion.destroy()

#Menu despues de elegir una empresa
def menuBarEmpresa():
    # Crear el menu principal
    menubarra = Menu(ventana_inicial)
    
    #Voucher
    menubarra.add_command(label="Voucher", command=hola)
    
    # Menu mantencion de tablas
    menuEmpresa = Menu(menubarra, tearoff=0)
    menuEmpresa.add_command(label="Empresa", command=hola)
    menuEmpresa.add_command(label="Centro de costo", command=hola)
    menuEmpresa.add_command(label="Plan de cuentas", command=hola)
    menuEmpresa.add_command(label="Impuestos", command=hola)
    menuEmpresa.add_command(label="Sucursales", command=hola)
    menuEmpresa.add_command(label="Tipo documentos", command=hola)
    menuEmpresa.add_command(label="Clasificación", command=hola)
    menuEmpresa.add_command(label="Parametros", command=hola)
    menuEmpresa.add_command(label="Vendedores", command=hola)
    menubarra.add_cascade(label="Mantencion de tablas", menu=menuEmpresa)
    
    # Menu Consultas
    menuMantencion = Menu(menubarra, tearoff=0)
    menuMantencion.add_command(label="Saldos", command=hola)
    menuMantencion.add_command(label="Libros de mayor", command=hola)
    menuMantencion.add_command(label="Analisis", command=hola)
    menubarra.add_cascade(label="Consultas", menu=menuMantencion)
    
    #Menu de usuario
    menuUsuario = Menu(menubarra, tearoff=0)
    menuUsuario.add_command(label="Cambiar contraseña", command=hola)
    if admin:#==True:
        menuUsuario.add_command(label="Agregar Usuario", command=hola)
        menuUsuario.add_command(label="Editar Usuario", command=hola)
        menuUsuario.add_command(label="ELiminar Usuario", command=hola)
    menuUsuario.add_separator()
    menuUsuario.add_command(label="Cerrar Sesión", command=cierre)
    menuUsuario.add_command(label="Salir Programa", command=ventana_inicial.quit)
    menubarra.add_cascade(label="Usuario", menu=menuUsuario)    
    
    #Menu de ayuda
    menuayuda = Menu(menubarra, tearoff=0)
    menuayuda.add_command(label="Acerca de...", command=hola)
    menubarra.add_cascade(label="Ayuda", menu=menuayuda)
    
    # Finalmente bucle de la ventana
    ventana_inicial.config(menu = menubarra)

def menuBar():
        
    # Crear el menu principal
    menubarra = Menu(ventana_inicial)
    
    # Menu empresas
    menuEmpresa = Menu(menubarra, tearoff=0)
    menuEmpresa.add_command(label="Seleccionar", command=seleccionContribuyente)
    menuEmpresa.add_command(label="Nuevo", command=hola)
    menuEmpresa.add_command(label="Editar", command=hola)
    menuEmpresa.add_command(label="Eliminar", command=hola)
    #menuEmpresa.add_separator()
    #menuEmpresa.add_command(label="Salir", command=root.quit)
    menubarra.add_cascade(label="Contribuyente", menu=menuEmpresa)
    
    # Menu
    """menuMantencion = Menu(menubarra, tearoff=0)
    menuMantencion.add_command(label="SubMenu", command=hola)
    menuMantencion.add_command(label="SubMenu", command=hola)
    menuMantencion.add_command(label="SubMenu", command=hola)
    menubarra.add_cascade(label="Menu2", menu=menuMantencion)"""
    
    #Menu de usuario
    menuUsuario = Menu(menubarra, tearoff=0)
    menuUsuario.add_command(label="Cambiar contraseña", command=hola)
    if admin:#==True:
        menuUsuario.add_command(label="Agregar Usuario", command=hola)
        menuUsuario.add_command(label="Editar Usuario", command=hola)
        menuUsuario.add_command(label="ELiminar Usuario", command=hola)
    menuUsuario.add_separator()
    menuUsuario.add_command(label="Cerrar Sesión", command=cierre)
    menubarra.add_cascade(label="Usuario", menu=menuUsuario)    
    
    #Menu de ayuda
    menuayuda = Menu(menubarra, tearoff=0)
    menuayuda.add_command(label="Acerca de...", command=hola)
    menubarra.add_cascade(label="Ayuda", menu=menuayuda)
    
    #Salida del programa
    menubarra.add_command(label="Salir", command=ventana_inicial.quit)
    
    # Finalmente bucle de la ventana
    ventana_inicial.config(menu = menubarra)
    
def cierre():
    ventana_inicial.destroy()
    ventana_login()

def hola():
    print "Hola!"
        

def ventana_login():
    global ventana_principal
    ventana_principal=Tk()
    ventana_principal.geometry("760x400")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("CONTABILIDAD")#TITULO DE LA VENTANA
    Label(text="Bienvenido\n Ingrese sus datos de inicio de sesion para empezar", 
          fg="black",    # Foreground
          bg="lightblue", #Background
          width="300", height="2",  #Tamaño
          font=("Arial",20)).pack()#ETIQUETA CON TEXTO
    Label(bg="lightblue", #Background
          text="").pack() 
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_principal,
          text="Nombre usuario * ",
          bg="lightblue", #Background
          width = "20", height= "2",
          font = ("Arial", 18)).pack()
    entrada_login_usuario = Entry(ventana_principal,
                                  width = "50",  
                                  textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_principal,
          bg="lightblue", #Background
          text="").pack()
    Label(ventana_principal, 
          text="Contraseña * ",
          bg="lightblue", #Background
          width = "20", height= "2",
          font = ("Arial", 18)).pack()
    entrada_login_clave = Entry(ventana_principal,
                                width = "50",
                                textvariable=verifica_clave, 
                                show= '*')
    entrada_login_clave.pack()
    Label(ventana_principal, 
          bg="lightblue", #Background
          text="").pack()
    Button(ventana_principal, 
           text="Acceder", 
           width=15, height=2,
           font = ("Arial", 15),
           command = verifica_login).pack()   
    ventana_principal.config(bg="lightblue",
                             bd=15,
                             relief="ridge")
    ventana_principal.mainloop()

#VENTANA "VERIFICACION DE LOGIN".
def verifica_login():
    global admin
    admin = False
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    if usuario1 != "" and clave1 != "":
        entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
        entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
        for i in range(len(loginNames)):
            if usuario1 == loginNames[i][0]:
                if clave1 == loginNames[i][1]:
                    ventana_principal.destroy()                
                    if usuario1 == "admin":
                        admin = True
                        ventana_inicio()
                    else:
                        admin = False
                        ventana_inicio()
                    break
                #SI LA CONTRASEÑA NO SE ENCUENTRA EN LOS ARCHIVOS....
                else:
                    messagebox.showerror("ERROR", "Error, contraseña incorreca")
    #    SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN LOS ARCHIVOS...
    elif i == len(loginNames)-1:
        messagebox.showerror("ERROR", "Error, usuario no encontrado")
    elif usuario1 == "":
        messagebox.showerror("ERROR", "Error, usuario no ingresado")
    elif clave1 == "":
        messagebox.showerror("ERROR", "Error, contraseña no ingresada")
    
def ventana_inicio():
    global ventana_inicial
    ventana_inicial = Tk()
    ventana_inicial.title("CONTABILIDAD")
    ventana_inicial.geometry("1440x720")
    ventana_inicial.config(bg="blue",
                           bd=15,
                           relief="ridge")

    label1 = Label()
    label1.pack(fill='both', expand=1)
    label1.config(bg="lightblue",
                  bd=25,
                  relief="sunken")
    
    label = Label(label1)
    label.pack(anchor=CENTER)
    label.config(fg="black",    # Foreground
                 bg="lightblue", #Background
                 text="SISTEMA COMPUTACIONAL\n SUPER CONTABILIDAD PARA CONTADORES\n Versión 1.0\n \nEntregado a: <CLIENT NAME>",
                 font=("Arial",28))
                 
    label2 = Label(label1)
    label2.pack(anchor=CENTER, pady=170, padx=150, fill="both")
    label2.config(bg="lightblue") #Background
                 
    espacio = Label(label1)
    espacio.config(bg="lightblue") #Background
    espacio.pack()
    
    menuBar()
  
    
    
    
#cambio de contraseña
def cambio_de_password():
    global ventana_cambio_pass
    ventana_cambio_pass = Toplevel(ventana_inicial)
    ventana_cambio_pass.title("Cambio de contraseña")
    ventana_cambio_pass.geometry("400x250")
    ventana_cambio_pass.config(bg="lightBlue")
 
    global usuario
    global antigua
    global nueva
    global valida_nueva
    usuario = StringVar()
    antigua = StringVar() 
    nueva = StringVar() 
    valida_nueva = StringVar() 
 
    entrada_usuario = Label(ventana_cambio_pass, 
                            text="Ingrese Usuario *", 
                            font=("Arial", 12))
    entrada_usuario.pack()
    entrada_usuario = Entry(ventana_cambio_pass, 
                            textvariable=usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_usuario.pack()
    entrada_antigua_pass = Label(ventana_cambio_pass, 
                                 text="Ingrese su antigua contraseña *", 
                                 font=("Arial", 12))
    entrada_antigua_pass.pack()
    entrada_antigua_pass = Entry(ventana_cambio_pass, 
                                 textvariable=antigua, 
                                 show='*') #ESPACIO PARA INTRODUCIR LA ANTIGUA PASS.
    entrada_antigua_pass.pack()
    etiqueta_clave = Label(ventana_cambio_pass, 
                           text="Ingrese su nueva contraseña *", 
                           font=("Arial", 12))
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_cambio_pass, 
                          textvariable=nueva, 
                          show='*') #ESPACIO PARA INTRODUCIR LA NUEVA CONTRASEÑA.
    entrada_clave.pack()
    etiqueta_valida_clave = Label(ventana_cambio_pass,
                                  text="Ingrese su nueva contraseña otra vez *", 
                                  font=("Arial", 12))
    etiqueta_valida_clave.pack()
    etiqueta_valida_clave = Entry(ventana_cambio_pass, 
                                  textvariable=valida_nueva, 
                                  show='*') #ESPACIO PARA RE-INTRODUCIR LA NUEVA CONTRASEÑA.
    etiqueta_valida_clave.pack()
    Label(ventana_cambio_pass, text="", bg="lightBlue").pack()
    Button(ventana_cambio_pass, 
           text="Cambiar", 
           width=10, height=1,
           command = valida_cambio,
           font=("Arial", 12)).pack() #BOTÓN "Registrarse"

def valida_cambio():
    user = usuario.get()
    antigua_pass = antigua.get()
    nueva_pass = nueva.get()
    validar = valida_nueva.get()
    
    if nueva_pass != validar:
        messagebox.showerror("ERROR", "Error, las contraseñas no coinciden")
    else:
        for i in range(len(loginNames)):
            if loginNames[i][0] == user and loginNames[i][1] == antigua_pass:
                loginNames[i][1] = nueva_pass
                messagebox.showinfo("Info", "La contraseña se cambio correctamente")
                break
                

def seleccion():
    print "salio el comando abrir"
    
def main():
#    bdconection()
    ventana_login()

if __name__ == '__main__':
    main()