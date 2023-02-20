import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext , Toplevel, LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatosPacintes, listarCondicion ,listar, editarDatoPaciente, eliminarPaciente
from modelo.historiaMedicaDao import historiaMedica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date



class Frame(tk.Frame):
    def __init__(self ,root):
        super().__init__(root, width=1280, height=720)
        self.root =root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None
        self.idHistoriaMedicaEditar = None
        self.capmposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def capmposPaciente(self):
        #levels
        self.lblNombre = tk.Label(self,text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblNombre.grid(column=0,row=0,padx=10, pady=5)


        self.lblApePaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApePaterno.config(font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblApePaterno.grid(column=0,row=1,padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApeMaterno.config(font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblApeMaterno.grid(column=0,row=2,padx=10, pady=5)

        self.lblDni = tk.Label(self, text='DNi: ')
        self.lblDni.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0,row=3,padx=10, pady=5)

        self.lblFechaNacimiento= tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechaNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechaNacimiento.grid(column=0,row=4,padx=10, pady=5)

        self.lblEDAD = tk.Label(self, text='Edad: ')
        self.lblEDAD.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEDAD.grid(column=0,row=5,padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0,row=6,padx=10, pady=5)
        
        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0,row=7,padx=10, pady=5)


        self.lblTelefono = tk.Label(self, text='Teléfono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0,row=8,padx=10, pady=5)

        #entris
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50, font=('ARIAL',15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50, font=('ARIAL',15))
        self.entryApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL',15))
        self.entryDni.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFechadeNacimiento = tk.StringVar()
        self.entryFechadeNacimiento = tk.Entry(self, textvariable=self.svFechadeNacimiento)
        self.entryFechadeNacimiento.config(width=50, font=('ARIAL',15))
        self.entryFechadeNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecedentes= tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo= tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono= tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)


        #buttons
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0,row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarDatoPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1,row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2,row=9, padx=10, pady=5)

        #buscador
        #label buscador
        self.lblBuscarDni =tk.Label(self, text= 'Buscar DNI: ')
        self.lblBuscarDni.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarDni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido =tk.Label(self, text= 'Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #Entrys buscador
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=('ARIAL',15))
        self.entryBuscarDni.grid(column=4, row=0, padx=10, pady=5,columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5,columnspan=2)

        #button buscador
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command = self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3,row=2, padx=10, pady=5, columnspan= 1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command = self.LimpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnLimpiarBuscador.grid(column=4,row=2, padx=10, pady=5, columnspan= 1)

        #button calendario
        self.btnCalendario = tk.Button(self, text='Calendario', command = self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                              bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnCalendario.grid(column=3,row=4, padx=10, pady=5, columnspan= 1)
    
    def vistaCalendario(self):
        self.calendario =Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar()
        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1990, month=1, day=1, locale ='es_US', 
                                bg ='#777777', fg ='#FFFFFF' , headersbackground ='#B6DDFE', cursor = 'hand2', date_pattern ='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column = 0)

        #trace enviar fecha
        
        self.svCalendario.trace('w' ,self.enviarFecha)
    
    def enviarFecha(self, *args):
       self.svFechadeNacimiento.set('' + self.svCalendario.get())
       if len(self.calendar.get_date()) > 1:
        self.svCalendario.trace('w', self.calcularEdad)
    
    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)












    def LimpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()


    
    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE DNI = " + self.svBuscarDni.get() + "" #WHERE
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarApellido.get()+ "%' AND activo = 1"
                
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()




    def guardarDatoPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(), self.svDni.get(), 
            self.svFechadeNacimiento.get(), self.svEdad.get(), self.svAntecedentes.get(), self.svCorreo.get(), self.svTelefono.get()
        )
        if self.idPersona == None:
            guardarDatosPacintes(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        
        self.deshabilitar()
        self.tablaPaciente()


    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFechadeNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        
        
        self.entryNombre.config(state='normal')
        self.entryApePaterno.config(state='normal')
        self.entryApeMaterno.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFechadeNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')


        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')




    
    def deshabilitar(self):
        self.idPersona = None

        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFechadeNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        
        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFechadeNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')


        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')

        self.btnCalendario.config(state='disabled')
    
    def tablaPaciente(self, where=""):
        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            self.listaPersona.reverse()
        
        self.tabla = ttk.Treeview(self, columns=('Nombre','APaterno','AMaterno','Dni','FNacimiento','Edad','Antecedentes','Correo','Telefono'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)
        self.tabla.tag_configure('evenrow', background='#C5EAFE')


        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Ap. Paterno')
        self.tabla.heading('#3',text='Ap. Materno')
        self.tabla.heading('#4',text='Dni')
        self.tabla.heading('#5',text='F. Nacimiento')
        self.tabla.heading('#6',text='Edad')
        self.tabla.heading('#7',text='Antecedentes')
        self.tabla.heading('#8',text='Correo')
        self.tabla.heading('#9',text='Telefono')


        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=300)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=82)

        for p in self.listaPersona:
            
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow' ,))
        
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=11, column=4, padx=10, pady=5)
    
    def historiaMedica(self):
        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']

            if (self.idPersona > 0):
                idPersona = self.idPersona
            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.config(bg='#CDD8FF')

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Apellido','Fecha Historia','Motivo','Examen Auxiliar','Tratamiento','Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical',command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=8,sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Auxiliar')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=100)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=500)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0],values=(p[1],p[2],p[3],p[4],p[5],p[6]))

            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#3A005D', cursor='hand2',activebackground='#B47CD6')
            self.btnEditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#890011', cursor='hand2',activebackground='#D8939C')
            self.btnEliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#6F6F6F')
            self.btnSalirHistoria.grid(row=2, column=6, padx=10, pady=5)
        except:
            title ='Historia Medica'
            mensaje ='Error al mostrar historial'
            messagebox.showerror(title, mensaje)
    
    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGRAGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg='#CDD8FF')
        
        #frame1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill='both', expand='yes', pady=10, padx=20)
        #labels agregar historia medica
        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de la Historia Medica', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblMotivoHistoria.grid(row=0, column=0, padx=5,pady=3)

        self.lblExamenAuxiliarHistoria = tk.Label(self.frameDatosHistoria, text='Examen Auxiliar', width=20, font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblExamenAuxiliarHistoria.grid(row=2, column=0, padx=5,pady=3)

        self.lblTratamientoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento', width=20, font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTratamientoHistoria.grid(row=4, column=0, padx=5,pady=3)

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistoria, text='Detalle de la Historia Medica', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblDetalleHistoria.grid(row=6, column=0, padx=5,pady=3)

        #entrys agrega historia medica
        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria =tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=70, font=('ARIAL',15))
        self.motivoHistoria.grid(row=1, column=0, padx= 5, pady=3, columnspan=2)

        self.svExamenAuxiliarHistoria = tk.StringVar()
        self.examenAuxiliarHistoria =tk.Entry(self.frameDatosHistoria, textvariable=self.svExamenAuxiliarHistoria)
        self.examenAuxiliarHistoria.config(width=70, font=('ARIAL',15))
        self.examenAuxiliarHistoria.grid(row=3, column=0, padx= 5, pady=3, columnspan=2)

        self.svTratamientoHistoria = tk.StringVar()
        self.tratamientoHistoria =tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoHistoria)
        self.tratamientoHistoria.config(width=70, font=('ARIAL',15))
        self.tratamientoHistoria.grid(row=5, column=0, padx= 5, pady=3, columnspan=2)

        self.svDetalleHistoria = tk.StringVar()
        self.detalleHistoria =tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalleHistoria)
        self.detalleHistoria.config(width=70, font=('ARIAL',15))
        self.detalleHistoria.grid(row=7, column=0, padx= 5, pady=3, columnspan=2)

        #frame 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

        #label fecha agregar historia
        self.lblFechaHistoria =tk.Label(self.frameFechaHistoria, text= 'Fecha y Hora', width=20, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        #entry fecha agragar historia
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=('ARIAL',15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        #traer fecha y hora actual
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))
        #buttons agrega historia 
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Agregar Historia', command=self.agregarHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12,'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2',activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir', command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=('ARIAL', 12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#646464')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

    
    def agregarHistorialMedico(self):
        try:
            if self.idHistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(), self.svMotivoHistoria.get(), self.svExamenAuxiliarHistoria.get(), self.svTratamientoHistoria.get(),self.svDetalleHistoria.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title = 'Agregar Historia'
            mensaje = 'Error al agregar historia Medica'
            messagebox.showerror(title, mensaje)
    
    def eliminarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)
            self.idHistoriaMedica = None
            self.topHistoriaMedica.destroy()
        except:
            title = 'Eliminar historia'
            mensaje = 'Error al eliminar'
            messagebox.showerror(title, mensaje)
    
    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.motivoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.exaMenAuxiliarHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.tratamientoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.detalleHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.config(bg='#CDD8FF')

            #frame editar datos historia
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#CDD8FF')
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

            #label editar historia
            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text='Motivo de la historia', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=3)

            self.lblExamenAuxiliarEditar = tk.Label(self.frameEditarHistoria, text='Examen Auxiliar', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblExamenAuxiliarEditar.grid(row=2, column=0, padx=5, pady=3)

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text='Tratamiento', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblTratamientoEditar.grid(row=4, column=0, padx=5, pady=3)

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text='Detalle de la Historia', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblDetalleEditar.grid(row=6, column=0, padx=5, pady=3)

          
            
            #entrys editar historia
            self.svMotivoEditar =  tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=('ARIAL',15))
            self.entryMotivoEditar.grid(row = 1, column=0 , pady=3, padx=5, columnspan=2)

            self.svExamenAuxiliarEditar =  tk.StringVar()
            self.entryExamenAuxiliarEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svExamenAuxiliarEditar)
            self.entryExamenAuxiliarEditar.config(width=65, font=('ARIAL',15))
            self.entryExamenAuxiliarEditar.grid(row = 3, column=0 , pady=3, padx=5, columnspan=2)

            self.svTratamientoEditar =  tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=65, font=('ARIAL',15))
            self.entryTratamientoEditar.grid(row = 5, column=0 , pady=3, padx=5, columnspan=2)

            self.svDetalleEditar =  tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=65, font=('ARIAL',15))
            self.entryDetalleEditar.grid(row = 7, column=0 , pady=3, padx=5, columnspan=2)


            #frame decha editar
            self.frameFechaEditar =tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#CDD8FF')
            self.frameFechaEditar.pack(fill="both",expand="yes", padx=20, pady=10)
            #label fecha editar
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5,pady=3)

            #entry fecha editar
            self.svFechaHistoriaEditar =  tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=('ARIAL',15))
            self.entryFechaHistoriaEditar.grid(row = 1, column=1 , pady=3, padx=5)

            #insertar los valores a los entrys
            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar)
            self.entryExamenAuxiliarEditar.insert(0, self.exaMenAuxiliarHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            #button editar historia
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Editar Historia', command = self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#030058', cursor='hand2', activebackground='#8986DA')
            self.btnEditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Salir', command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#676767')
            self.btnSalirEditarHistoriaMedica.grid(row=2, column=1, padx=10, pady=5)

            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica

            self.idHistoriaMedica = None




        except:
            title = 'Editar Historia'
            mensaje =  'Error al editar historia'
            messagebox.showerror(title, mensaje)

    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svExamenAuxiliarEditar.get(),self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)
            self.topEditarHistoria.destroy()             






    

    
    
    
    def salirTop(self):
        self.topHistoriaMedica.destroy()
    
    
    
    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.ApellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.ApellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimentoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.ApellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.ApellidoMaternoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFechadeNacimiento.insert(0, self.fechaNacimentoPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)
        
        except:
            title ='Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title , mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)

            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)

















        







    


        